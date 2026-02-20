def prefix(arr):
    result=[]
    total=0
    for i in range(len(arr)):
        total+=arr[i]
        avg=total//(i+1)
        result.append(avg)
    return result
arr=list(map(int,input().split()))
print(prefix(arr))

