import math

def factors(n):
    list_o_lower_factors = []
    list_o_upper_factors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            list_o_lower_factors.append(i)
            result = int(n / i)
            if result != i and not result in list_o_upper_factors:
                list_o_upper_factors.append(result)
    list_o_upper_factors.reverse()
    total_list = list_o_lower_factors + list_o_upper_factors
    return total_list

solu_numb = 0
n = 4

while solu_numb < 1000:
    n += 1
    solu_numb = 0
    #factor = factors(n) #okay this just works
    #so i've got a thing where i know that this just... works
    #for thing in factor:
    #    side_1 = n + n//thing
    #    side_2 = side_1 * thing
    #
    #    print(side_1, side_2)
    solu_numb = len(factors(n))

print(n)
