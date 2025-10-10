#okay lets. see how do i even GENERATE a polynomial?

#i guess first i'll just like... model out the function.
#i should make this like... multipurpose, i do think.

#okay floating point is killing me
from decimal import *

def numb_to_dec(n):
    return Decimal(str(n))

#how many is how many y values to generate (1-[]). 1 gives you x=1; 2 gives x=1,2; etc. you can make it a list to set the range, though i made the top inclusive!
#coefficents is the coefficents, and also term amount. highest term first, 4x^2 - 3x + 1; would be put in as 4,-3,1
def polynomial_ints_outputer(how_many, *coefficents):
    list_of_outputs = []

    if type(how_many) is int:
        how_many = [1, how_many]

    if len(coefficents) == 1:
        sort_it_out = []
        for i in coefficents:
            for j in i:
                sort_it_out.append(j)
        coefficents = tuple(sort_it_out)

    coefficents = coefficents[::-1]

    for x in range(how_many[0],how_many[1]+1):
        sum = numb_to_dec(0)
        for term, n in enumerate(coefficents):
            sum += numb_to_dec(n) * numb_to_dec(x)**numb_to_dec(term)
        list_of_outputs.append(int(sum))

    return list_of_outputs

#print(polynomial_ints_outputer(3,4,-3,1))

#okay, it works i'm fairly sure,,,

the_canonical_sequence = (polynomial_ints_outputer(10,1,-1,1,-1,1,-1,1,-1,1,-1,1))
#i can use big fancy words :)

def matrix_mult(a,b):
    #oh geesz this is gonna be painful.
    c = []
    for rows in range(len(a)):
        c.append([])
        for columns in range(len(b[rows])):
            sum = numb_to_dec(0)
            for a_col in range(len(a[rows])):
                #print("a:", a_col, rows, a[rows][a_col])
                #print("b:", columns, a_col, b[a_col][columns])
                #print(a[rows][a_col], b[a_col][columns])
                sum += numb_to_dec(numb_to_dec(a[rows][a_col]) * numb_to_dec(b[a_col][columns]))
            c[rows].append(numb_to_dec(sum))
    return c

#c = matrix_mult([[1,4,-2],[3,5,-6]],[[5,2,8,-1],[3,6,4,5],[-2,9,7,-3]])
#result matches the video i used, so my matrix works
#for i in c:
#    print(i)

def determinant(old):
    if len(old) == 2:
        return numb_to_dec(numb_to_dec(old[0][0])*numb_to_dec(old[1][1])-numb_to_dec(old[0][1])*numb_to_dec(old[1][0]))
    #elif len(old) == 3:
    else:
        resulting_factors = []
        for cur_row in range(len(old)):
            temp_matrix = []
            iter = -1
            for temp_row in range(len(old)):
                if temp_row != cur_row:
                    temp_matrix.append([])
                    iter += 1
                    for temp_col in range(1,len(old[temp_row])):
                        temp_matrix[iter].append(old[temp_row][temp_col])
            resulting_factors.append(numb_to_dec(determinant(temp_matrix)))
        returning_sum = 0
        for cur_row in range(len(old)):
            #print(old[cur_row][0] * resulting_factors[cur_row] * (-1)**cur_row)
            returning_sum += numb_to_dec(old[cur_row][0]) * numb_to_dec(resulting_factors[cur_row]) * numb_to_dec(-1)**numb_to_dec(cur_row)
        #print(returning_sum)
        #print("waggabaga bobo")
        return numb_to_dec(returning_sum)
        '''
        uhm_yeah = []
        for cur_row in range(len(old)):
            for cur_col in range(len(old[cur_row])):
            #cur_col = 0
                uhm_yeah.append([])
                temp_matrix = []
                iter = -1
                for temp_row in range(len(old)):
                    if temp_row != cur_row:
                        temp_matrix.append([])
                        iter += 1
                        for temp_col in range(len(old[temp_row])):
                            if temp_col != cur_col:
                                temp_matrix[iter].append(old[temp_row][temp_col])
                uhm_yeah[cur_row].append(determinant(temp_matrix) * (-1)**(cur_row+cur_col))
        sim = 0
        for i in range(len(uhm_yeah)):
            for j in range(len(uhm_yeah[i])):
                sim += uhm_yeah[i][j] * old[i][j]
        #print(sim)
        return sim
        '''

