N=2
M=3
def sumofelements(N,M,matrix):
    total=0
    for i in range(N):
        for j in range(M):
            total=total+matrix[i][j]
    print("The sum of elements in the matrix is:",total)
    return total
sumofelements(N,M,[[1,2,3],[4,5,6]])
                   