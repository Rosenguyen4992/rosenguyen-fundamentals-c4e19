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
obstacle = [
    { "x": 2, "y": 4},
    { "x": 5, "y": 5},
]

playing = True
while playing:
    for y in range (sokoban['size_y']):  
        for x in range (sokoban['size_x']):
            box_is_here = False
            des_is_here = False
            obs_is_here = False
            for box in boxes:
                if x == box['x'] and y == box['y']:
                    box_is_here = True
            for des in destination:
                if x == des['x'] and y == des['y']:
                    des_is_here = True
            for obs in obstacle:
                if x == obs['x'] and y == obs['y']:
                    obs_is_here = True  
            if x == player['x'] and y == player['y']:
                print("P ", end = "")
            elif box_is_here:
                print ("B ", end = "")
            elif des_is_here:
                print ("D ", end = "")
            elif obs_is_here:
                print ("O ", end = "")
            else:
                print ("- ", end = "")
        print ()

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

    if 0 <= player['x'] + dx < sokoban['size_x'] and 0 <= player['y'] + dy < sokoban['size_y']:
        player['x'] += dx
        player['y'] += dy
    else:
        print("Ouch!")
    
    for box in boxes:
        if player['x'] == box['x'] and player['y'] == box['y']:
            box['x'] += dx
            box['y'] += dy