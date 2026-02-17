def isAutomorphic(n):
    square=n*n
    temp=n
    count=0
    while temp>0:
        temp//=10
        count+=1
    if square%(10**count)==n:
        print( "Automorphic")
    else:
        print("Not Automorphic")
    return n
n=int(input("Enter a number: "))
isAutomorphic(n)

    

