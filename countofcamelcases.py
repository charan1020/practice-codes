def count_camelcases(s):
    return sum(1 for char in s if char.isupper())
s=str(input("Enter a string: "))
print(count_camelcases(s))