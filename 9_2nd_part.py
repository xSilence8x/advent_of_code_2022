with open("data/9.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

coord_t = [[0, 0] for x in range(10)] # 9 resting knots in total

coord_move = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
} 

list_coord_h = []
list_coord_t = [coord_t[-1]]

for x in data:
    direction, moves = x.split(" ") # R 4
    moves = int(moves)
    for y in range(moves): # 0 1 2 3 (4x)
        coord_t[0] = [x + y for x, y in zip(coord_move[direction], coord_t[0])]
        list_coord_h.append(coord_t[0])
        for i in range(1, 10):
            coord_t[i-1] = [coord_t[i-1][0], coord_t[i-1][1]]
            coord_t[i] = [coord_t[i][0], coord_t[i][1]]
            if abs(coord_t[i-1][0] - coord_t[i][0]) > 1 or abs(coord_t[i-1][1] - coord_t[i][1]) > 1:
                tx_move = 0 if coord_t[i-1][0] == coord_t[i][0] else (coord_t[i-1][0] - coord_t[i][0]) / abs(coord_t[i-1][0] - coord_t[i][0])
                ty_move = 0 if coord_t[i-1][1] == coord_t[i][1] else (coord_t[i-1][1] - coord_t[i][1]) / abs(coord_t[i-1][1] - coord_t[i][1])
                coord_t[i] =  [coord_t[i][0] + int(tx_move), coord_t[i][1] + int(ty_move)]
        if coord_t[-1] not in list_coord_t:
            list_coord_t.append(coord_t[-1])
element_count_t = len(list_coord_t)
print(f"Tail visited at least once: {element_count_t}")

