def gp(n,a,r):
    if r==1:
        return a*n
    else:
        return a*(r**n-1)//(r-1)
n,a,r=map(int,input().split())
print(gp(n,a,r))