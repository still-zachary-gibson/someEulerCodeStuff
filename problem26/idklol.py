import decimal

# Set precision to a fixed value 
decimal.getcontext().prec = 2000

def stupidly_complicated_function(number):
    oh_god = str(decimal.Decimal(decimal.Decimal(1)/decimal.Decimal(number)))[2:]
    #print(number)
    #print(oh_god)
    #funny_thing = 0
    cur_length = 0
    pattern = ""
    for i in range(len(oh_god)):
        breakw = False
        for j in range(len(pattern)):
            if i > j and oh_god[i] == pattern[j]:
                #print(pattern[j:])
                #print(oh_god[i:i+len(pattern[j:])])
                if oh_god[i:i+len(pattern[j:])] == pattern[j:]:
                    #print(oh_god[i+j+1:1+i+j+len(pattern[j:])])
                    if(oh_god[i+j+1:1+i+j+len(pattern[j:])] == pattern[j:]):
                       # funny_thing = j
                        cur_length -= j
                        breakw = True
                        break
        if breakw:
            break
        cur_length += 1
        pattern += oh_god[i]
    #print(cur_length, funny_thing)
    #print(oh_god[funny_thing:funny_thing+cur_length])
    return cur_length

longest_repeat = [0,0]
for i in range(2,1000):
   #print("-"*20)
   oh_goodness = stupidly_complicated_function(i)
   if longest_repeat[0] < oh_goodness:
       longest_repeat = [oh_goodness,i]

print(longest_repeat)


print(str(decimal.Decimal(decimal.Decimal(1)/decimal.Decimal(263)))[2:])