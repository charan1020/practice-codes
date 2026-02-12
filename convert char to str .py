def convert_list_to_string(arr,n):
    return ''.join(arr)
n=int(input("Enter the number of elements in the array: "))
arr=list(map(str,input().split()))
print(convert_list_to_string(arr,n))
