def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
x1=int(input("Enter the value of x1: "))
y1=int(input("Enter the value of y1: "))    
x2=int(input("Enter the value of x2: "))
y2=int(input("Enter the value of y2: "))
print (distance(x1,y1,x2,y2))