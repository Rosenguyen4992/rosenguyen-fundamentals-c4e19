map_sokoban = {
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


playing = True
while playing:
    ########## print map

    for y in range(1, map_sokoban["size_y"]+1):
        for x in range(1, map_sokoban["size_x"]+1):

            box_is_here = False
            for box in boxes:
                if box["x"] == x and box['y'] == y:
                    box_is_here = True

            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True

            des_is_here = False
            for des in destination:
                if des["x"] == x and des["y"] == y:
                    des_is_here = True
            if player_is_here:
                print("P ",end='')
            elif box_is_here:            
                print("B ",end='')
            elif des_is_here:
                print("D ",end='')
            else:
                print("- ",end='')
        print()


    #check win:
    win = True
    for box in boxes:
        if box not in destination:
            win = False
    if win:
        print("You win")
        break

    dx = 0
    dy = 0
    move = input("ur move: ").lower()
    if move == "w":
        dy = -1
    elif move == "s":
        dy = 1
    elif move == "a":
        dx = -1
    elif move == "d":
        dx = 1
    else:
        playing = False
    if 0 <= player['x'] + dx < map_sokoban['size_x'] \
    and 0 <= player['y'] + dy < map_sokoban['size_y']:
        player['x'] += dx
        player['y'] += dy

    for box in boxes:
        if box['x'] == player["x"] and box['y'] == player['y']:
            box['x'] += dx
            box['y'] += dy

    
