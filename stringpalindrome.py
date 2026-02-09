def string(arr):
    for num in arr:
        if str(num)!= str(num)[::-1]:
            return False
    return True
n=int(input("Enter the number of elements in the array: "))
arr=list(map(int,input().split()))
print(string(arr))