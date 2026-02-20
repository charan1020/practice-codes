def fascinating(n):
    while n<100:
        return False
    s=str(n)+str(2*n)+str(3*n)
    if len(s)==9 and set(s)==set('123456789'):
        print(s)
        print("Fascinating number")
        return True
    else:
        print(s)
        print("Not a fascinating number")
        return False
n=int(input("Enter a number: "))
print(fascinating(n))