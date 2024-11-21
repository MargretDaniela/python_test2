# Basic: Create a class called Car with attributes brand and color. Instantiate
#  an object of the Car class and print its attributes.
class Car:
    brand = 'RangeRover'
    color = 'white'
data = Car()
print(data.brand)
print(data.color)

# Intermediate: Add a method called start_engine to the Car 
# class that prints a message saying the engine of the car has 
# started. Create an instance of Car and call the method.
class Car:
    def __init__(self,start_engine):
        self.start_engine = start_engine

start = Car('The Car Engine Has Started')
print(start.start_engine)
# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.
class BankAccount:
    def _init_(self, account_number, balance=0):
        # Initialize the account with account number and an optional balance (default is 0)
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        # Deposit an amount into the account.
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        # Withdraw an amount from the account if sufficient balance exists.
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. Current balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def print_balance(self):
        # Print the current balance of the account.
        print(f"Account {self.account_number} balance: {self.balance}")

#Create an account with account number '12345' and initial balance of 10000
account = BankAccount('12345', 100000)

# Deposit 50000
account.deposit(50000)

# Try to withdraw 12000
account.withdraw(12000)

# Withdraw 20000
account.withdraw(20000)

# Print current balance
account.print_balance()

# Challenge: Implement a class called Library that manages a collection of
#  books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).
class Book:
  def __init__(self, title, author,available_status ):
    self.title = title
    self.author = author
    self.available_status = available_status

  def printname(self):
    print(self.title, self.author, self.available_status )

class Library(Book):
  def __init__(self, title, author, available_status, OliverTwist):
    super().__init__(title, author, available_status, OliverTwist)
    self.book = OliverTwist

  def welcome(self):
    print("Welcome to our library with", self.title, self.author,self.available_status, "to the class of", self.OliverTwist)

x = Library("Government Inspector", "Joel", 'yes','OliverTwist')
x.welcome()
