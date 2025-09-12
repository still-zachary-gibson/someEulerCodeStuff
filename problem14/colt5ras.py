def coltra(n):
    iter_count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        if n > 1:
            iter_count += 1
    return iter_count

biggest = [0,0]
for i in range(1000000):
    value = coltra(i)
    if value > biggest[0]:
        biggest = [value, i]
        print(biggest)

print(i)
