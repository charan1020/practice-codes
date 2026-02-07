n=int(input("Enter a number:"))
def sumofdigits(n):
    total=0
    while n>0:
        digit=n%10
        total=total+digit
        n=n//10
    print("The sum of digits is:",total)
    return total
sumofdigits(n)