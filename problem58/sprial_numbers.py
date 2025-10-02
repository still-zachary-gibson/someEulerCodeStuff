#sprial code stuff yay
import math

def is_prime(n): #reused
    if (n < 2 or n % 2 == 0) and n != 2:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

#I need to optimize, and reuse for some time gain.
def generate_sprial(size,clockwise=True):
    global the_spiral
    do_we_have = True
    try:
        test = (the_spiral)
    except:
        do_we_have = False
    if do_we_have: #new code for awesomeness
        #it only works for +2 size increases but i don't care enough currently
        #OH THAT'S SUCH A SPEED INCREASE
        cool_spiral = the_spiral
        for i in cool_spiral:
            i.insert(0,0)
            i.append(0)
        cool_spiral = [[0]*size] + cool_spiral + [[0]*size]
        if clockwise:
            number_to_yeah = cool_spiral[1][size-2]
            current_postion = [1, size-2]
        else:
            number_to_yeah = cool_spiral[size-2][size-2]
            current_postion = [size-2, size-2]
        spooky_numb = 1
    else:
        cool_spiral = []
        for i in range(size):
            cool_spiral.append([0]*size)
        number_to_yeah = 1
        current_postion = [math.floor(size/2), math.floor(size/2)] #y, x
        spooky_numb = math.floor(size/2)
    cur_dir = 0 #0 right, 1 down, 2 left, 3 up
    while number_to_yeah <= size**2:
        cool_spiral[current_postion[0]][current_postion[1]] = number_to_yeah
        number_to_yeah += 1
        look_for = size if cur_dir < 2 else -1 #i didn't notice this was different,,,
        if current_postion[(cur_dir+1)%2] + spooky_numb*(1-(math.floor(cur_dir/2)*2)) == look_for:
            if cur_dir == 1 + clockwise*2:
                spooky_numb -= 1
            cur_dir = (cur_dir+1*((clockwise*2)-1)) % 4
            current_postion[(cur_dir+1)%2] += 1*(1-(math.floor(cur_dir/2)*2))
        else:
            current_postion[(cur_dir+1)%2] += 1*(1-(math.floor(cur_dir/2)*2))
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

def calc_prime_corners(spiral):
    global prime_amount
    size = len(spiral)-1
    exists = True
    try:
        test = prime_amount
    except:
        exists = False
    print("Size:",size)
    if exists:
        #Another speed increase, less to calc
        #oops it breaks the calcs?
        #print(is_prime(spiral[0][0]), spiral[0][0])
        print("Old Prime:",prime_amount)
        #print(spiral[0][0], is_prime(spiral[0][0]))
        #print(spiral[0][size], is_prime(spiral[0][size]))
        #print(spiral[size][0], is_prime(spiral[size][0]))
        #print(spiral[size][size], is_prime(spiral[size][size]))
        if is_prime(spiral[0][0]):
            prime_amount += 1
        if is_prime(spiral[0][size]):
            prime_amount += 1
        if is_prime(spiral[size][0]):
            prime_amount += 1
        if is_prime(spiral[size][size]): #IT WAS 0 size AAARGH
            prime_amount += 1
        print("New Prime:",prime_amount)
    else:
        prime_amount = 0
        print("Old Prime:",prime_amount)
        for y in range(len(spiral)):
            for x in range(len(spiral[y])):
                if x == y:
                    if is_prime(spiral[y][x]):
                        prime_amount += 1
                elif y == size - x:
                    if is_prime(spiral[y][x]):
                        prime_amount += 1
        print("New Prime:",prime_amount)
    return (prime_amount/((size+1)*2-1)) # 7 gives 8 / 13, so right on

prime_percent = 1
size = 1

while prime_percent*100 >= 10:
    size += 2

    the_spiral = generate_sprial(size, False)

    #print(the_spiral)

    prime_percent = (calc_prime_corners(the_spiral))

    if size > 300:
        print("STOOPP")

    #print(size, prime_percent*100)

print(size)