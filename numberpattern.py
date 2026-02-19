def pattern(N):
    result=[]
    for i in range(1,N+1):
        pattern=""
        for j in range(1,i+1):
            pattern+=str(j)
        for j in range(i-1,0,-1):
            pattern+=str(j)
        result.append(pattern)
    print("\n".join(result))
N=int(input("Enter a number: "))
pattern(N)

