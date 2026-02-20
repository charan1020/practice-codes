def merge(s1,s2):
    result=""
    minlength=min(len(s1),len(s2))
    for i in range(minlength):
        result+=s1[i]
        result+=s2[i]
    result+=s1[minlength:]
    result+=s2[minlength:]
    return result
s1=input("Enter a string: ")
s2=input("Enter a string: ")
print(merge(s1,s2))