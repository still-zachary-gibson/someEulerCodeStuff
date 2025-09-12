#NO multipl of 2
#no multiple of 3
#no multiple of 5

primes = []
iter = 2
max = 2000000
while iter < max:
    is_prime = True
    for prime in primes:
        if iter % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(iter)
    if iter == 2:
        iter += 1
    else:
        iter += 2

print(primes)
