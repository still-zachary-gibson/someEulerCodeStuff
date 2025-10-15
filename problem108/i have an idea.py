import math
from concurrent.futures import ThreadPoolExecutor

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

solu_numb = True
n = 4

awesome = -1

def check(result):
    global awesome
    global solu_numb
    if len(result.result()) >= 1000:
        solu_numb = False
        awesome = result.result()[-1]

with ThreadPoolExecutor() as executor:
    while solu_numb:
        n += 1
        #factor = factors(n) #okay this just works
        #so i've got a thing where i know that this just... works
        #for thing in factor:
        #    side_1 = n + n//thing
        #    side_2 = side_1 * thing
        #
        #    print(side_1, side_2)
        future = executor.submit(factors, n)
        future.add_done_callback(check)

print(awesome)
