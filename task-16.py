def countString(string):
    # mylist = []
    # count = 1
    # for i in range(len(string)-1):
    #     if string[i] == string[i+1]:
    #         count += 1
    #     else:
    #         mylist.append(string[i])
    #         mylist.append(count)
    #         count = 1
    # mylist.append(string[-1])
    # mylist.append(count)  
    # return mylist
    count = 1
    result =""
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += string[i - 1] + str(count)
            count = 1
    
    result += string[-1] + str(count)
    return result

def deCodeStr(s):
    result = ""
    
    for i in range(0, len(s) ,2):
        result += s[i] * int(s[i+1])
    
    return result

userstr = input("Enter the string: ")
string = countString(userstr)
print(string)
print(deCodeStr(string))