print("=============Simple Banking System=============")

balance=1000

choice=int(input("Enter 1 for Check the balance\nEnter 2 for Depositing the money\nEnter 3 for withdrawal\nEnter: "))

if choice==1:
    print(f"The total amount in bank is {balance}")
elif choice==2:
    deposit_amount=int(input("Enter the amount you want to deposit "))

    balance=balance+deposit_amount
    print(f"The total amount in bank after depositing is {balance}")
elif choice==3:
    withdrawal_amount = int(input("Enter the amount you want to withdrawal "))
    
    if withdrawal_amount > balance:
        print("Insufficient balance")
    else:
        balance=balance-withdrawal_amount
        print(f"The total amount in bank after withdrawal is {balance}")
else:
    print("Invalid Operation")