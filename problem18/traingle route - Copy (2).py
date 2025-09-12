erm = [       75,
             95,64,
            17,47,82,
           18,35,87,10,
          20, 4,82,47,65,
         19, 1,23,75, 3,34,
        88, 2,77,73, 7,63,67,
       99,65, 4,28, 6,16,70,92,
      41,41,26,56,83,40,80,70,33,
     41,48,72,33,47,32,37,16,94,29,
    53,71,44,65,25,43,91,52,97,51,14,
   70,11,33,28,77,73,17,78,39,68,17,57,
  91,71,52,38,17,14,91,43,58,50,27,29,48,
 63,66, 4,68,89,53,67,30,73,16,69,87,40,31,
 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23] #14

def triangle_to_index(y, x):
    index = 0
    if x > y:
        x = y
    while y > 0:
        index += y
        y -= 1
    index += x
    return index

current_pos = [0,0]
current_amount = 0

def try_route(temp_pos):
    our_value = erm[triangle_to_index(temp_pos[0], temp_pos[1])]
    while temp_pos[0] < 14:
        val1 = try_route([temp_pos[0]+1,temp_pos[1]])
        val2 = try_route([temp_pos[0]+1,temp_pos[1]+1])
        temp_pos[0]+=1
        if val1 < val2:
            temp_pos[1]+=1
        our_value += erm[triangle_to_index(temp_pos[0], temp_pos[1])]
    return our_value

'''while current_pos[0] < 14:
    current_amount += erm[triangle_to_index(current_pos[0], current_pos[1])]
    value1 = triangle_to_index(current_pos[0]+1, current_pos[1])
    value2 = triangle_to_index(current_pos[0]+1, current_pos[1]+1)
    current_pos[0] += 1
    if erm[value1] < erm[value2]:
        current_pos[1] += 1
'''
print(try_route([0,0]))
'''
        
current_amount += erm[triangle_to_index(current_pos[0], current_pos[1])]
print(current_pos, current_amount)
'''