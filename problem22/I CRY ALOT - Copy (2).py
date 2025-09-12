#oh god.

f = open("0022_names.txt")
name_hell = f.read()
name_hell = name_hell.replace('"',"")
name_list = name_hell.split(",")

def letter_to_number(char, zero_index=1):
    return ord(char)-64-zero_index

def sort_alpha(string):
    letter_numb = letter_to_number(string[0])
    if len(sorted_list[letter_numb]) == 0:
        sorted_list[letter_numb].append(string)
    else:
        ok_done = False
        starting_numb = 0
        letter_to_check = 1
        while not ok_done:
            for j in range(starting_numb, len(sorted_list[letter_numb])):
                if(letter_to_check > 1):
                    if len(sorted_list[letter_numb][j]) <= letter_to_check-1:
                        sorted_list[letter_numb].insert(j+1, string)
                        ok_done = True
                        break
                    if letter_to_number(string[letter_to_check-1]) < letter_to_number(sorted_list[letter_numb][j][letter_to_check-1]):
                        sorted_list[letter_numb].insert(j, string)
                        ok_done = True
                        break
                if len(sorted_list[letter_numb][j]) <= letter_to_check:
                    sorted_list[letter_numb].insert(j+1, string)
                    ok_done = True
                    break
                elif len(string) <= letter_to_check:
                    sorted_list[letter_numb].insert(j, string)
                    ok_done = True
                    break
                elif letter_to_number(string[letter_to_check]) > letter_to_number(sorted_list[letter_numb][j][letter_to_check]):
                    if j+1 == len(sorted_list[letter_numb]):
                        ok_done = True
                        sorted_list[letter_numb].append(string)
                        break
                    #if letter_to_check > 1:
                    #   letter_to_check -= 1
                    continue
                elif letter_to_number(string[letter_to_check]) < letter_to_number(sorted_list[letter_numb][j][letter_to_check]):
                    sorted_list[letter_numb].insert(j, string)
                    ok_done = True
                    break
                else:
                    print(sorted_list[letter_numb])
                    letter_to_check += 1
                    starting_numb = j
                    break
                




sorted_list = []
for i in range(26):
    sorted_list.append([])

for i in name_list:
    sort_alpha(i)
    print(sorted_list)
    
