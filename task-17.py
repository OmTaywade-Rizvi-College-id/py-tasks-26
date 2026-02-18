def consecutiveSequence(s):
    count = 1
    maxVal = 0
    result = ""
    for i in range(0, len(s)):
        if int(s[i-1]) < int(s[i]):
            count += 1
            result += s[i-1]
            maxVal = max(maxVal, count)
        else:
            count = 1
            maxVal = 0
            result = ""
    result += s[-1]
    print(count, f"({result})")

s= input("Enter the sequence: ")
consecutiveSequence(s)