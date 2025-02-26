''' Assigement 01 
Name: Aproj Husensab Myageri
email: aprojmyageri0786@gmail.com
Ph. no: 9611519967
Department: Electrical and Electronics Engineering
Passout year: 2026
'''


My_account_number = 2004042313         #define variable 
My_phone_number = 1234567890            #define variable
My_adhara_number = 9876543210           #define variable
My_bank_balance = 1000                             #define variable

Account_number = int(input("Please enter your account number:")) #ask input from the user
Mobile_number = int(input("Please enter your mobile number:"))     #ask input from the user

if Account_number == My_account_number and Mobile_number == My_phone_number:   #if user entered correct account number and mobile number then it entered into loop otherwise 
    while True:
        print("Welcome to AJ Bank")
        print("1. Deposite Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Change Mobile number")
        print("5. Change My Adhara number")
        print("6. Exit")

        choice = int(input("Please enter your choice: "))  #ask input from the user

        if choice == 1: #if user entered 1
            amount = int(input("Enter amount to deposite: ")) #ask input from the user
            if amount > 0: #if user entered amount greater then 0
                My_bank_balance += amount #the amount add to the balance 
                print(f"You deposited INR {amount} and your new balance is INR {My_bank_balance}")
            else:
                print("Invalid amount") #if user entered amount equal to  0
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount > 0 and amount <= My_bank_balance:  #if amount is greater then 0 or less then balance amount
                My_bank_balance -= amount #sub amount from the balance
                print(f"You withdrew INR {amount} and your new balance is INR {My_bank_balance}")
            else:
               print(f"Invalid_amount_or_insufficient_balance") #if amount is less then 0 orgreater then balance amount

        elif choice == 3: 
            print(f"Your balance is INR {My_bank_balance}")
        elif choice == 4:
            old_mobile_number = (int(input("Enter your old mobile number: ")))
            if old_mobile_number == My_phone_number: #if user entered old ph. N0 correctlly
             new_mobile_number = (int(input("Enter your new mobile number: "))) #ask the user for new number 
             My_phone_number = new_mobile_number 
             print(f"Your mobile number is changed to {My_phone_number}")
            else:
                print("Invalid_mobile_number") #if user entered old ph. N0 wrong 

        elif choice == 5:
            old_adhara_number = (int(input("Enter your old adhara number:")))
            if old_adhara_number == My_adhara_number:
               new_adhara_number = (int(input("Enter your new adhara number: ")))
               My_adhara_number = new_adhara_number
               print(f"Your adhara number is changed to {My_adhara_number}")
            else:
               print("Invalid_adhara_number")
        elif choice == 6:
            print("Thank you for using AJ Bank")
            break # exit fron the loop
        else:
            print("Invalid choice") #if user entered grater then 6 as a choice
else:
    print("Invalid account number or mobile number") #if user entered wrong a\c number and mobile number 
