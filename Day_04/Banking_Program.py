
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}\n")

def deposit(balance):
    amount=float(input("Enter the amount you want to deposit:$"))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
 
def withdraw(balance):
    amount=float(input("Enter the amount you want to withdraw:"))

    if amount > balance:
        print("Insufficient amount")
        return 0
    
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    
    else:
        return amount

def main():
   balance=0
   is_running=True

   while is_running:
      print("***********************")
      print("    Banking Program   ")
      print("***********************")
      print("1. Show Balance")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Exit")

      choice=input("Enter your choice from (1-4):")

      if choice == '1':
          show_balance(balance)
    
      elif choice == '2':
         balance+=deposit(balance)

      elif choice == '3':
         balance-=withdraw(balance)
    
      elif choice == '4':
         is_running=False

      else:
         print("That is invalid choice")

   print("Thank you! Have a nice day!")


main()