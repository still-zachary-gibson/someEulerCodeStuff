def check_power_sum_thing(number, power):
    numb_string = str(number)
    the_sum = 0
    for i in numb_string:
        the_sum += int(i) ** power
    return number == the_sum

max = 100000000
power = 5
things = []

for i in range(2,max):
    if int(str(i)[0]) == 1 and int(str(i)[1:]) == 0:
        print(i)
    if check_power_sum_thing(i, power):
        things.append(i)

print(things)

sum_em = 0

for i in things:
    sum_em += i
print(sum_em)
