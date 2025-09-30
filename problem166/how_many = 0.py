how_many = 0

grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,-1]
]

def index_to_grid(index):
    return grid[index//4][index%4]
    #return index // 4, index % 4

def add_to_grid(index):
    grid[index//4][index%4] += 1
    if grid[index//4][index%4] == 10:
        grid[index//4][index%4] = 0
        return True
    return False

while grid[0][0] < 10:
    position = 15
    while position >= 0:
        if add_to_grid(position):
            position -= 1
        else:
            break
    #y_pos, x_pos = index_to_grid(position)
    failure = False
    sum_to_aim = -1
    for y in range(4):
        temp = 0
        for x in range(4):
            temp += grid[y][x]
        if sum_to_aim == -1:
            sum_to_aim = temp
        elif sum_to_aim != temp:
            failure = True
            break
    if failure:
        continue
    for x in range(4):
        temp = 0
        for y in range(4):
            temp += grid[y][x]
        if sum_to_aim != temp:
            failure = True
            break
    if failure:
        continue
    temp = 0
    for xy in range(4):
        temp += grid[xy][xy]
    if sum_to_aim != temp:
        break
    temp = 0
    for xy in range(4):
        temp += grid[3-xy][xy]
    if sum_to_aim != temp:
        break
    print(grid)
    how_many += 1

print(how_many)
