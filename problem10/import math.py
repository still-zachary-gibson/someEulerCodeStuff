import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def Adds(max):
    total = 0
    for i in range(2,max):
        print(i, is_prime(i))
        if is_prime(i):
            total += i
    return total

print(Adds(20))