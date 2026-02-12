def factorial(n):
    count=1
    for i in range(1,n+1):
        if n!=0:
            count*=i
    return count
n=int(input("Enter a number: "))
print("The factorial of",n,"is:",factorial(n))