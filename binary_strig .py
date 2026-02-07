s=input("Enter a string:")
is_binary=True
for ch in s:
    if ch!= '0' and ch!='1':
        is_binary=False
        break
if is_binary:
    print("True")
else:
    print("False")
