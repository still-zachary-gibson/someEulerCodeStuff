#these problems are miserable.

import math

import sys #this just for testin

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
    action_taken_str = strng[1:]
    if len(action_taken_str) < 1: #1 -> 0
        return (1,0) #it is... a move.
    while len(action_taken_str) > 0:
        if action_taken_str[0] == "0":
            action_taken_str = action_taken_str[1:]
        else: break
    else:
        return (len(strng),0)
    #1001 -> 001 -> 01 -> 1
    #okay, goal should be to reduce 0s, but if possible choose ones with more ones?
    #something about uh,,, making moves that lead to more0s being taken?

    #okay lets think
    #1000 vs 1001
    #is one of these better?
    #okay yeah, 1001 is
    #cause it gives an extra turn to 1 in the end

    #but does that matter at all to this algorithm?
    #is there any way that conclusion would affect gameplay?

    #should i also think about 0s gameplan?
    #okay, 0 would prefer 1000 to 1001?
    #1000 -> 100 -> 10 -> 1
    #1001 -> 101 -> 11

    #yeah, 0 would. so 1 should try to go for that one?
    #there's no way for an extra 1 to pop into existence, isn't there?

    #oh god i think there is, 10 can become 1 or 0, depending on who plays
    #there is a way to cause extra turns that way, if 1 FORCES 0 to take moves that keep 1s, and 1 tries to not take moves that don't
    
    #now how to demonstrate that in code. lets see, 100?

    #right meaning 1 played, v is 0 played
    #100 > 0
    #    v 10 > 0
    #         v 1

    #wait no i  dont think there's extra turns? no, thereisn't. it's just how many turns are used up by 0 skipping that changes...
    #so 1's goal is to pull the point where 0 has no more moves, ie all numbers < 10, closer...
    #and 0's goal is to push it farther away.

    #my brain hurts so much

    '''
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
    '''

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
    print("_"*20)
    print(start, "Turn: None")
    while True:
        if not OnesTurn and not any_ones(start):
            if zeroSkips == 0:
                print("It begins!")
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
                    elif destr[0] >= best_descruction[0] and len(i) > len(start[best_descruction[2]]) and best_descruction[0] != -1:
                        best_descruction = (destr[0], destr[1], index)
                        print("Better move?")
            #how_many,which sub index, which_index
            if best_descruction[0] == -1: #apprently this should never be called?
                print("UHM")
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
        print(start, "Turn: " + str(int(OnesTurn)))
        OnesTurn = not OnesTurn
    print(f"Zero won, only needing {zeroSkips} skips.")
    return zeroSkips
        
if game_time(generate_start(2)) != 2:
    print("You broke something REALLY badly.")
    sys.exit()
if game_time(generate_start(5)) != 17:
    print("You broke something.")
    sys.exit()
if game_time(generate_start(10)) != 64:
    print("Still don't got it.")
    sys.exit()

game_time(generate_start(10**5))
#2 = 2
#5 = 17
#10 = 64