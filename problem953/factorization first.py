#okay lets start with  factorization

#god damn it first i need to get the primes

prime_list = []
max_prime = 0

#heaps_baby = [0,1]

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
    if numba == 1:
        return [1]
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
'''
iter = 2
while iter < 80:
    heaps_baby.append(factorization(iter))
    iter += 1
'''

#print(factorization(70))

def willOneWin(the_heaps):
    if(the_heaps == [1]):
        return False
    amazing_number = the_heaps[0]
    for i in range(1, len(the_heaps)):
        amazing_number = amazing_number^the_heaps[i]
    if amazing_number == 0:
        return False
    else:
        return True

loss_amount = 0
max_numb = 10**14

for i in range(1,max_numb+1):
    #print(factorization(i))
    if not willOneWin(factorization(i)):
        #print(i/max_numb)
        loss_amount += i

print(loss_amount % (10**9+7))