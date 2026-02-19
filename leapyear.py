def leapyear(n):
    if n%4==0 and n%100!=0 or n%400==0:
        print(n,"is a leap year")
        return True
    else:
        print(n,"is not a leap year")
        return False
n=int(input("Enter a year: "))
print(leapyear(n))