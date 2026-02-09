n=int(input("Enter a number:"))
def counting(n):
    count=0
    temp=n
    while temp>0:
        digit=temp%10
        if digit!=0 and n%digit==0: #here logic is every number is divided which means 2446%2==0,2446%4,2446%4,2446%6==0 so ans is 1st one is correct answer is 1
            count+=1
        temp//=10
    return count
print("Number of dogits:",counting(n))