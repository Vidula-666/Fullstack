def show_balance():
    print("-----------")
    print("Your balance is {$balance:.2f}")
    print("-----------")
def deposit():
    print("-----------")
    amount=input("Enter an amount to be deposited:")
    print("------------")


    if (amount<0):
        print("Tht's not a valid amount")

    else:
        return amount
def withdraw():
    amount=float(input("Enter amount to be withdrawn: "))

    if amount>balance:
        print("Insufficient funds!!")
    elif amount<0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance=0
is_running=True

while is_running:
    print("Banking program")
    print("-----------")
    print("1.show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("----------")

    choice=input("Enter ur choice(1-4):")

    if choice=='1':
        show_balance(balance)
    elif choice=='2':
       balance+= deposit()
    elif choice=='3':
       balance-= withdraw(balance)
    elif choice=='4':
        is_running=False
    else:
        print("---------")
        print("That is not a valid choice")

print("Thanku !!have a nice day!!")



if __name__ == '__main__':
    main()
