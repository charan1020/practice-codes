def noofdivisors(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:         #it is for only condition for divisible by 3 is if n%i==0 and i%3==0:
            count+=1
    return count
n=int(input("Enter a number: "))
print("The number of divisors of",n,"is:",noofdivisors(n))
