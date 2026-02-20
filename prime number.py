def primenumber(n):
    if n<=1:
        print(n,"is not a prime number")
        return False
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            return False
    print(n,"is a prime number")
    return True
n=int(input("Enter a number: "))
print(primenumber(n))