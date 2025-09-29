def euclid_algo(n,m):
    steps = 0
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n
        steps += 1
    return n, steps

smallest_numb = (0,999999999999)
numb = 10**12 + 39

for i in range(1,numb):
    results = euclid_algo(numb,i)
    if results[0] != 1:
        continue
    if results[1] < smallest_numb[1]:
        #print(results, smallest_numb)
        smallest_numb = (i, results[1])

print(smallest_numb)
