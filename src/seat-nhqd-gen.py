import json
from collections import defaultdict

# --------------------------------------------
# 1) Helper: seat numbering + alignment
# --------------------------------------------
def generate_numbers(parity, start, end, direction):
    """
    Builds a list of seat numbers from `start`..`end` (inclusive),
    filtered by parity ('odd', 'even', or 'all'),
    then sorted ascending or descending.
    """
    low, high = (min(start, end), max(start, end))
    all_nums = range(low, high + 1)
    
    if parity == "odd":
        nums = [n for n in all_nums if n % 2 == 1]
    elif parity == "even":
        nums = [n for n in all_nums if n % 2 == 0]
    else:  # 'all'
        nums = list(all_nums)
    
    if direction == "asc":
        nums.sort()
    else:  # 'desc'
        nums.sort(reverse=True)
    
    return nums

def place_seats_right_aligned(seat_nums, anchor_x, spacing_x):
    """
    Right-align these seats at anchor_x.
    seat i=0 -> x=anchor_x
    seat i=1 -> x=anchor_x - spacing_x, etc.
    Returns a list of (seat_num, x_position).
    """
    coords = []
    for i, seat_num in enumerate(seat_nums):
        x = anchor_x - i * spacing_x
        coords.append((seat_num, x))
    return coords

def place_seats_center_aligned(seat_nums, anchor_x, spacing_x):
    """
    Center-align these seats around anchor_x.
    If n seats, total width = (n-1)*spacing_x.
    seat i=0 starts at anchor_x - total_width/2.
    Returns a list of (seat_num, x_position).
    """
    coords = []
    n = len(seat_nums)
    total_width = (n - 1) * spacing_x if n > 1 else 0
    leftmost_x = anchor_x - (total_width / 2)
    for i, seat_num in enumerate(seat_nums):
        x = leftmost_x + i * spacing_x
        coords.append((seat_num, x))
    return coords

def place_seats_left_aligned(seat_nums, anchor_x, spacing_x):
    """
    Left-align these seats starting at anchor_x.
    seat i=0 -> x=anchor_x
    seat i=1 -> x=anchor_x + spacing_x, etc.
    Returns a list of (seat_num, x_position).
    """
    coords = []
    for i, seat_num in enumerate(seat_nums):
        x = anchor_x + i * spacing_x
        coords.append((seat_num, x))
    return coords

# --------------------------------------------
# 1a) Helper: assign seat zone based on rules
# --------------------------------------------
def get_zone(row, num):
    """
    Determine the zone category for a seat based on its row letter and seat number.
    Zones:
      - Back rows (S, T, U, V, X, Y) are all zone5.
      - For rows A-E and F-I, etc., assign zones per provided numeric ranges.
      - Leftover seats not in zones 1-3 are assigned to zone4.
    """
    # Back rows: S, T, U, V, X, Y
    if row in ["R", "S", "T", "U", "V", "X", "Y"]:
        return "zone5"
    
    if row == "A":
        if 1 <= num <= 15:
            return "zone1"
        elif 16 <= num <= 19:
            return "zone2"
        elif 20 <= num <= 23:
            return "zone3"
        else:
            return "zone4"
    if row == "B":
        if 1 <= num <= 16:
            return "zone1"
        elif 17 <= num <= 20:
            return "zone2"
        elif 21 <= num <= 24:
            return "zone3"
        else:
            return "zone4"
    if row == "C":
        if 1 <= num <= 17:
            return "zone1"
        elif 18 <= num <= 21:
            return "zone2"
        elif 22 <= num <= 25:
            return "zone3"
        else:
            return "zone4"
    if row == "D":
        if 1 <= num <= 18:
            return "zone1"
        elif 19 <= num <= 22:
            return "zone2"
        elif 23 <= num <= 26:
            return "zone3"
        else:
            return "zone4"
    if row == "E":
        if 1 <= num <= 19:
            return "zone1"
        elif 20 <= num <= 23:
            return "zone2"
        elif 24 <= num <= 27:
            return "zone3"
        else:
            return "zone4"
    if row in ["F", "G", "H", "I"]:
        if row == "F":
            if 1 <= num <= 16:
                return "zone1"
            elif 17 <= num <= 28:
                return "zone2"
            else:
                return "zone4"
        else:  # For G, H, I
            if 1 <= num <= 16:
                return "zone1"
            elif 17 <= num <= 20:
                return "zone2"
            elif 21 <= num <= 28:
                return "zone3"
            else:
                return "zone4"
    if row in ["K", "L"]:
        if 1 <= num <= 20:
            return "zone2"
        elif 21 <= num <= 28:
            return "zone3"
        else:
            return "zone4"
    if row == "M":
        if 1 <= num <= 20:
            return "zone2"
        elif 21 <= num <= 24:
            return "zone3"
        else:
            return "zone4"
    if row == "N":
        if 1 <= num <= 24:
            return "zone3"
        else:
            return "zone4"
    if row == "O":
        if 1 <= num <= 17:
            return "zone3"
        else:
            return "zone4"
    if row in ["P", "Q", "R"]:
        return "zone4"
    
    return "zone4"  # Default

