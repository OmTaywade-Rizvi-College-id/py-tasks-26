nums = input("Enter 3 Nos Seperated by Space: ")
inputList = nums.split(" ")
compValues = [i for i in range(len(inputList)) if inputList[i] > inputList[i-1]]
print(inputList[compValues[len(compValues) -1 ]])