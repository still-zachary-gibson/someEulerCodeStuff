import math
from concurrent.futures import ThreadPoolExecutor

def check_values(x,y,z):
    print(x,y,z, flush=True)
    try:
        if int(math.sqrt(x+y)) != math.sqrt(x+y):
            raise Exception
        if int(math.sqrt(x-y)) != math.sqrt(x-y):
            raise Exception
        if int(math.sqrt(x+z)) != math.sqrt(x+z):
            raise Exception
        if int(math.sqrt(x-z)) != math.sqrt(x-z):
            raise Exception
        if int(math.sqrt(y+z)) != math.sqrt(y+z):
            raise Exception
        if int(math.sqrt(y-z)) != math.sqrt(y-z):
            raise Exception
    except:
        return False
    else:
        return True, x, y, z

x = 3
y = 2
z = 1

tru_x = -1
tru_y = -1
tru_z = -1

done = False

def sure(what):
    global done
    global tru_x
    global tru_y
    global tru_z
    if what.result() != False and tru_x == -1:
        done = True
        tru_x = what.result()[1]
        tru_y = what.result()[2]
        tru_z = what.result()[3]

with ThreadPoolExecutor() as executor:
    while not done:
        future = executor.submit(check_values, x, y, z)
        future.add_done_callback(sure)
        z += 1
        if z == y:
            z = 1
            y += 1
            if y == x:
                y = 2
                x += 1

print(tru_x,tru_y,tru_z)
