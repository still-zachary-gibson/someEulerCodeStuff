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

numbers_to_not_use = []

print("Done abunding")

for i in range(len(abundent_list)):
    print(i)
    for j in range(i, len(abundent_list)):
        sum = abundent_list[i] + abundent_list[j]
        #print(abundent_list[i], abundent_list[j], sum)
        if sum > 28123:
            #print("too high movin on")
            break
        elif sum in numbers_to_not_use:
            #print("already there")
            continue
        else:
            #print("added")
            numbers_to_not_use.append(sum)

sum_ugh = 0

print("Done adding")

for i in range(1,28123+1):
    if not i in numbers_to_not_use:
        sum_ugh += i

print(sum_ugh)