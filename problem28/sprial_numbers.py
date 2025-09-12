#sprial code stuff yay
import math
def generate_sprial(size):
    cool_spiral = []
    for i in range(size):
        funby_temp_thing = []
        for j in range(size):
            funby_temp_thing.append(0)
        cool_spiral.append(funby_temp_thing) #now we have all of the spaces
    number_to_yeah = 1
    current_postion = [math.floor(size/2), math.floor(size/2)] #y, x
    spooky_numb = math.floor(size/2)
    cur_dir = 0 #0 right, 1 down, 2 left, 3 up
    while number_to_yeah <= size**2:
        cool_spiral[current_postion[0]][current_postion[1]] = number_to_yeah
        number_to_yeah += 1
        if cur_dir == 0:
            if current_postion[1] + spooky_numb == size:
                cur_dir = 1
                current_postion[0] += 1
            else:
                current_postion[1] += 1
        elif cur_dir == 1:
            if current_postion[0] + spooky_numb == size:
                cur_dir = 2
                current_postion[1] -= 1
            else:
                current_postion[0] += 1
        elif cur_dir == 2:
            if current_postion[1] - spooky_numb == -1:
                cur_dir = 3
                current_postion[0] -= 1
            else:
                current_postion[1] -= 1
        elif cur_dir == 3:
            if current_postion[0] - spooky_numb == -1:
                cur_dir = 0
                spooky_numb -= 1
                current_postion[1] += 1
            else:
                current_postion[0] -= 1
    return cool_spiral

def calc_corners(spiral):
    size = len(spiral)-1
    sum = 0
    for y in range(len(spiral)):
        for x in range(len(spiral[y])):
            if x == y:
                sum += spiral[y][x]
            elif y == size - x:
                sum += spiral[y][x]
    return sum
    


the_spiral = generate_sprial(int(input("Dimensions: ")))

print(calc_corners(the_spiral))
