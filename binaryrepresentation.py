n=int(input("Enter a number: "))
def binaryrepresentation(n):
     return format(n,'032b')
     #binary=bin(n)[2:].zfill(32)
     #return binary
print("Binary representation of",n,"is:",binaryrepresentation(n))