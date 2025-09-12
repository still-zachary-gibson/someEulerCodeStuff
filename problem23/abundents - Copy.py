# first get some abundents
import math

def get_numb_factors(numb):
    factor_list = []
    for i in range(1, math.floor(numb/2)+1):
        if numb % i == 0:
            factor_list.append(i)
    return factor_list

def is_abundent(numb):
    factors = get_numb_factors(numb)
    test_sum = 0
    for i in factors:
        test_sum += i
    if test_sum > numb:
        return True
    return False

abundent_list = []
for i in range(1,28123+1):
    #print(i, is_abundent(i))
    if is_abundent(i):
        abundent_list.append(i)

print(len(abundent_list))