# --------------------------------------------
# 2) Row specs: same seat numbering rules
# --------------------------------------------
row_specs = {
    "A": {
        "left":   {"parity": "odd",  "start": 13, "end": 31, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 11, "direction": "desc"},
        "right":  {"parity": "even", "start": 12, "end": 30, "direction": "asc"}
    },
    "B": {
        "left":   {"parity": "odd",  "start": 13, "end": 31, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 12, "direction": "desc"},
        "right":  {"parity": "even", "start": 14, "end": 32, "direction": "asc"}
    },
    "C": {
        "left":   {"parity": "odd",  "start": 15, "end": 33, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 13, "direction": "desc"},
        "right":  {"parity": "even", "start": 14, "end": 32, "direction": "asc"}
    },
    "D": {
        "left":   {"parity": "odd",  "start": 15, "end": 35, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 14, "direction": "desc"},
        "right":  {"parity": "even", "start": 16, "end": 36, "direction": "asc"}
    },
    "E": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 15, "direction": "desc"},
        "right":  {"parity": "even", "start": 16, "end": 36, "direction": "asc"}
    },
    "F": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 38, "direction": "asc"}
    },
    "G": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "H": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "I": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "K": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "L": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "M": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 38, "direction": "asc"}
    },
    "N": {
        "left":   {"parity": "odd",  "start": 17, "end": 23, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 24, "direction": "asc"}
    },
    "O": {
        "left":   {"parity": "odd",  "start": 19, "end": 25, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 24, "direction": "asc"}
    },
    "P": {
        "left":   {"parity": "odd",  "start": 17, "end": 21, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 22, "direction": "asc"}
    },
    # Row Q: no center block; only left and right blocks are defined.
    "Q": {
        "left":   {"parity": "odd",  "start": 13, "end": 17, "direction": "asc"},
        "right":  {"parity": "even", "start": 14, "end": 18, "direction": "asc"}
    },
    "S": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 15, "direction": "desc"},
        "right":  {"parity": "even", "start": 16, "end": 36, "direction": "asc"}
    },
    "T": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "U": {
        "left":   {"parity": "odd",  "start": 19, "end": 41, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "V": {
        "left":   {"parity": "odd",  "start": 19, "end": 35, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 36, "direction": "asc"}
    },
    "X": {
        "left":   {"parity": "odd",  "start": 19, "end": 21, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 18, "direction": "desc"},
        "right":  {"parity": "even", "start": 20, "end": 24, "direction": "asc"}
    },
    "Y": {
        "left":   {"parity": "odd",  "start": 17, "end": 21, "direction": "asc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 22, "direction": "asc"}
    }
}

# --------------------------------------------
# 3) Layout / positioning config
# --------------------------------------------
ROW_SPACING_Y = 40
BASE_Y = 100
SEAT_SPACING_X = 30  # spacing within each block
LEFT_BLOCK_ANCHOR_X   = 250
CENTER_BLOCK_ANCHOR_X = 650  # 400 difference from left anchor
RIGHT_BLOCK_ANCHOR_X  = 1050 # 400 difference from center anchor

# We also add extra vertical offsets after certain rows.
extra_vertical_offset = 0

# --------------------------------------------
# 4) Prepare seat_data and text_data
# --------------------------------------------
seat_data = []
text_data = []

# (4a) Prepend the "Sân Khấu" text object
text_data.append({
    "id": "116a57ac-9bc2-4f0c-a9fc-e1a57448bda7",
    "x": 578.3721923828125,
    "y": -5.1,
    "label": "Sân Khấu",
    "fontSize": 35,
    "fontWeight": 200,
    "letterSpacing": 5,
    "color": "#ffffff",
    "embraceOffset": False,
    "rotation": 0
})

# Ordered rows (using the dictionary order)
ordered_rows = list(row_specs.keys())
seat_id = 1
current_row_index = 0

for row_letter in ordered_rows:
    # Compute Y position, adding any extra offsets
    y_pos = BASE_Y + (current_row_index * ROW_SPACING_Y) + extra_vertical_offset
    
    # 1) Generate seat numbers for left, center, right blocks
    spec_left = row_specs[row_letter]["left"]
    spec_center = row_specs[row_letter].get("center")  # may be None (e.g. for row Q)
    spec_right = row_specs[row_letter]["right"]
    
    left_nums = generate_numbers(spec_left["parity"], spec_left["start"], spec_left["end"], spec_left["direction"])
    if spec_center is not None:
        center_nums = generate_numbers(spec_center["parity"], spec_center["start"], spec_center["end"], spec_center["direction"])
    else:
        center_nums = []  # For row Q, no center seats.
    right_nums = generate_numbers(spec_right["parity"], spec_right["start"], spec_right["end"], spec_right["direction"])
    
    # 2) Place them with alignment
    left_coords = place_seats_right_aligned(left_nums, LEFT_BLOCK_ANCHOR_X, SEAT_SPACING_X)
    center_coords = place_seats_center_aligned(center_nums, CENTER_BLOCK_ANCHOR_X, SEAT_SPACING_X)
    right_coords = place_seats_left_aligned(right_nums, RIGHT_BLOCK_ANCHOR_X, SEAT_SPACING_X)
    
    # 3) Create seat objects with a "block" property.
    for seat_num, x_pos in left_coords:
        zone = get_zone(row_letter, seat_num)
        seat_data.append({
            "id": f"seat-{seat_id}",
            "block": "left",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_letter}{seat_num}",
            "square": True,
            "status": "Available",
            "category": zone
        })
        seat_id += 1
    
    for seat_num, x_pos in center_coords:
        zone = get_zone(row_letter, seat_num)
        seat_data.append({
            "id": f"seat-{seat_id}",
            "block": "center",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_letter}{seat_num}",
            "square": True,
            "status": "Available",
            "category": zone
        })
        seat_id += 1
    
    for seat_num, x_pos in right_coords:
        zone = get_zone(row_letter, seat_num)
        seat_data.append({
            "id": f"seat-{seat_id}",
            "block": "right",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_letter}{seat_num}",
            "square": True,
            "status": "Available",
            "category": zone
        })
        seat_id += 1
    
    # 4) Create text objects for row labels (placed between the blocks)
    mid_left_center = (LEFT_BLOCK_ANCHOR_X + CENTER_BLOCK_ANCHOR_X) / 2 - 100
    mid_center_right = (CENTER_BLOCK_ANCHOR_X + RIGHT_BLOCK_ANCHOR_X) / 2 + 100
    
    text_data.append({
        "id": f"text-{row_letter}-LC",
        "x": mid_left_center,
        "y": y_pos + 15,
        "label": row_letter,
        "fontSize": 20,
        "fontWeight": 400,
        "letterSpacing": 0,
        "color": "#000000",
        "embraceOffset": False,
        "rotation": 0
    })
    text_data.append({
        "id": f"text-{row_letter}-CR",
        "x": mid_center_right,
        "y": y_pos + 15,
        "label": row_letter,
        "fontSize": 20,
        "fontWeight": 400,
        "letterSpacing": 0,
        "color": "#000000",
        "embraceOffset": False,
        "rotation": 0
    })
    
    # 5) Adjust extra_vertical_offset after rows E and Q.
    if row_letter == "E" or row_letter == "Q":
        extra_vertical_offset += 100
    if row_letter == "Q":
        extra_vertical_offset += 100
        text_data.append({
            "id": "text-tret2",
            "x": CENTER_BLOCK_ANCHOR_X,
            "y": y_pos + 100,
            "label": "Trệt",
            "fontSize": 34,
            "fontWeight": 600,
            "letterSpacing": 1,
            "color": "#000000",
            "embraceOffset": False,
            "rotation": 0
        })
    
    # 6) After the last row (Y), add text "Lầu"
    final_y = BASE_Y + (current_row_index - 1) * ROW_SPACING_Y + extra_vertical_offset
    if row_letter == "Y":
        text_data.append({
            "id": "text-lau",
            "x": CENTER_BLOCK_ANCHOR_X,
            "y": final_y + 120,
            "label": "Lầu",
            "fontSize": 34,
            "fontWeight": 600,
            "letterSpacing": 1,
            "color": "#000000",
            "embraceOffset": False,
            "rotation": 0
        })
    
    current_row_index += 1

