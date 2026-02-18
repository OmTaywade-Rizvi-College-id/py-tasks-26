inputstr = input("Enter the values sepearated by space: ")
inputlist = inputstr.split(" ")
length = len(inputlist)
inputlist = map(int, inputlist)
avg = sum(inputlist)/ length
print(f"Avg: {avg}")