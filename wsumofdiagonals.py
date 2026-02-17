def diagonal(N,Grid):
    primary=0
    secondary=0
    for i in range(N):
        primary+=Grid[i][i]
        secondary+=Grid[i][N-i-1]
    print (abs(primary-secondary))
N=3
Grid=[[1,2,5],[4,5,6],[7,8,9]]
diagonal(N,Grid)