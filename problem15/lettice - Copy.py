# okay i want 4 choices through a 2x2 grid to have 6 routes

#0011
#0101
#1100
#0110
#1001
#1010

routes = 0
max_moves = 6
maps = []
place_to_splore = 1

while True:
    zero_amount = max_moves/2
    string = ""
    while len(string) < max_moves:
        if zero_amount > 0:
            if len(string)+1 == max_moves-place_to_splore:
                string += "1"
                #place_to_splore = 0
            else:
                zero_amount -= 1
                string += "0"
        else:
            if max_moves-len(string) > place_to_splore:
                place_to_splore = max_moves-len(string)
            string += "1"
    print(string)