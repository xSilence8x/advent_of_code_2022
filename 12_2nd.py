from collections import namedtuple, deque

with open("12_test.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

point = namedtuple("point", "x y")

grid = [list(line) for line in data]


for i in range(len(grid)): # my rows
    for j in range(len(grid[0])): # my columns
        element = grid[i][j]
        if element == "E":
            grid[i][j] = ord("z")
            start = point(i, j)
        elif element == "S":
            grid[i][j] = ord("a")
            
        else:
            grid[i][j] = ord(element)

def get_neighbours(p: point):
    return [
        point(p.x + offset[0], p.y + offset[1])
        for offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ]

def find_path(grid, start):
    
    buffer = deque([(start, 0)])
    
    visited = set()
    while buffer:
        current = buffer.popleft()
        a = current[0][0]
        b = current[0][1]
        check_letter = grid[a][b]
        if current[0] in visited:
            continue
        if check_letter == ord("a"):
            return current[1]
        visited.add(current[0])
        
        for n in get_neighbours(current[0]):
            
            if n.x < 0 or n.y < 0 or n.x >= len(grid) or n.y >= len(grid[0]):
                continue
            if grid[n.x][n.y] >= grid[current[0].x][current[0].y] - 1:
                buffer.append((n, current[1]-1))
                
        
print(abs(find_path(grid, start)))