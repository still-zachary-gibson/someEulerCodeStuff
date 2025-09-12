my_iter = 7010180
found = False

while not found:
    for i in range (2,21):
        print(my_iter, i)
        if my_iter % i != 0:
            my_iter = my_iter + 20
            break
        elif i == 20:
            found = True
print(my_iter)
