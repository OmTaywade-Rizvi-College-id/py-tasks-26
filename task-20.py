from statistics import mean, median, mode, variance, stdev

# def median(s):
#     s.sort()
#     mid = int(s[0]) + (int(s[-1]) - int(s[0]))
#     return mid

# def mean(s):
#     total = 0
#     for i in intList:
#         total += int(i)
#     meanVal = total/len(intList)   
#     return meanVal

# def mode(s):
#     s.sort()
#     for i in range(1, len(s)):
#         if s[i-1] == s[i]:
#             return s[i]
    
#     return -1

# def variance(s):
#     meanVal = mean(s)
#     total= 0
#     for i in s:
#         total += (int(i) - meanVal)**2
#     return total/len(s)

# def deviation(s):
#     var = variance(s)
#     return float(var**0.5)

s = input("Enter the comma string sepearated string: ")
intList= [int(item.strip()) for item in s.split(',')]
print(mean(intList))
print(median(intList))
print(mode(intList))
print(variance(intList))
print(stdev(intList))