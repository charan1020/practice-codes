def paliarray(arr):
    for num in arr:
        if str(num)!= str(num)[::-1]:
            return False
    return True
arr=list(map(int,input().split()))
print(paliarray(arr))