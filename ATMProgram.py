
"""                         Standard English - ATM Program

This program will function as a simple ATM program to simulate how transactions that occur
at ATMs are made. 
Transactions availble in ATM program will be see balance, deposit, withdraw, 
and exit ATM. 

The program begins by taking in the users card and requiring the users input for
the card pin. 
If the pin is correct, the user is welcomed and can then choose from 4 options: "Balance", "Deposit", "Withdraw", 
and "Exit ATM" and must input their desired selection. If pin is not correct, a "Wrong pin" message
is displayed and the user must input try to input correct pin again. 

If the user chooses "balance" option, the program displays the balance to the user.
The user is then asked if they wish to make another transacion; If no, program 
exits displaying to user "Thank you for using this ATM", but if yes, program 
continues and user can pick another transaction option.

If the user chooses  "Withdraw" option, the program takes in user input of desired withdraw
amount. If the withdraw amount is more than the available balance, an "Insufficient funds" message
displays and a transaction must be chosen again. If the withdraw amount is less than available balance, 
than a "Transaction Successful" message
is displayed alongside the users new balance after the transaction. 
Next, the user is then asked if they wish to make another transacion; If no, program 
exits displaying a message "Thank you for using this ATM" to the user, but if yes, program 
continues and user can pick another transaction option.

If the user chooses "Deposit" option, the program takes in user input of the desired deposit
amount. The amount is added to the current balance and a "Transaction Successful" message
is displayed alongside the users new balance.
The user is then asked if they wish to make another transacion; If no, program 
exits displaying to user "Thank you for using this ATM", but if yes, program 
continues and user can pick another transaction option.

If the user chooses to see "Exit" option, the program exits and "Thank you for using ATM" message is displayed to user.

"""

"""                         Pseudocode - ATM Program

Print to user ("Please insert your card)
Ask user input () for card pin
balance = set balance$$$$
pin = set pin 

if pin is correct
    print("Welcome to Sierra Valley ATM)
    Print("Select Transaction option

    1) Balance
    2) Withdraw
    3) Deposit
    4) Exit ATM 
    " ) 

    While true:
        option = input of user transaction desired selection  

        if option = 1: 
            print balance to user
            Print message to user and take input if they wish to make another transaction
            If yes:
                continue
            else: 
                print "Thank you for using Sierra Valley ATM" to user
                exit ATM Program
        elif option = 2:
            print (available balance, balance)
            withdraw = user input of desired amount 
            if balance > withdraw
                total = balance - withdraw
                print ("Transaction successful")
                print (new balance to user, total)
            else:
                print "Insufficient funds"
        elif option = 3
            print (available balance, balance)
            deposit = user input of desired amount 
            totalbalance = balance + deposit amount
                print ("Transaction successful")
                print (Total new balance to user, totalbalance)
        elif option = 4
            print("Thank you for using this ATM")
            exit ()
        else:
            print("no selected transaction")

else: 
    print("Wrong pin, please try again")
    user input(users card pin )
        
"""

print("Please insert your card")
pin = int(input("Enter your card pin: "))

balance = 1000

if pin == 1234:
    print("""
    ---- Welcome to Sierra Valley ATM ----
    Please Select A Transaction option

    1) Balance
    2) Withdraw
    3) Deposit
    4) Exit ATM 

    """) 

    while True:
        option = int(input("Enter desired transaction option: "))  

        if(option == 1): 
            print("Your balance is: ", balance) 
            anothertrans = input("Do you wish to make another transaction YES/NO: ") 
            if(anothertrans == "YES"): 
                continue
            else: 
                print("Thank you for using Sierra Valley ATM!")
                break 
        elif(option == 2):
            print("Available balance: ", balance)
            withdraw = float(input("Enter desired amount to withdraw: ")) 
            if(balance > withdraw): 
                total = balance - withdraw
                print("Transaction successful!")
                print("Your new balance is: ", total)
            else:
                print("Insufficient balance")
        elif(option == 3):
            print("Available balance: ", balance)
            deposit = float(input("Enter desired amount to withdraw: "))  
            totalbalance = balance + deposit
            print("Transaction successful!")
            print ("Total balance is now: ", totalbalance)
        elif(option == 4):
            print("Thank you for using Sierra Valley ATM!")
            exit ()
        else:
            print("No selected transaction")

else: 
    print("Wrong pin, please try again")
    input("Enter your card pin: ")