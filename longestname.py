def longest_name(arr):  
    max_length = 0  
    longest = ""  
    for name in arr:  
        if len(name) > max_length:  
            max_length = len(name)  
            longest = name  
    return longest 
arr=list(map(str,input().split()))
print(longest_name(arr))  