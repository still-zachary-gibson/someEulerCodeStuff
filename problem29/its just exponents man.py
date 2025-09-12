annoying_list = []
max_numb = 100

for a in range(2, max_numb+1):
    for b in range(2,max_numb+1):
        result = a**b
        if not result in annoying_list:
            annoying_list.append(result)

print(len(annoying_list))
