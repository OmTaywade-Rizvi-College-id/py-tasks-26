a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c= int(input("Enter the c: "))

print(f"Equation is: {a}x^2 + {b}x + {c} = 0")
d= b**2 -4*a*c
if d>0:
    root1= (-b + d**0.5)/(2*a)
    root2= (-b - d**0.5)/(2*a)
    print(f"Roots are real and different: {root1}, {root2}")
elif d==0:
    root= -b/(2*a)
    print(f"Roots are real and same: {root}")
else:
    realPart= -b/(2*a)
    imagPart= (-d)**0.5/(2*a)
    print(f"Roots are complex and different: {realPart}+{imagPart}i, {realPart}-{imagPart}i")
    