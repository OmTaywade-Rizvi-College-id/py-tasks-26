userIn = int(input("Enter the number: "))
count = 0
while userIn >= 10:
    cal = 1
    for digit in str(userIn):
        cal *= int(digit)
    userIn = cal
    count += 1
    print(userIn)

print("iteration: ", count)