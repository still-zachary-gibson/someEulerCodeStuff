import math
def find_prime(nunba):
    return math.floor((math.factorial(nunba) % (nunba + 1))/nunba) * (nunba-1) + 2


how_many_found = 1
iter = 1
most_recent = 0
while how_many_found < 10001+1:
    if find_prime(iter) != 2:
        most_recent = find_prime(iter)
        print(how_many_found, most_recent)
        how_many_found += 1
    iter += 1

print(most_recent)
