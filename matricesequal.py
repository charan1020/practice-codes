def matrices(matrix1,matrix2,N,M):
    for i in range(N):
        for j in range(M):
            if matrix1==matrix2:
                print("The matrices are equal")
            else:
                print("The matrices are not equal")
    
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,0]]
N=3
M=3
matrices(matrix1,matrix2,N,M)

