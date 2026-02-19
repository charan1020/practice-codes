def maxoccuring(s):
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1
    maxcount=0
    result=''
    for char in sorted(freq):
        if freq[char]>maxcount:
            maxcount=freq[char]
            result=char
    return result
s=input("Enter a string: ")
print(maxoccuring(s))