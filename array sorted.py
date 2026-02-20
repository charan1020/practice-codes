def arraysort(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
arr=list(map(int,input().split()))
print(arraysort(arr))