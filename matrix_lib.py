def upper_triangle(matrix:list[list[int or float]]):
    #i  0  1  2 j
    #0 [1, 2, 3],
    #1 [4, 5, 6],
    #2 [7, 8, 9]
    for i in range(0,len(matrix),1):
        for j in range(i,len(matrix[i]),1):
            print(matrix[i][j], end=" ")
        print()
upper_triangle([[1,2,3],[4,5,6],[7,8,9]])