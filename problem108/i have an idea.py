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

awesome = -1

prime_list = []
max_prime = 0

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

for i in range(1,100):
    is_prime(i)

def factorization(numba, repeat=True):
    if(numba > max_prime):
        temp_length = len(prime_list)
        iter = max_prime+1
        while len(prime_list)-2 < temp_length:
            is_prime(iter)
            iter += 1
        #print(prime_list)
    if numba == 1:
        return [1]
    if is_prime(numba):
        return [numba]
    return_ma = []
    number = numba
    iter = 0
    for iter in prime_list:
        if(number % iter == 0):
            while number % iter == 0:
                number /= iter
                if repeat:
                    return_ma.append(iter)
            if not repeat:
                return_ma.append(iter)
        if(number == 1):
            break
    return return_ma

def product_notation(_list):
    total = 1
    for i in _list:
        total *= i
    return total

def flatten_list(nested_list, first=False):
    flat_list = []

    for i in nested_list:
        if type(i) is list:
            if len(i) != 0:
                if(type(i[0]) is list):
                    flat_list.extend(flatten_list(i))
                else:
                    flat_list.append(flatten_list(i))
            #else:
            #flat_list.append(i)
        else:
            flat_list.append(i)

    return flat_list

def check(result):
    global awesome
    global solu_numb
    print(str(len(result.result())) + " from " + str(result.result()[-1]) + "\n")
    if len(result.result()) > 1000:
        solu_numb = False
        awesome = result.result()[-1]

def inf_fors(n, min, max, results):
    thing_to_return = []
    if len(n) == 1:
        return results
    else:
        for i in range(min, max, -1):
            thing_to_return.append(inf_fors(n[1:len(n)], i-1, 0, results + [i]))
        return thing_to_return

def cool_calcs(n):
    prime_facts = factorization(n, False)
    s = product_notation(prime_facts)
    v = n//s
    oaky = inf_fors(prime_facts, 10, 0, [])
    print(flatten_list(oaky, True))

cool_calcs(97772875200)
'''

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
'''