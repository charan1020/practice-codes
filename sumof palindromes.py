def pali(n):
    s=0
    while n>0:
        digit=n%10
        s+=digit
        n=n//10
    if str(s)==str(s)[::-1]:
        return True
    else:
        return False
n=int(input("Enter a number: "))
print(pali(n))

