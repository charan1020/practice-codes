def checksparse(n):
    if(n&(n>>1)):
        return False
    return True
print(checksparse(72))
print(checksparse(100))