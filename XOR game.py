def game(n,arr):
    for i in range(n-1):
        arr[i]=arr[i]^arr[i+1]
    return arr
n=int(input("Enter the number of elements in the array: "))
arr=list(map(int,input().split()))
print(game(n,arr))
