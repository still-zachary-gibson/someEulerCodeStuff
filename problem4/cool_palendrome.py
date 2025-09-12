my_pals = []
highest = 0

import math

for i in range(100,1000):
    for j in range(i, 1000):
        cool_product = i * j
        cool_string = list(str(cool_product))
        is_pal = True
        for k in range(math.ceil(len(cool_string)/2)):
            if cool_string[k] != cool_string[len(cool_string)-1-k]:
                is_pal = False
                break
        if is_pal:
            if cool_product > highest:
                highest = cool_product
                my_pals.append(cool_product)

print(my_pals)
