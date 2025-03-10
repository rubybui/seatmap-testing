import json

# -----------------------
# Center Configuration
# -----------------------
center_rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
row_spacing_center = 40
seat_spacing_center = 40
base_y_center = 200
left_base_x_center = 480
right_base_x_center = 570
center_category = "6267c38d-e1ee-433a-9bda-8be0cab0b062"

row_seat_ranges_center = {
    "A": (23, 22),
    "B": (23, 22),
    "C": (23, 22),
    "D": (23, 22),
    "E": (23, 22),
    "F": (19, 18),
    "G": (21, 20),
    "H": (17, 16),
    "I": (17, 16),
    "J": (13, 14),
    "K": (13, 14)
}

# -----------------------
# Determine the leftmost and rightmost seat X in the center
# so we can place the side lines further out.
# -----------------------
# We'll compute them by simulating the extremes in the center block.

# Leftmost seat occurs in a row with the largest odd_max (like 23).
# For seat_num=23 => offset=(23-1)//2=11 => x=500-(11*40)=500-440=60
# That means the leftmost seat in the center is around x=60 (for rows with odd_max=23).

# Rightmost seat occurs in a row with the largest even_max (like 22).
# For seat_num=22 => offset=(22-2)//2=10 => x=550+(10*40)=550+400=950
# That means the rightmost seat in the center is around x=950 (for rows with even_max=22).

leftmost_center_x = 60
rightmost_center_x = 950

# -----------------------
# Left side lines
# -----------------------
# We'll start them further left than x=60, say x=0 or 20. 
# We'll keep them somewhat close to each other by adjusting start_y values.
# We'll angle them top-left to bottom-right => step_x > 0, step_y > 0.

left_side_lines = [
    {
        "label": "M",
        "seat_count": 15,
        "start_x": -200,   # further left than x=60
        "start_y": 120,
        "step_x": 20,    # move right each seat
        "step_y": 30
    },
    {
        "label": "Q",
        "seat_count": 16,
        "start_x": -200,   # same X start so lines are close
        "start_y": 240,  # slightly lower
        "step_x": 20,
        "step_y": 30
    },
    {
        "label": "R",
        "seat_count": 16,
        "start_x": -200,
        "start_y": 360,
        "step_x": 20,
        "step_y": 30
    },
]

# -----------------------
# Right side lines
# -----------------------
# We'll start them further right than x=950, say x=1000.
# We'll angle them top-right to bottom-left => step_x < 0, step_y > 0.

right_side_lines = [
    {
        "label": "N",
        "seat_count": 15,
        "start_x": 1200,  # further right than x=950
        "start_y": 120,
        "step_x": -20,    # move left each seat
        "step_y": 30
    },
    {
        "label": "P",
        "seat_count": 16,
        "start_x": 1200,
        "start_y": 240,
        "step_x": -20,
        "step_y": 30
    },
    {
        "label": "T",
        "seat_count": 16,
        "start_x": 1200,
        "start_y": 360,
        "step_x": -20,
        "step_y": 30
    },
]

side_category = "6267c38d-e1ee-433a-9bda-8be0cab0b062"


# -----------------------
# 3) BACK ROWS (L, O, S) SPLIT INTO BLOCKS OF 4 - 6 - 4
# -----------------------
# Each row has 14 seats total: L1..L14, O1..O14, S1..S14.
# We'll place them behind the center (below row K).
# You can tweak these X positions to space out each block differently.

back_rows = ["L", "O", "S"]
back_row_spacing = 40  # same vertical spacing
base_y_back = 200 + len(center_rows) * row_spacing_center + 40  
# The above starts them one row below K; tweak as you wish

# We'll define the X positions for the 3 blocks:
#  - 4 seats in the left block
#  - 6 seats in the middle block
#  - 4 seats in the right block
# For example:
# left block seats: x= 400, 440, 480, 520
# center block seats: x= 600, 640, 680, 720, 760, 800
# right block seats: x= 880, 920, 960, 1000
back_left_x = [248, 288, 328, 368]
back_center_x = [428, 468, 508, 548, 588, 628]
back_right_x = [688, 728, 768, 808]


