n=int(input("enter a number:"))
def countdigits(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print("number of digits:",countdigits(n))