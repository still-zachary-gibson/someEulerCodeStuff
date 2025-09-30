#okay firstly, i need to GRAB all of the primes.

import math


def is_prime(n):
    if (n < 2 or n % 2 == 0) and n != 2:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

#luckily, I don't actually need any below 10 digits!
#crap this is massive isn't it. Maybe I just go as I check for em, no need to do ELEVEN run throughs.

most_amount_of = []
list_of_most = []
for j in range(10):
    most_amount_of.append(0)
    list_of_most.append([])

#most of tracks the most of the digit to appear so far

for i in range(10**9, 10**10):
    if is_prime(i):
        prime_str = str(i)
        for j in range(10):
            count_of = prime_str.count(str(j))
            if count_of > most_amount_of[j]:
                most_amount_of[j] = count_of
                if len(list_of_most[j]) > 0:
                    list_of_most[j] = []
            if count_of == most_amount_of[j] and most_amount_of[j] != 0:
                list_of_most[j].append(i)
        #print(list_of_most)

#seems like it works but i should make sure it has something to do before wasting time that might be better spent actually doing

sum = 0

for i in range(10):
    temp_sum = 0
    for j in range(len(list_of_most[i])):
        temp_sum += j
    sum += temp_sum

print(sum)
