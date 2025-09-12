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

prime_amount = 0 
iter = 0

while prime_amount < 10001:
    if is_prime(iter):
        prime_amount += 1
    if prime_amount < 10001:
        iter += 1

print(iter)