def multiflyarray(arr,n):
    result = 1
    for i in range(n):
        result *= arr[i]
    return result
n=int(input("Enter the number of elements in the array: "))
arr=list(map(int,input().split()))
print(multiflyarray(arr,n))