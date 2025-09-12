import math

def the_quad_thing(a,b,n):
    return n**2 + a*n + b

def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

success_count = [0,0,0]

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(abs(the_quad_thing(a,b,n))):
            n += 1
        print(a,b,n)
        if n > success_count[2]:
            success_count = [a,b,n]

print(success_count)
