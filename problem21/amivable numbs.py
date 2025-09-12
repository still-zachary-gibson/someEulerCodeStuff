# okay amicable numbers, gonna want a running total me thinks? array?
# i may have a slight addiction to arrays perhaps.
possible_amics = []

for i in range(1,10001): #change to 10001
    my_sum = 1
    include_even = 1 if i % 2 == 0 else 2
    if include_even == 1:
        my_sum += 2
    for j in range(3,i,include_even): #okay any way to reduce this amount? we can kill evens for odds
        if i % j == 0:
            my_sum += j
    if my_sum != 1 and my_sum != 2:
        possible_amics.append([i, my_sum])

actual_amicables = []

for i in range(len(possible_amics)):
    for j in range(i):
        if possible_amics[i][0] == possible_amics[j][1] and possible_amics[i][1] == possible_amics[j][0]:
            actual_amicables.append(possible_amics[i][0])
            actual_amicables.append(possible_amics[i][1])
    
print(actual_amicables)

cool_sum = 0

for i in actual_amicables:
    cool_sum += i

print(cool_sum)
