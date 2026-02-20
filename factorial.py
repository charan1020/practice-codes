def number(n):#factorial less than or equal to n
    result=[]
    fact=1
    i=1
    while i<=n:
        result.append(fact)
        i+=1
        fact=fact*i
    return result
n=int(input("Enter a number: "))
print(number(n))
