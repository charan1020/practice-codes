def intersection(a,b):
    set_a=set(a)
    count=0
    for num in b:
        if num in set_a:
            count+=1
    return count
a=list(map(int,input("enter a list array:").split()))
b=list(map(int,input("enter b list arry:").split()))
print("intersection of two arrays is:",intersection(a,b))