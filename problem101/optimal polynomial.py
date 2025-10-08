#okay lets. see how do i even GENERATE a polynomial?

#i guess first i'll just like... model out the function.
#i should make this like... multipurpose, i do think.

#how many is how many y values to generate (1-[]). 1 gives you x=1; 2 gives x=1,2; etc. you can make it a list to set the range, though i made the top inclusive!
#coefficents is the coefficents, and also term amount. highest term first, 4x^2 - 3x + 1; would be put in as 4,-3,1
def polynomial_ints_outputer(how_many, *coefficents):
    list_of_outputs = []

    if type(how_many) is int:
        how_many = [1, how_many]

    coefficents = coefficents[::-1]

    for x in range(how_many[0],how_many[1]+1):
        sum = 0
        for term, n in enumerate(coefficents):
            sum += n * x**term
        list_of_outputs.append(sum)

    return list_of_outputs

#print(polynomial_ints_outputer(3,4,-3,1))

#okay, it works i'm fairly sure,,,

the_canonical_sequence = (polynomial_ints_outputer(10,1,-1,1,-1,1,-1,1,-1,1,-1,1))
#i can use big fancy words :)

def transpose(old_matrix):
    new_matrix = []
    for y in range(len(old_matrix)):
        new_matrix.append([])
        for x in range(len(old_matrix[y])):
            new_matrix[y].append(old_matrix[x][y])
    return new_matrix

def polynomial_factory(ref_points):
    x_matrix = []
    for y in range(len(ref_points)):
        x_matrix.append([])
        for x in range(len(ref_points)):
            x_matrix[y].append((y+1)**x)
    x_t = transpose(x_matrix)
    #y_t = transpose([ref_points])
    #print(y_t)
    
polynomial_factory(the_canonical_sequence)