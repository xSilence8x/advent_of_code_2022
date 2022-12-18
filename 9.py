with open("data/9.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

coord_h = [0, 0] # starting location of H
coord_t = [0, 0]

coord_move = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
} 

list_coord_h = []
list_coord_t = [coord_t]

for x in data:
    direction, moves = x.split(" ") # R 4
    moves = int(moves)

    for y in range(moves): # 0 1 2 3 (4x)
        coord_h = [x + y for x, y in zip(coord_move[direction], coord_h)]
        list_coord_h.append(coord_h)
        print("list coord h", coord_h)
        if abs(coord_h[0] - coord_t[0]) > 1 or abs(coord_h[1] - coord_t[1]) > 1:
            tx_move = 0 if coord_h[0] == coord_t[0] else (coord_h[0] - coord_t[0]) / abs(coord_h[0] - coord_t[0])
            ty_move = 0 if coord_h[1] == coord_t[1] else (coord_h[1] - coord_t[1]) / abs(coord_h[1] - coord_t[1])
            coord_t =  [coord_t[0] + int(tx_move), coord_t[1] + int(ty_move)]
            if coord_t not in list_coord_t:
                list_coord_t.append(coord_t)
        print("coord t", coord_t)

element_count_t = len(list_coord_t)
print(f"Tail visited at least once: {element_count_t}")

