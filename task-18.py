def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if i%n == 0:
            return False
    else:
        return True
        

def rotationalPrime(n):
    s = str(n)
    rotations = []
    
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if isPrime(int(rotated)):
            rotations.append(int(rotated))
    
    return rotations


num = int(input("Enter the number: "))
mylist = rotationalPrime(num)
print(mylist)
