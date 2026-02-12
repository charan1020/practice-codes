def multi(n):
    result=[]
    for i in range(1,11):
        result.append(n*i)
    return result
n=int(input("Enter a number:"))
print("Multiplication Table of",n,"is:",multi(n))