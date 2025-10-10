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

def matrix_mult(a,b):
    #oh geesz this is gonna be painful.
    c = []
    for rows in range(len(a)):
        c.append([])
        for columns in range(len(b[rows])):
            sum = 0
            for aNumb in range(len(a[rows])):
                sum += (a[rows][aNumb] * b[aNumb][columns])
            c[rows].append(sum)
    return c

#c = matrix_mult([[1,4,-2],[3,5,-6]],[[5,2,8,-1],[3,6,4,5],[-2,9,7,-3]])
#result matches the video i used, so my matrix works
#for i in c:
#    print(i)

def determinant(old):
    if len(old) == 2:
        return old[0][0]*old[1][1]-old[0][1]*old[1][0]
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
            resulting_factors.append(determinant(temp_matrix))
        returning_sum = 0
        for cur_row in range(len(old)):
            print(old[cur_row][0] * resulting_factors[cur_row] * (-1)**cur_row)
            returning_sum += old[cur_row][0] * resulting_factors[cur_row] * (-1)**cur_row
        print(returning_sum)
        print("waggabaga bobo")
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
            uhm_yeah[cur_row].append(determinant(temp_matrix) * (-1)**(cur_row+cur_col))
    return uhm_yeah

def matrix_inverse(old_matrix):
    cofactor = transpose(get_co(old_matrix))
    print(cofactor)
    determint = 1
    inverse = []
    for cur_row in range(len(cofactor)):
        inverse.append([])
        for cur_col in range(len(cofactor[cur_row])):
            inverse.append(cofactor[cur_row][cur_col] / determint)
    pass

#matrix_inverse([[1,1,1],[2,1,1],[1,1,2]])

def transpose(old_matrix):
    new_matrix = []
    for y in range(len(old_matrix[0])):
        new_matrix.append([])
        for x in range(len(old_matrix)): new_matrix[y].append(0)
    for y in range(len(old_matrix)):
        for x in range(len(old_matrix[y])):
            new_matrix[x][y] = old_matrix[y][x]
    return new_matrix

def polynomial_factory(ref_points):
    x_matrix = []
    for y in range(len(ref_points)):
        x_matrix.append([])
        for x in range(len(ref_points)):
            x_matrix[y].append((y+1)**x)
    x_t = transpose(x_matrix)
    y_t = transpose([ref_points])
    print(matrix_mult(x_t, x_matrix))
    #print(y_t)

#matrix_inverse([[1,2,0],[-1,1,1],[1,2,3]])

#print(get_co([[3,4,9,2],[2,37,7,8],[2,9,3,23],[1,86,9,6]]))

print(determinant([[37,7,8],[9,3,23],[86,9,6]]))

#print(determinant([[1,1,1,1],[1,1,0,4],[1,0,2,0],[1,4,0,3]]))
#polynomial_factory(the_canonical_sequence)  