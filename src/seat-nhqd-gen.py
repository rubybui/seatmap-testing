import json

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
    => seats extend leftward as i increases.
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
    => seats extend to the right from there.
    Returns a list of (seat_num, x_position).
    """
    coords = []
    n = len(seat_nums)
    if n > 1:
        total_width = (n - 1) * spacing_x
    else:
        total_width = 0
    
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
    => seats extend rightward as i increases.
    Returns a list of (seat_num, x_position).
    """
    coords = []
    for i, seat_num in enumerate(seat_nums):
        x = anchor_x + i * spacing_x
        coords.append((seat_num, x))
    return coords

# --------------------------------------------
# 2) Row specs: same seat numbering rules
# --------------------------------------------
row_specs = {
    "A": {
        "left":   {"parity": "odd",  "start": 13, "end": 31, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 11, "direction": "desc"},
        "right":  {"parity": "even", "start": 12, "end": 30, "direction": "asc"}
    },
    "B": {
        "left":   {"parity": "odd",  "start": 13, "end": 31, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 12, "direction": "desc"},
        "right":  {"parity": "even", "start": 14, "end": 32, "direction": "asc"}
    },
    "C": {
        "left":   {"parity": "odd",  "start": 15, "end": 33, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 13, "direction": "desc"},
        "right":  {"parity": "even", "start": 14, "end": 32, "direction": "asc"}
    },
    "D": {
        "left":   {"parity": "odd",  "start": 15, "end": 35, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 14, "direction": "desc"},
        "right":  {"parity": "even", "start": 16, "end": 36, "direction": "asc"}
    },
    "E": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 15, "direction": "desc"},
        "right":  {"parity": "even", "start": 16, "end": 36, "direction": "asc"}
    },
    "F": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 38, "direction": "asc"}
    },
    "G": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "H": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "I": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "K": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "L": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "M": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 38, "direction": "asc"}
    },
    "N": {
        "left":   {"parity": "odd",  "start": 17, "end": 23, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 24, "direction": "asc"}
    },
    "O": {
        "left":   {"parity": "odd",  "start": 17, "end": 25, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 24, "direction": "asc"}
    },
    "P": {
        "left":   {"parity": "odd",  "start": 17, "end": 23, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 22, "direction": "asc"}
    },
    "Q": {
        "left":   {"parity": "odd",  "start": 13, "end": 17, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 12, "direction": "desc"},
        "right":  {"parity": "even", "start": 14, "end": 18, "direction": "asc"}
    },
    "R": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 15, "direction": "desc"},
        "right":  {"parity": "even", "start": 16, "end": 36, "direction": "asc"}
    },
    "S": {
        "left":   {"parity": "odd",  "start": 17, "end": 37, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 15, "direction": "desc"},
        "right":  {"parity": "even", "start": 16, "end": 36, "direction": "asc"}
    },
    "T": {
        "left":   {"parity": "odd",  "start": 17, "end": 39, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 16, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "U": {
        "left":   {"parity": "odd",  "start": 19, "end": 41, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 40, "direction": "asc"}
    },
    "V": {
        "left":   {"parity": "odd",  "start": 19, "end": 39, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 17, "direction": "desc"},
        "right":  {"parity": "even", "start": 18, "end": 38, "direction": "asc"}
    },
    "X": {
        "left":   {"parity": "odd",  "start": 19, "end": 21, "direction": "desc"},
        "center": {"parity": "all",  "start":  1, "end": 18, "direction": "desc"},
        "right":  {"parity": "even", "start": 20, "end": 24, "direction": "asc"}
    },
    "Y": {
        "left":   {"parity": "odd",  "start": 17, "end": 21, "direction": "desc"},
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
# We want bigger horizontal gaps (100 more points than previously).
# For instance:
LEFT_BLOCK_ANCHOR_X   = 250
CENTER_BLOCK_ANCHOR_X = 650  # 400 difference from left anchor
RIGHT_BLOCK_ANCHOR_X  = 1050 # 400 difference from center anchor

# We also add 100 points after finishing row E, and another 100 points after finishing row Q.
# We'll track a dynamic offset that increments after E and Q.
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

# Sort the rows if you want alphabetical, or just keep the order in the dictionary
ordered_rows = list(row_specs.keys())  # or sorted(row_specs.keys())

seat_id = 1
current_row_index = 0

for row_letter in ordered_rows:
    # Compute Y position, adding any extra offsets
    y_pos = BASE_Y + (current_row_index * ROW_SPACING_Y) + extra_vertical_offset
    
    # 1) Generate seat numbers for left, center, right
    spec_left   = row_specs[row_letter]["left"]
    spec_center = row_specs[row_letter]["center"]
    spec_right  = row_specs[row_letter]["right"]
    
    left_nums = generate_numbers(spec_left["parity"], spec_left["start"], spec_left["end"], spec_left["direction"])
    center_nums = generate_numbers(spec_center["parity"], spec_center["start"], spec_center["end"], spec_center["direction"])
    right_nums = generate_numbers(spec_right["parity"], spec_right["start"], spec_right["end"], spec_right["direction"])
    
    # 2) Place them with alignment
    left_coords   = place_seats_right_aligned(left_nums,   LEFT_BLOCK_ANCHOR_X,   SEAT_SPACING_X)
    center_coords = place_seats_center_aligned(center_nums, CENTER_BLOCK_ANCHOR_X, SEAT_SPACING_X)
    right_coords  = place_seats_left_aligned(right_nums,   RIGHT_BLOCK_ANCHOR_X,  SEAT_SPACING_X)
    
    # 3) Create seat objects
    for seat_num, x_pos in left_coords:
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_letter}{seat_num}",
            "square": True,
            "status": "Available",
            "category": "left-block"
        })
        seat_id += 1
    
    for seat_num, x_pos in center_coords:
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_letter}{seat_num}",
            "square": True,
            "status": "Available",
            "category": "center-block"
        })
        seat_id += 1
    
    for seat_num, x_pos in right_coords:
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_letter}{seat_num}",
            "square": True,
            "status": "Available",
            "category": "right-block"
        })
        seat_id += 1
    
    # 4) Create text objects for row label:
    #    One text between left & center blocks, one between center & right blocks
    #    We'll place them at the row's y, horizontally in the midpoint
    #    For left <-> center, midpoint = (LEFT_BLOCK_ANCHOR_X + CENTER_BLOCK_ANCHOR_X)/2
    #    For center <-> right, midpoint = (CENTER_BLOCK_ANCHOR_X + RIGHT_BLOCK_ANCHOR_X)/2
    mid_left_center = (LEFT_BLOCK_ANCHOR_X + CENTER_BLOCK_ANCHOR_X) / 2 - 100
    mid_center_right = (CENTER_BLOCK_ANCHOR_X + RIGHT_BLOCK_ANCHOR_X) / 2 + 100
    
    text_data.append({
        "id": f"text-{row_letter}-LC",
        "x": mid_left_center,
        "y": y_pos +15 ,
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
        "y": y_pos + 15 ,
        "label": row_letter,
        "fontSize": 20,
        "fontWeight": 400,
        "letterSpacing": 0,
        "color": "#000000",
        "embraceOffset": False,
        "rotation": 0
    })
    
    # 5) If this row is E or Q, add 100 to extra_vertical_offset
    if row_letter == "E" or row_letter == "Q":
        extra_vertical_offset += 100
    if row_letter == "Q":
        extra_vertical_offset += 100
        # After finishing row Q, add text "Trệt" as well or something else?
        # The instructions say "add text 'Trệt' after Q line"? 
        # Or was it after E and Q? 
        # If you want the same label or a different one, adjust:
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
    
        current_row_index += 1

    # 6) After the last row (Y), add text "Lầu"
    # Let's figure out the final row's Y position:
    final_y = BASE_Y + (current_row_index - 1) * ROW_SPACING_Y + extra_vertical_offset
    # The last row was drawn at final_y. We'll place "Lầu" ~50 points below that:
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
# 5) Save to seats.json and text.json
# --------------------------------------------
with open("seats.json", "w") as f:
    json.dump(seat_data, f, indent=4)

with open("texts.json", "w") as f:
    json.dump(text_data, f, indent=4)

print("Done! Generated seats.json for seat data and text.json for text objects.")
