def oddoccuring(arr):
    result=0
    for num in arr:
        result^=num #XOR OPERATION
    return result
arr=list(map(int,input().split()))
print(oddoccuring(arr))
