def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(gcd(a, b))