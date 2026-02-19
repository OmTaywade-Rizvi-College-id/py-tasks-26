def calcAdd(*numbers):
    total = 0
    for num in numbers:
        total += num
        
    return total

print(calcAdd(1, 2))
print(calcAdd(1, 3, 2))
print(calcAdd(5, 10, 15, 20))
