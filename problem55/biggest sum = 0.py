biggest_sum = 0

for a in range(2,100+1):
    for b in range(2,100+1):
        test = a**b
        temp = 0
        for numb in str(test):
            temp += int(numb)
        if temp > biggest_sum:
            biggest_sum = temp

print(biggest_sum)