# --------------------------------------------
# 5) Save to seats.json and texts.json
# --------------------------------------------
with open("seats.json", "w") as f:
    json.dump(seat_data, f, indent=4)

with open("texts.json", "w") as f:
    json.dump(text_data, f, indent=4)

print("Done! Generated seats.json for seat data and texts.json for text objects.")

# --------------------------------------------
# 6) Print summary counts
# --------------------------------------------
# Summary by block (left, center, right)
row_block_counts = defaultdict(lambda: {"left": 0, "center": 0, "right": 0})
overall_block_counts = {"left": 0, "center": 0, "right": 0}

# Summary by category (zone)
row_category_counts = defaultdict(lambda: defaultdict(int))
overall_category_counts = defaultdict(int)

for seat in seat_data:
    # Extract row letter from label (e.g., "A15" -> "A")
    row_letter = seat["label"][0]
    block = seat["block"]
    category = seat["category"]
    
    row_block_counts[row_letter][block] += 1
    overall_block_counts[block] += 1
    
    row_category_counts[row_letter][category] += 1
    overall_category_counts[category] += 1

# Print block counts per row
print("\nSeat counts per row and block (with row totals):")
for row in sorted(row_block_counts.keys()):
    row_total = sum(row_block_counts[row].values())
    print(f"Row {row} (Total: {row_total}):")
    for blk in ["left", "center", "right"]:
        print(f"  {blk}: {row_block_counts[row][blk]}")

print("\nOverall block counts:")
for blk in ["left", "center", "right"]:
    print(f"  {blk}: {overall_block_counts[blk]}")

# Print category counts per row
print("\nSeat counts per row and category (with row totals):")
for row in sorted(row_category_counts.keys()):
    row_total = sum(row_category_counts[row].values())
    print(f"Row {row} (Total: {row_total}):")
    for cat, count in row_category_counts[row].items():
        print(f"  {cat}: {count}")

print("\nOverall category counts:")
for cat, count in overall_category_counts.items():
    print(f"  {cat}: {count}")
