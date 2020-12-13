
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
displays and a transaction must be chosen again. If the withdraw amount is less than available balance, than a "Transaction Successful" message
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