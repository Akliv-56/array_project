def upper_triangle(matrix:list[list[int or float]]):
    #i  0  1  2  3  4 j
    #0 [1, 2, 3, 4, 5],
    #1 [4, 5, 6, 7, 8],
    #2 [7, 8, 9, 1, 2],
    #3 [4, 5, 6, 7, 8],
    #4 [5, 6, 7, 8, 9]
    for i in range(0,len(matrix),1):
        for j in range(i,len(matrix[i]),1):
            print(matrix[i][j], end=" ")
        print()
upper_triangle([[1,2,3],[4,5,6],[7,8,9]])

def lower_triangle(matrix:list[list[int or float]]):
    for i in range(0, len(matrix),1):
        for j in range(0,i+1,1):
            print(matrix[i][j],end=" ")
        print()
lower_triangle([[1,2,3],[4,5,6],[7,8,9]])

def left_triangle(matrix:list[list[int or float]]):
    #i  0  1  2  3  4 j
    #0 [1, 2, 3, 4, 5],
    #1 [4, 5, 6, 7, 8],
    #2 [7, 8, 9, 1, 2],
    #3 [4, 5, 6, 7, 8],
    #4 [5, 6, 7, 8, 9]
    counter = 0
    for i in range(0,len(matrix),1):
        if i >= len(matrix)/2:
            counter += 2
        for j in range(0,i+1-counter,1):
            print(matrix[i][j],end=" ")
        print()
    
left_triangle([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,1,2],[4,5,6,7,8],[5,6,7,8,9]])
            


def top_triangle(matrix:list[list[int or float]]):
    for j in range(0,len(matrix[0]),1):
        if j > len(matrix)/2:
            for i in range(0,len(matrix)-j,1):
                print(matrix[i][j],end=" ")
        else:
            for i in range(0,j + 1,1):
                print(matrix[i][j],end=" ")
        print()
top_triangle([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,1,2],[4,5,6,7,8],[5,6,7,8,9]])
