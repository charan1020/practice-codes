def solve(n:int,a:list,b:int):
    for i in range(n):
        if a[i]==b:
            b=b*2
    return b
n=int(input("Enter the number of elements in the array: "))
a=list(map(int,input().split()))
b=int(input("Enter a number: "))
print(solve(n,a,b))