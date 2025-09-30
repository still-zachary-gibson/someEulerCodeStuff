import math

#this feels like a terrible idea but im unsure of how else

how_many = 0
save_calc_time = 10**12

for z in range(0,2000+1):
    print(z)
    for x in range(z,2000+1-z):
        y = 2000-x-z
        #print(x, y, z)
        #print(x + y + z)
        coefficent = math.factorial(x+y+z)//(math.factorial(x)+math.factorial(y)+math.factorial(z))
        if (coefficent % save_calc_time) == 0:
            how_many += 1

print(how_many)
