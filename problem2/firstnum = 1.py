firstnum = 1
secondnum = 2
awesome_numb = 0
holder = 2
while awesome_numb < 4000000:
    awesome_numb = firstnum + secondnum
    firstnum = secondnum
    secondnum = awesome_numb
    if awesome_numb % 2 == 0 and awesome_numb < 4000000:
        print(awesome_numb)
        holder += awesome_numb

print(holder)
