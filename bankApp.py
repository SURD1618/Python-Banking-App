class BankingApp:

  def __init__(self, initial_balance=0):
    self.balance = initial_balance

  def deposit(self, amount):
    self.balance += amount
    self.log_transaction(f"Deposited ${amount}")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds!")
    else:
      self.balance -= amount
      self.log_transaction(f"Withdrew ${amount}")

  def print_balance(self):
    self.log_transaction(f"Your current balance is: ${self.balance}")
    print(f"Current Balance: ${self.balance}")

  def log_transaction(self, transaction):
    with open("transactions.log", "a") as f:
      f.write(transaction + "\n")


bank = BankingApp()

while True:
  try:
    action = input(
        "Would you like to make a deposit or withdrawal? (d/w/q): ").lower()
    if action == 'd':
      amount = float(input("Enter the deposit amount: "))
      bank.deposit(amount)
    elif action == 'w':
      amount = float(input("Enter the withdrawal amount: "))
      bank.withdraw(amount)
    elif action == 'q':
      print("Exiting the banking app. Goodbye!")
      break
    else:
      print(
          "Invalid input. Please enter 'd' for deposit, 'w' for withdrawal, or 'q' to quit."
      )
  except ValueError:
    print("Invalid input. Please enter a valid amount.")

  bank.print_balance()
