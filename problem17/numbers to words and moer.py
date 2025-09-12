def digit_to_word(digit):
    return_table = ["","one","two","three","four","five","six","seven","eight","nine"]
    return return_table[int(digit)]
def tens_digit_to_word(digit):
    return_table = ["","CRY","twenty","thirty","forty","fifty", "sixty","seventy","eighty","ninety"]
    return return_table[int(digit)]

def number_to_word(number, spaces=False):
    word = ""
    number = str(number)
    iter_ater = len(number)
    higher = False
    if number == "0":
        iter_ater = 0
        word = "zero"
    while iter_ater > 0:
        print(iter_ater%3)
        if iter_ater == 4:
            #word += digit_to_word(number[len(number)-iter_ater])
            if spaces:
                word += " "
            word += "thousand"
            if spaces:
                word += " "
        if iter_ater % 3 == 0:
            if higher == False:
                if number[len(number)-iter_ater] != "0":
                    word += digit_to_word(number[len(number)-iter_ater])
                    if spaces:
                        word += " "
                    word += "hundred"
                    if spaces:
                        word += " "
            higher = False
            if number[(len(number)-iter_ater+1):(len(number)-iter_ater+2)] != "00":
               word += "and"
               if spaces:
                word += " "
        if iter_ater % 3 == 1:
            clean = tens_digit_to_word(number[len(number)-iter_ater])
            if clean != "CRY":
                word += clean
                if spaces and number[(len(number)-iter_ater+1):(len(number)-iter_ater+1)] != "0" and clean != "":
                    word += "-"
            else:
                higher = True
                if number[(len(number)-iter_ater+1):(len(number)-iter_ater+1)] == "0":
                    word += "ten"
                elif number[(len(number)-iter_ater+1):(len(number)-iter_ater+1)] == "1":
                    word += "eleven"
                elif number[(len(number)-iter_ater+1):(len(number)-iter_ater+1)] == "2":
                    word += "twelve"
                elif number[(len(number)-iter_ater+1):(len(number)-iter_ater+1)] == "3":
                    word += "thirteen"
                elif number[(len(number)-iter_ater+1):(len(number)-iter_ater+1)] == "5":
                    word += "fifteen"
                elif number[(len(number)-iter_ater+1):(len(number)-iter_ater+1)] == "8":
                    word += "eighteen"
                else:
                    word += digit_to_word(number[len(number)-iter_ater+1]) + "teen"
        if iter_ater % 3 == 2:
            if higher == False:
                word += digit_to_word(number[len(number)-iter_ater])
            higher = False
        iter_ater -= 1
    if spaces:
        word = word.strip()
    return word

print(digit_to_word(13))

'''

hellish_string = ""
hellish_string_two = ""

for i in range(1,1001):
    if i > 500:
        hellish_string_two += number_to_word(i)
    else:
        hellish_string += number_to_word(i)
    print(number_to_word(i))
    '''