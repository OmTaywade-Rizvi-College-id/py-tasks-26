val= input("Enter string seperated with comma: ")
sepList = val.split(",")
sqCubeList = [int(sepList[i])**2 if i%2 == 0 else int(sepList[i])**3 for i in range(len(sepList))]
print(sqCubeList)