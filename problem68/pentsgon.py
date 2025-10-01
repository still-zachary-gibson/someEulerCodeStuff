#okay i need to visualize how the HECK i do this uh,
#first i should probably actually have things to like. construct this.

#drew out an index diagram

import math

from copy import deepcopy

number_list = list(range(1,11))
amazing_lists = []
numbers = []
rings = [[]]
for i in range(5):
    rings[0].append([0,0,0])
'''def base_vals():
    rings = []
    for i in range(5):
        rings.append([0,0,0])
    return rings
'''

def modify_ring(index, new_val):
    global current_index
    temp_ring = deepcopy(rings[len(rings)-1])
    if index == 0:
        temp_ring[0][0] = new_val
    elif index == 1:
        temp_ring[0][1] = new_val
        temp_ring[4][2] = new_val
    elif index % 2 == 0:
        temp_ring[math.floor(index/2)-1][2] = new_val
        temp_ring[math.floor(index/2)][1] = new_val
    elif index % 2 == 1:
        temp_ring[math.floor(index/2)][0] = new_val
    rings.append(temp_ring)
    current_index += 1

def current_ring():
    if len(rings) > 0:
        return rings[len(rings)-1]
    else:
        return deepcopy(rings)

def take_out_number(numba):
    #print(amazing_lists)
    if len(amazing_lists) > 0:
        temp_list = deepcopy(amazing_lists[len(amazing_lists)-1])
    else:
        temp_list = deepcopy(number_list)

    #print("3:", temp_list)

    temp_list.pop(temp_list.index(numba))

    amazing_lists.append(temp_list)

    #return numba

def get_current_thing():
    if len(amazing_lists) > 0:
        return amazing_lists[len(amazing_lists)-1]
    else:
        return deepcopy(number_list)

#rings = base_vals()

def go_up_layer():
    global current_index
    things[current_index] = 0
    #amazing_lists.pop()
    #rings.pop()
    current_index -= 1

'''for i in range(10):
    modify_ring(i, i)

#cool it works

print(rings)
'''

things = [0]*10

current_index = 0

#okay go through all the first one optionsd,,,

#Oh god. ugh... I gotta be able to go up to look through all the options,,,
#and then go back,,,,

things[0] = 1

sixteen_ones = []

def check_if_magic():
    global sixteen_ones
    cur_ring = current_ring()
    sum_to_check = sum(cur_ring[0])
    magic = True
    for i in cur_ring:
        if sum(i) != sum_to_check:
            magic = False
            break
    #print(cur_ring, magic)
    if magic:
        print(cur_ring)
        starting_point = math.inf
        for i in range(len(cur_ring)):
            if cur_ring[i][0] < starting_point:
                starting_point = i
        i = starting_point
        temp_str = ""
        while True:
            for j in cur_ring[i]:
                temp_str += str(j)
            i = (i+1) % len(cur_ring)
            if i == starting_point:
                break
        if len(temp_str) == 16:
            sixteen_ones.append(temp_str)

def run_loop():
    global current_index
    while things[current_index] <= 10:
        if current_index > 0:
            if things[current_index] in things[:current_index]:
                things[current_index] += 1
                continue
        #print("1:", things)
        take_out_number(things[current_index])

        modify_ring(current_index, things[current_index])

        #print(current_ring())

        wasteNoTime = False #having it true broke things.

        if wasteNoTime:
            if current_index % 3 == 2 and current_index > 3:
                #print(current_ring())
                if sum(current_ring()[0]) != sum(current_ring()[math.floor(current_index/3)]):
                    amazing_lists.pop()
                    rings.pop()
                    go_up_layer()
                    things[current_index] += 1
                    continue

        #print(current_index)
        if current_index == 10:
            check_if_magic()
            #print(current_ring())
            current_index -= 1
        else:
            if len(get_current_thing()) > 0:
                things[current_index] = get_current_thing()[0]

                run_loop()

        #print(current_ring())

        things[current_index] += 1
        amazing_lists.pop()
        rings.pop()
    #print(things)
    go_up_layer()

run_loop()

max = 0

for all in sixteen_ones:
    if int(all) > max:
        max = int(all)

print(max)

'''
while things[0] <= 10:

    take_out_number(things[0])

    modify_ring(0, things[0])

    things[1] = get_current_thing()[0]
    while things[1] <= 10:
        if things[1] == things[0]:
            things[1] += 1
            continue
        take_out_number(things[1])
        modify_ring(1, things[1])

        print(current_ring())

        go_up_layer()

        things[1] += 1

    go_up_layer()

    print(rings)
    
    things[0] += 1
'''
