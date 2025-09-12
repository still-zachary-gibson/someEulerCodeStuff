#card game thingy?

card_amount = 2

import json
import os
import math
def n_choose_k(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

def generate_shuffle(c):
    clean_as_go = True
    progress = True
    if progress:
        ending_val = n_choose_k(c*2, c)
    binary_tree = {"": False}
    while binary_tree.get("") == False:
        #print(len(binary_tree))
        if clean_as_go:
            temp_copy = binary_tree.copy()
            for key in temp_copy.keys():
                if len(key) != c*2 and binary_tree.get(key) == True:
                    if binary_tree.get(key[0:len(key)-1]) == True:
                        #print(key)
                        binary_tree.pop(key)
            temp_copy.clear()
        if progress:
            very_cool = 0
            for key in binary_tree.keys():
                if len(key) == c*2:
                    very_cool += 1
            print(str(very_cool)+"/"+str(ending_val)+" ("+str(round(very_cool/ending_val*10000)/100)+"%)")
        red_cards = c
        black_cards = c
        string = ""
        while red_cards > 0 or black_cards > 0:
            play_red = True
            if not string in binary_tree: #Is this here yet? If not, put it there
                binary_tree.update({string: False})
            elif string+"0" in binary_tree: #has the next red been placed already?
                if binary_tree.get(string+"0") == True: #is it marked as a dead end?
                    play_red = False #if so, black
                    if string+"1" in binary_tree: #is black also been placed?
                        if binary_tree.get(string+"1") == True: #is it a dead end?
                            binary_tree.update({string: True}) #if so, this is one too
                            break
                    elif black_cards == 0: #can we even PLAY black?
                        binary_tree.update({string: True}) #if not, this is a dead end
                        break
            elif string+"1" in binary_tree: #if black doesnt exist, see if red does,
                if binary_tree.get(string+"1") == True: #if dead end...
                    binary_tree.update({string: True}) #its dead
                    break 
            if red_cards > 0 and play_red: #play red unless otherwise stated
                string += "0"
                red_cards -= 1
            elif black_cards > 0: #if out of red or told not to, play black
                string += "1"
                black_cards -= 1
            else: #but if got no black, put red anyways
                string += "0"
                red_cards -= 1
            if black_cards == 0 and red_cards == 0: #inherently this is a dead end
                binary_tree.update({string: True}) #so mark it so previous ones know!
    awesome_list = []
    for key in binary_tree.keys():
        if len(key) == c*2: #remove all the inbetweeners
            awesome_list.append(key)
    return(awesome_list)

def is_fair(sequence):
    print(sequence)
    player_wins = [0,0]
    possibilities = [[sequence,0]]
    while len(possibilities) > 0:
        cards_left,OnesTurn = possibilities.pop()
        last_card = -1
        card = 0
        while card < len(cards_left):
            #print("Cards_Left: "+cards_left[card:], "Last_Card: "+str(last_card), "Turn: "+str(1+OnesTurn))
            if last_card == -1:
                last_card = cards_left[card]
                card += 1
                if card >= len(cards_left):
                    OnesTurn = 1 - OnesTurn
            else:
                if cards_left[card] == last_card:
                    #print("Coinflip!")
                    possibilities.append([cards_left[card:], 1-OnesTurn]) #the lose the flip case, for later
                    card += 1
                OnesTurn = 1 - OnesTurn
                last_card = -1
        #print("WIN: ",(1-OnesTurn)+1)
        player_wins[1-OnesTurn] += 1
    print(player_wins)
    return player_wins[1] == player_wins[0]


def calc_groups(amount_):
    if os.path.isfile("saved_tree_"+str(amount_)):
        with open("saved_tree_"+str(amount_), 'r') as config_file:
            all_games = json.load(config_file)
    else:
        all_games = generate_shuffle(amount_)

        with open("saved_tree_"+str(amount_), 'w') as config_file:
            json.dump(all_games, config_file)
    return all_games

all_games = calc_groups(8)

print(len(all_games), n_choose_k(16, 8))

i = 0

while i < len(all_games):
    if is_fair(all_games[i]):
        i += 1
    else:
        all_games.pop(i)
    #print("_"*20)

print(len(all_games))

#print(n_choose_k(40, 20))