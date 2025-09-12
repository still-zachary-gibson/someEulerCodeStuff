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

'''
erm1 = [
 1929961,
 0936492, 0993394,
 0447647, 0488750, 0504580, 
 0211339, 0236291, 0252412, 0252086, 
 0099255, 0112066, 0124190, 0128135, 0123941, 
 0046976, 0052259, 0059803, 0064305, 0063783, 0060093,
 0022804, 0024153, 0028105, 0031675, 0032555, 0031225, 28834, 
 0011421, 0011295, 0012856, 0015172, 0016430, 0016118, 15044, 13723, 
 0005921, 0005401, 0005829, 0007023, 0008121, 0008303, 7799, 7175, 6456, 
 0003188, 0002692, 0002668, 0003135, 0003832, 0004206, 4057, 3662, 3443, 2980,
 0001731, 0001416, 0001228, 0001368, 0001734, 0002051, 2123, 1897, 1749, 1600, 1351,
 0000942, 0000736, 0000609, 0000575, 0000728, 0000981, 1027, 1005, 840, 812, 737, 600,
 0000446, 0000426, 0000299, 0000277, 0000270, 0000381, 527, 483, 444, 357, 387, 333, 210,
 0000129, 0000226, 0000129, 0000118, 0000121, 0000132, 235, 201, 239, 147, 160, 200, 104, 58,
 0000004, 0000062, 0000098, 0000027, 0000023, 0000009, 70, 98, 73, 93, 38, 53, 60, 4, 23,

'''

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
tri_vals = []
for i in erm:
    tri_vals.append(0)

def get_child_value(y, x):
    my_value = erm[triangle_to_index(y,x)]
    #print(my_value, y, x)
    if triangle_to_index(y+1,x) < len(erm):
        val1 = tri_vals[triangle_to_index(y+1,x)]
        val2 = tri_vals[triangle_to_index(y+1,x+1)]
        my_value += val1 if val1 > val2 else val2 
    #print(my_value, y, x)
    return my_value

for y in reversed(range(15)):
    for x in range(y+1):
        tri_vals[triangle_to_index(y,x)] = get_child_value(y,x)

#print(tri_vals)

current_amount += erm[triangle_to_index(current_pos[0], current_pos[1])]
while current_pos[0] < 14:
    print(current_pos)
    left = tri_vals[triangle_to_index(current_pos[0]+1,current_pos[1])]
    right = tri_vals[triangle_to_index(current_pos[0]+1,current_pos[1]+1)]
    current_pos[0] += 1
    if left < right:
        current_pos[1] += 1
    current_amount += erm[triangle_to_index(current_pos[0], current_pos[1])]

print(current_amount)