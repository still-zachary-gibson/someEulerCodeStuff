import math

def is_prime(n): #reused
    if (n < 2 or n % 2 == 0):
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

prime_amount = 0
side = -1
size = 1
cur_numb = 1
step = 1

prime_percent = 1

while prime_percent >= 0.1:
    lower = 1 if side == 0 else 0
    if is_prime(cur_numb-lower):
        prime_amount+=1
    if side == 0 and prime_amount > 0:
        size += 2
        prime_percent = prime_amount/((size+1)*2-1)
        print(size, prime_percent)
    cur_numb += step
    if side % 2 == 0 and side >= 0:
        step += 1
    side = (side+1) % 4

print(size)