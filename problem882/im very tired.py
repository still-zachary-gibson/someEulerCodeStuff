#these problems are miserable.

import math

#this one generates the starting state
def generate_start(n):
    cool = []
    for i in range(1,n+1):
        for j in range(i): cool.append(num_to_binary(i))
    return cool

#okay lets see here, see how big the number is compared to power of twos...
#log, probably
def num_to_binary(n): #input int
    hi_est = (math.floor(math.log2(n)))
    binary = ""
    while hi_est >= 0:
        if n - 2**hi_est >= 0:
            n -= 2**hi_est
            binary += "1"
        else:
            binary += "0"
        hi_est -= 1
    #while binary[0] == "0": #Wait, this code is never used.
    #    binary = binary[1:]
    return binary #output str

def binary_to_num(b): #input str
    b = str(b)
    number = 0
    while len(b) > 0:
        if b[0] == "1":
            number += 2**(len(b)-1)
        b = b[1:]
    return number #output int

#not actually needed, i think?


#print(generate_start(3))

#binary_to_num("101")

#while True:
#    num_to_binary(int(input("Enter num: ")))

#cool, i've got the number functions down.
#NOW HOW DO I SIMULATE A GAME!!!

#lets at least get the conditions in first,,,

def sum_with_strs(array): #are we at the end?
    numb = 0
    for i in array:
        numb += int(i)
        if numb > 0: #lets just save time man
            break
    return numb

def any_ones(array): #can zero play any moves?
    wrong = False
    for i in array:
        if i.count("1") > 0 and i.count('0') > 0:
            wrong = True
            break
    return wrong

def zero_destroyer(strng): #see how many 0s any move would remove
    max_leading = (0,0)
    for index in range(len(strng)):
        if strng[index] == "0":
            continue
        temp = strng[:index] + strng[index+1:]
        leading = 1
        for char in temp:
            if char == "1":
                break
            else:
                leading += 1
        if leading > max_leading[0]:
            max_leading = (leading, index)
    return max_leading

#while True:
#    print(zero_destroyer(input("Enter Binary Num: ")))

def zero_saver(strng): #find what one saves the most 0s.
    best_case = (math.inf, 0)
    for index in range(len(strng)):
        if strng[index] == "1":
            continue
        temp = strng[:index] + strng[index+1:]
        leading = 1
        for char in temp:
            if char == "1":
                break
            else:
                leading += 1
        if leading < best_case[0]:
            best_case = (leading, index)
    return best_case

#while True:
#    print(zero_saver(input("Enter Binary Num: ")))

def game_time(start):
    OnesTurn = True
    zeroSkips = 0
    #print(start, OnesTurn)
    while True:
        if not OnesTurn and not any_ones(start):
            OnesTurn = not OnesTurn
            zeroSkips += 1
            continue
        if sum_with_strs(start) == 0:
            break
        if OnesTurn:
            best_descruction = (0,0,0)
            for index, i in enumerate(start):
                destr = zero_destroyer(i)
                if destr[0] >= best_descruction[0]:
                    best_descruction = (destr[0], destr[1], index)
            #how_many,which sub index, which_index
            choice = best_descruction[2]
            choice2 = best_descruction[1]
        else:
            best_descruction = (-1,0,0)
            for index, i in enumerate(start):
                if i.count("0") > 0 and i.count("1") > 0:
                    destr = zero_destroyer(i)
                    if destr[0] > best_descruction[0]:
                        best_descruction = (destr[0], destr[1], index)
            #how_many,which sub index, which_index
            if best_descruction[0] == -1:
                best_descruction=(math.inf,0,0)
                for index, i in enumerate(start):
                    if i != "0":
                        destr = zero_saver(i)
                        if destr[0] < best_descruction[0]:
                            best_descruction=(destr[0], destr[1], index)
            choice = best_descruction[2]
            choice2 = zero_saver(start[choice])[1]
        #choice = int(input("Which one to remove? "))
        #choice2 = int(input("Which position? "))
        if int(OnesTurn) != int(start[choice][choice2]):
            print("WEE WOO")
        start[choice] = start[choice][:choice2] + start[choice][choice2+1:]
        if start[choice] == "":
            start[choice] = "0"
        else:
            while start[choice][0] == "0" and len(start[choice]) > 1:
                start[choice] = start[choice][1:]
        #print(start, int(OnesTurn))
        OnesTurn = not OnesTurn
    print(f"Zero won, only needing {zeroSkips} skips.")
        


game_time(generate_start(10))