def perfect(n):
    odd=1
    while n>0:
        n=n-odd
        odd=odd+2
    if n==0:
        print(n,"is a perfect number")
        return 1
    else:
        print(n,"is not a perfect number")
        return 0
n=int(input("Enter a number: "))
print(perfect(n))