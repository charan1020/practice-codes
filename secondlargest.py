def seconlargest(arr):
    largest=-1
    secondlargest=-1
    for num in arr:
        if num>largest:
            secondlargest=largest
            largest=num
        elif num>secondlargest and num!=largest:
            secondlargest=num
    return secondlargest
arr=list(map(int,input().split()))
print(seconlargest(arr))

