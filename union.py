def union(a,b):
    return sorted(set(a)|set(b))
a=list(map(int,input("enter a list array:").split()))
b=list(map(int,input("enter b list arry:").split()))
print("union of two arrays is:",union(a,b))