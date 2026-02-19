def letters(s):
    result=s[0]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            result+=s[i]
    return result
s=input("Enter a string: ")
print(letters(s))