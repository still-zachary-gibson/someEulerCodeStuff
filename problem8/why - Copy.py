hell = [
    list("73167176531330624919225119674426574742355349194934"),
    list("96983520312774506326239578318016984801869478851843"),
    list("85861560789112949495459501737958331952853208805511"),
    list("12540698747158523863050715693290963295227443043557"),
    list("66896648950445244523161731856403098711121722383113"),
    list("62229893423380308135336276614282806444486645238749"),
    list("30358907296290491560440772390713810515859307960866"),
    list("70172427121883998797908792274921901699720888093776"),
    list("65727333001053367881220235421809751254540594752243"),
    list("52584907711670556013604839586446706324415722155397"),
    list("53697817977846174064955149290862569321978468622482"),
    list("83972241375657056057490261407972968652414535100474"),
    list("82166370484403199890008895243450658541227588666881"),
    list("16427171479924442928230863465674813919123162824586"),
    list("17866458359124566529476545682848912883142607690042"),
    list("24219022671055626321111109370544217506941658960408"),
    list("07198403850962455444362981230987879927244284909188"),
    list("84580156166097919133875499200524063689912560717606"),
    list("05886116467109405077541002256983155200055935729725"),
    list("71636269561882670428252483600823257530420752963450")
]
# oh my goodness gee willikers

biggest_product = 0
last_biggest = 0
alt_list = []

for y_pos in range(len(hell)):
    alt_list.append([])
    for x_pos in range(len(hell[y_pos])):
        alt_list[y_pos].append(0)
        if biggest_product != last_biggest:
            print(biggest_product)
            last_biggest = biggest_product
        if x_pos+12 < len(hell[y_pos]):
            #teststring = ""
            alt_list[y_pos][x_pos] += 1
            testnum = 1
            for i in range(0, 13):
                #teststring += hell[y_pos][x_pos+i]
                testnum *= int(hell[y_pos][x_pos+i])
                if testnum == 0:
                    break
            #print(teststring)
            if testnum > biggest_product:
                biggest_product = testnum
            if y_pos+12 < len(hell):
                #teststring = ""
                alt_list[y_pos][x_pos] += 10
                testnum = 1
                for i in range(0, 13):
                 #   teststring += hell[y_pos+i][x_pos+i]
                    testnum *= int(hell[y_pos+i][x_pos+i])
                    if testnum == 0:
                        break
                #print(teststring)
                if testnum > biggest_product:
                    biggest_product = testnum
        if y_pos+12 < len(hell):
            testnum = 1
            alt_list[y_pos][x_pos] += 100
            #teststring = ""
            for i in range(0, 13):
            #    teststring += hell[y_pos+i][x_pos]
                testnum *= int(hell[y_pos+i][x_pos])
                if testnum == 0:
                    break
            #print(teststring)
            if testnum > biggest_product:
                biggest_product = testnum
        if x_pos-12 >= 0:
            if y_pos+12 < len(hell):
                alt_list[y_pos][x_pos] += 1000
                testnum = 1
                #teststring = ""
                for i in range(0, 13):
                #    teststring += hell[y_pos+i][x_pos-i]
                    print(x_pos-i)
                    testnum *= int(hell[y_pos+i][x_pos-i])
                    if testnum == 0:
                        break
                #print(teststring)
                if testnum > biggest_product:
                    biggest_product = testnum
        for i in range(4-len(str(alt_list[y_pos][x_pos]))):
            alt_list[y_pos][x_pos] = "0" + str(alt_list[y_pos][x_pos])
print(biggest_product)

#for i in range(len(alt_list)):
   # print(alt_list[i])