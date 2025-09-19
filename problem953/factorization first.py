#okay lets start with  factorization

#god damn it first i need to get the primes

prime_list = []
max_prime = 0

import math

def is_prime(n):
    if (n < 2 or n % 2 == 0) and n != 2:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    global prime_list
    global max_prime

    prime_list.append(n)
    max_prime = n

    return True

def factorization(numba):
    if(numba > max_prime):
        temp_length = len(prime_list)
        iter = max_prime+1
        while len(prime_list)-2 < temp_length:
            is_prime(iter)
            iter += 1
        #print(prime_list)
    return_ma = []
    number = numba
    iter = 0
    while iter < len(prime_list):
        if(number % prime_list[iter] == 0):
            number /= prime_list[iter]
            return_ma.append(prime_list[iter])
        else:
            iter += 1
            if(number == 1):
                break
    return return_ma
    #return a list?

iter = 2
while iter < 20:
    print(factorization(iter))
    iter += 1
