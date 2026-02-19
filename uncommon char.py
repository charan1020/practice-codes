def uncommon(s1,s2):
    return ''.join(sorted(set(s1)^set(s2)))
s1=input("Enter a string: ")
s2=input("Enter a string: ")
print({uncommon(s1,s2)})