back_category = "fe1a1eb0-1f30-4014-ae49-ee8438b720a3"


# -----------------------
# Generate all seats
# -----------------------
seat_data = []
seat_id = 1

# 1) Generate center seats (A–K)
for row_index, row_label in enumerate(center_rows):
    y_pos = base_y_center + row_index * row_spacing_center
    odd_max, even_max = row_seat_ranges_center[row_label]
    
    # Left side (odd seats)
    for seat_num in range(1, odd_max + 1, 2):
        offset = (seat_num - 1) // 2
        x_pos = left_base_x_center - offset * seat_spacing_center
        
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_label}{seat_num}",
            "square": True,
            "status": "Available",
            "category": center_category
        })
        seat_id += 1

    # Right side (even seats)
    for seat_num in range(2, even_max + 1, 2):
        offset = (seat_num - 2) // 2
        x_pos = right_base_x_center + offset * seat_spacing_center
        
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_pos,
            "y": y_pos,
            "label": f"{row_label}{seat_num}",
            "square": True,
            "status": "Available",
            "category": center_category
        })
        seat_id += 1

# 2) Generate left side lines (M, Q, R)
for line in left_side_lines:
    label = line["label"]
    seat_count = line["seat_count"]
    start_x = line["start_x"]
    start_y = line["start_y"]
    step_x = line["step_x"]
    step_y = line["step_y"] 
    
    for i in range(1, seat_count + 1):
        seat_index = i - 1
        x_pos = start_x + seat_index * step_x 
        y_pos = start_y + seat_index * step_y
        
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_pos,
            "y": y_pos,
            "label": f"{label}{i}",
            "square": True,
            "status": "Available",
            "category": side_category
        })
        seat_id += 1

# 3) Generate right side lines (N, P, T)
for line in right_side_lines:
    label = line["label"]
    seat_count = line["seat_count"]
    start_x = line["start_x"]
    start_y = line["start_y"]
    step_x = line["step_x"] 
    step_y = line["step_y"] 
    
    for i in range(1, seat_count + 1):
        seat_index = i - 1
        x_pos = start_x + seat_index * step_x 
        y_pos = start_y + seat_index * step_y
        
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_pos,
            "y": y_pos,
            "label": f"{label}{i}",
            "square": True,
            "status": "Available",
            "category": side_category
        })
        seat_id += 1


# 3) Generate back rows (L, O, S) in 3 blocks of 4-6-4 seats
for i, row_label in enumerate(back_rows):
    # y position for each row
    y_pos = base_y_back + i * back_row_spacing
    
    # left block (4 seats => 1..4)
    for idx, x_val in enumerate(back_left_x, start=1):
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_val,
            "y": y_pos,
            "label": f"{row_label}{idx}",  # L1..L4, O1..O4, S1..S4
            "square": True,
            "status": "Available",
            "category": back_category
        })
        seat_id += 1
    
    # center block (6 seats => 5..10)
    for idx, x_val in enumerate(back_center_x, start=5):
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_val,
            "y": y_pos,
            "label": f"{row_label}{idx}",  # L5..L10, O5..O10, S5..S10
            "square": True,
            "status": "Available",
            "category": back_category
        })
        seat_id += 1
        # right block (4 seats => labels rowX11..rowX14)
    for idx, x_val in enumerate(back_right_x, start=11):
        seat_data.append({
            "id": f"seat-{seat_id}",
            "x": x_val,
            "y": y_pos,
            "label": f"{row_label}{idx}",
            "square": True,
            "status": "Available",
            "category": back_category
        })
        seat_id += 1


# -----------------------
# Save to seats.json
# -----------------------
seat_json = json.dumps(seat_data, indent=4)
with open("seats.json", "w") as f:
    f.write(seat_json)

print("seats.json created with side lines closer together, starting further from the center block.")
