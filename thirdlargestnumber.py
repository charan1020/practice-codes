def thirdlargest(arr):
    first=-1
    second=-1
    third=-1
    for num in arr:
        if num>first:
            third=second
            second=first
            first=num
        elif num>second and num!=first:
            third=second
            second=num
        elif num>third and num!=second:
            third=num
    return third
arr=list(map(int,input().split()))
print(thirdlargest(arr))
