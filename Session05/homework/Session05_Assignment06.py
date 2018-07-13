sokoban = {
    "size_x": 6,
    "size_y": 6,
}

player = { "x": 2, "y": 2} 

boxes = [
    { "x": 1, "y": 3},
    { "x": 2, "y": 3},
    { "x": 3, "y": 3},
    { "x": 4, "y": 3},
]
destination = [
    { "x": 1, "y": 4},
    { "x": 2, "y": 5},
    { "x": 1, "y": 6},
    { "x": 4, "y": 6},
]
# obstacle = [
#     { "x": 2, "y": 4},
#     { "x": 5, "y": 5},
# ]

playing = True

while playing:
    for y in range (1, sokoban['size_y']+1):  
        for x in range (1, sokoban['size_x']+1):
            box_is_here = False
            des_is_here = False
            # obs_is_here = False
            for box in boxes:
                if x == box['x'] and y == box['y']:
                    box_is_here = True
            for des in destination:
                if x == des['x'] and y == des['y']:
                    des_is_here = True
            # for obs in obstacle:
            #     if x == obs['x'] and y == obs['y']:
            #         obs_is_here = True  
            if x == player['x'] and y == player['y']:
                print("P ", end = "")
            elif box_is_here:
                print ("B ", end = "")
            elif des_is_here:
                print ("D ", end = "")
            # elif obs_is_here:
            #     print ("O ", end = "")
            else:
                print ("- ", end = "")
        print ()

#check win:
    win = True
    for box in boxes:
        if box not in destination:
            win = False
    if win:
        print("You win")
        break
        
# Move player
    move = input("Your move: ").upper()

    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        print ("Buzzzz")
        playing = False

# Di chuyen player
    # move_player = False
    # move_box = False
    if 1 <= player['x'] + dx <= sokoban['size_x'] and 1 <= player['y'] + dy <= sokoban['size_y']:
        player['x'] += dx
        player['y'] += dy
        # move_player = True
    else:
        print("Can't move >_<")

    
    for box in boxes:
        if box['x'] == player['x'] + dx and box['y'] == player['y'] + dy:
        # and 1 <= box['x'] + dx <= sokoban['size_x'] and 1 <= box['y'] + dy <= sokoban['size_y']:
            box['x'] += dx
            box['y'] += dy
            # move_box = True

    # # Di chuyen
    # if move_player:
    #     player['x'] += dx
    #     player['y'] += dy

    # if move_box:
    #     box['x'] += dx
    #     box['y'] += dy

