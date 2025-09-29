def euclid_algo(n,m):
    steps = 0
    times_since_changed = [0,0]
    while m != n:
        if n > m:
            times_since_changed[0] = -1
            n -= m
        else:
            times_since_changed[1] = -1
            m -= n
        '''
        times_since_changed[0] += 1
        times_since_changed[1] += 1
        if times_since_changed[1] > 20:
            steps += n/m
            n = m
        elif times_since_changed[0] > 20:
            steps += m/n
            m = n
        else:
        '''
        steps += 1
    return n, steps

smallest_numb = (0,999999999999)
numb = 10**12 + 39

#print(euclid_algo(89, 34))

for i in range(1,numb):
    results = euclid_algo(numb,i)
    if results[0] != 1:
        continue
    if results[1] < smallest_numb[1]:
        #print(results, smallest_numb)
        smallest_numb = (i, results[1])

print(smallest_numb)