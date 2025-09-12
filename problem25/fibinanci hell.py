#fibinanci hell

def fibonacci(first,second, count):
    third = first + second
    count += 1
    return second,third,count

first = 1
second = 1
count = 2

while len(str(second)) < 1000:
    #print(first,second,count)
    first, second, count = fibonacci(first, second, count)

print(second, count)
