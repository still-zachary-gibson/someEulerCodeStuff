import math

permutations = []

def n_choose_k(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

def generate_shuffle(conditions):
    clean_as_go = True
    progress = False
    if progress:
        print("Don't, I'm not sure how to calculate it")
        #print(pow(sum(conditions), sum(conditions) - len(conditions)+1))
        #ending_val = n_choose_k(c*2, c)
    binary_tree = {"": False}
    while binary_tree.get("") == False:
        #print(len(binary_tree))
        options = conditions.copy()
        if clean_as_go:
            temp_copy = binary_tree.copy()
            for key in temp_copy.keys():
                if len(key) != sum(options) and binary_tree.get(key) == True:
                    if binary_tree.get(key[0:len(key)-1]) == True:
                        #print(key)
                        binary_tree.pop(key)
            temp_copy.clear()
        string = ""
        while sum(options) > 0:
            play_which = 0
            stopNo = True
            while True:
                if not string in binary_tree: #Is this here yet? If not, put it there
                    binary_tree.update({string: False})
                    break #no need to check any further
                else:
                    if string+str(play_which) in binary_tree: #has the next current choice been placed already?
                        if binary_tree.get(string+str(play_which)) == True: #is it marked as a dead end?
                            play_which += 1 #if so, move to the next possible play
                            if play_which >= len(options): #okay this is screwed clearly
                                binary_tree.update({string: True})
                                stopNo = False
                                break
                        else:
                            break
                    else: #it isn't?
                        if options[play_which] > 0:
                            break #then splore!
                        else:
                            play_which += 1
                            if play_which >= len(options): #okay this is screwed clearly
                                binary_tree.update({string: True})
                                stopNo = False
                                break
            if not stopNo:
                break
            which_way = -1
            while True:
                if options[play_which] > 0:
                    string += str(play_which)
                    options[play_which] -= 1
                    break
                else:
                    if play_which == 0:
                        which_way = 1
                    play_which += which_way
                    if play_which >= len(options):
                        raise BaseException("I have clearly done something wrong.")
            if sum(options) == 0: #inherently this is a dead end
                binary_tree.update({string: True}) #so mark it so previous ones know!
    awesome_list = []
    for key in binary_tree.keys():
        if len(key) == sum(options): #remove all the inbetweeners
            awesome_list.append(key)
    return(awesome_list)

total = []
for i in range(3):
    thing = [1,1,1]
    thing[i] += 1
    total.extend(generate_shuffle(thing))

print(total)
