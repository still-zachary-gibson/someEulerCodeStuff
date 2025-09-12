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
            is_in = False
            for i in maps:
                if i == string:
                    is_in = True
                    break
            zero_amount -= 1
            string += "0"
        else:
            string += "1"
        is_in = False
        for i in maps:
            if i == string:
                is_in = True
                break
        if not is_in:
            maps.append(string)
    print(maps)
    print(string)