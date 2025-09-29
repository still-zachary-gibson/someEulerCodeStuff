def euclid_algo(n,m):
    steps = 0
    while m != 0:
        if n > m:
            n -= m
        else:
            m -= n
        #if n < m:
            #n,m = m,n
        #n -= m
        steps += 1
        '''if n%m == 0:
            steps += n/m
            n =
            ''' 
    return n, steps

smallest_numb = (0,999999999999)
numb = 89 # 10**12 + 39

for i in range(1+3,numb):
    results = euclid_algo(numb,i)
    if results[0] != 1:
        continue
    if results[1] < smallest_numb[1]:
        #print(results, smallest_numb)
        smallest_numb = (i, results[1])

print(smallest_numb)