// Prime Gap Finder
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if(n%i == 0):
            return False;
        
    return True

num = int(input("Enter the number: "))
print(isPrime(num))
ans = 0
count = 0
while(count < 2):
    num += 1
    if(isPrime(num)):
        count += 1
        print(num)
        ans = num - ans
       
print(ans)
