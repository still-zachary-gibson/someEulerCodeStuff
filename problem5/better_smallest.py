prime_list = [1,2,3,5,7,11,13,17,19]

numb = 1

for i in range(9):
    numb *= (prime_list[i])

iter = 1
found = False
while not found:
    test_numb = numb * iter
    for i in range (1,21):
        print(test_numb, i)
        if test_numb % i != 0:
            iter = iter + 1
            break
        elif i == 20:
            found = True

print(test_numb)