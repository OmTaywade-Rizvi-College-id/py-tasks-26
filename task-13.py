def DoubleFactorial(num):
    fact = 1 
    while(num >= 1):
        fact *= num
        num -= 2
    return fact

num = int(input("Enter the number: "))
print(DoubleFactorial(num))