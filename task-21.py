total_amount = 0
pin = None

def check_balance():
    print(f"Current Balance: {total_amount}")

def authenticate(epin):
    return epin == pin

def deposit(amount):
    global total_amount
    attempt = 0
    
    while attempt < 5:
        epin = int(input("Enter the pin: "))
        
        if authenticate(epin):
            total_amount += amount
            print("Amount Deposited successfully")
            return
        else:
            attempt += 1
            print(f"Pin is incorrect. {attempt} attempt(s)")
            
            if attempt >= 5:
                print("Too many failed attempts.")
                return
            
            nattempt = input("Do you want to continue? (y or n): ")
            if nattempt.lower() != 'y':
                return

def withdraw(amount):
    global total_amount
    attempt = 0
    
    while attempt < 5:
        epin = int(input("Enter the pin: "))
        
        if authenticate(epin):
            if amount > total_amount:
                print("Insufficient Balance")
                return
            total_amount -= amount
            print(f"Amount {amount} withdrawn successfully")
            return
        else:
            attempt += 1
            print(f"Pin is incorrect. {attempt} attempt(s)")
            
            if attempt >= 5:
                print("Too many failed attempts.")
                return
            
            nattempt = input("Do you want to continue? (y or n): ")
            if nattempt.lower() != 'y':
                return

def main_menu():
    print("\n1. Deposit")
    print("2. Check Balance")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        amount = int(input("Enter the amount to deposit: "))
        deposit(amount)
    elif choice == 2:
        check_balance()
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        withdraw(amount)
    elif choice == 4:
        print("Thank you for using ourBank.")
    else:
        print("Invalid choice")

print("--------Welcome to ourBank-------")

checkAccount = input("Is Account present? (y or n): ")

if checkAccount.lower() == 'y':
    pin = int(input("Set the pin: "))
    main_menu()
else:
    print("Please create an account first.")
