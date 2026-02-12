def counttypechar(s):
    uppercase=0
    lowercase=0
    numeric=0
    special=0
    for char in s:
        if char.isupper():
            uppercase+=1
        elif char.islower():
            lowercase+=1
        elif char.isdigit():
            numeric+=1
        else:
            special+=1
    return uppercase,lowercase,numeric,special
s=input("Enter a string: ")
print(counttypechar(s))