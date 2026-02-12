def si(p,t,r):
    return round(p*t*r)/100
p=float(input("Enter the principal amount: "))
t=float(input("Enter the time period: "))
r=float(input("Enter the rate of interest: "))
print("The simple interest is: ",si(p,t,r))