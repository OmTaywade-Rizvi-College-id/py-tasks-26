def palindrone(string):
    if(string == string[::-1]):
        print("Palindrone hai")
    else:
        print("Not a Palindrone")

string = input("Enter string: ")
palindrone(string)