def get_co(old):
    if len(old) == 2:
        return [[old[1][1], -old[0][1]],[-old[1][0], old[0][0]]]
    else:
        uhm_yeah = []
        for cur_row in range(len(old)):
            uhm_yeah.append([])
            for cur_col in range(len(old[cur_row])):
                temp_matrix = []
                iter = -1
                for temp_row in range(len(old)):
                    if temp_row != cur_row:
                        temp_matrix.append([])
                        iter += 1
                        for temp_col in range(len(old[temp_row])):
                            if temp_col != cur_col:
                                temp_matrix[iter].append(old[temp_row][temp_col])
                uhm_yeah[cur_row].append(numb_to_dec(determinant(temp_matrix)) * numb_to_dec((-1)**(cur_row+cur_col)))
        return uhm_yeah

def matrix_inverse(old_matrix):
    ajoint = transpose(get_co(old_matrix)) #UP TO COFACTOR IT WORKS
    determint = numb_to_dec(determinant(old_matrix))
    inverse = []
    for cur_row in range(len(ajoint)):
        inverse.append([])
        for cur_col in range(len(ajoint[cur_row])):
            inverse[cur_row].append(numb_to_dec(numb_to_dec(ajoint[cur_row][cur_col]) / determint))
    return inverse #ITS FINE HERE.
    #for i in inverse:
    #    print(i)

#matrix_inverse([[1,1,1],[2,1,1],[1,1,2]])

def transpose(old_matrix):
    new_matrix = []
    for y in range(len(old_matrix[0])):
        new_matrix.append([])
        for x in range(len(old_matrix)): new_matrix[y].append(0)
    for y in range(len(old_matrix)):
        for x in range(len(old_matrix[y])):
            new_matrix[x][y] = numb_to_dec(old_matrix[y][x])
    return new_matrix

def polynomial_factory(ref_points):
    x_matrix = []
    for y in range(len(ref_points)):
        x_matrix.append([])
        for x in range(len(ref_points)):
            x_matrix[y].append(numb_to_dec(numb_to_dec(y+1)**numb_to_dec(x)))
    x_t = transpose(x_matrix)
    y_t = transpose([ref_points])
    coefficents_temp = (matrix_mult(matrix_mult(matrix_inverse(matrix_mult(x_t, x_matrix)),x_t),y_t))
    coefficents = []
    for i in coefficents_temp:
        for j in i:
            coefficents.append(int(j))
    #print(coefficents)
    return reversed(coefficents)
    #print(y_t)

#matrix_inverse([[1,2,0],[-1,1,1],[1,2,3]])

#print(get_co([[3,4,9,2],[2,37,7,8],[2,9,3,23],[1,86,9,6]]))

#print(matrix_inverse([[1,2,0],[-1,1,1],[1,2,3]]))

#print(determinant([[37,7,8],[9,3,23],[86,9,6]]))

#print(determinant([[1,1,1,1],[1,1,0,4],[1,0,2,0],[1,4,0,3]]))
#print(the_canonical_sequence[:3])
#print(polynomial_ints_outputer(3,polynomial_factory(the_canonical_sequence[:3])))

total_sum = 1
for terms in range(2,10):
    #print(the_canonical_sequence[:terms+1])

    if terms == 5:
        print("les inspect")

    temp_co = polynomial_factory(the_canonical_sequence[:terms])
    sequence = polynomial_ints_outputer(terms+1, temp_co)

    print(str(terms) + ":")
    print(the_canonical_sequence[:terms+1])
    print(sequence[:terms+1])
    print("-"*20)

    total_sum += sequence[terms]

print(total_sum)