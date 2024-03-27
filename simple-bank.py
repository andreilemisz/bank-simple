###
from abc import ABC, abstractmethod
import random

class Person(ABC):
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
        
    def set_name(self, name):
        self._name = name
        
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age
    
    @abstractmethod
    def __repr__(self) -> str:
        return f'Person is {self._name} | Age is {self._age}'
    
class Client(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.account = None
    
    def open_account(self):
        while True: 
            self.account = input("Which type of account do you want to open, [c]heckings or [s]avings?\n").lower()
            match self.account:
                case "c":
                    print("You chose [c]heckings.")
                    self.account = CheckingsAccount(self)
                    self.account.open_account()
                    break
                case "s":
                    print("You chose [s]avings.")
                    self.account = SavingsAccount(self)
                    self.account.open_account()
                    break
                case _:
                    print("You did not choose a type of account. Try again.")

    def __repr__(self) -> str:
        if self.account:
            return f"Person is {self._name}\nAge {self._age}\n\
Account type {self.account.type}\nBank {self.account.bank}\n\
Agency {self.account.agency}\nNumber {self.account.number}"
        
        return f"Person is {self._name} | Age {self._age}"

class Account(ABC):
    def __init__(self, bank, agency, number) -> None:
        self.bank = bank
        self.agency = agency
        self.number = number
        self.value = 0
    
    def open_account(self):
        while True:
            print("Which bank would you like to choose?")
            self.bank = input("[1] American\n[2] French\n[3] Swiss\n[4] Brazilian\n")
            match self.bank:
                case "1":
                    self.bank = "American"
                    break
                case "2":
                    self.bank = "French"
                    break
                case "3":
                    self.bank = "Swiss"
                    break
                case "4":
                    self.bank = "Brazilian"
                    break
                case _:
                    print("You did not choose a valid bank. Try again.")
        print(f"You chose the {self.bank} bank.")
        self.agency = random.randrange(1,100)
        print(f"Your agency number is {self.agency}")
        self.number = random.randrange(1,1000)
        print(f"Your account number is {self.number}")
        
    def deposit_money(self):
        while True:
            self.amount = input("How much would you like to deposit?\n")
            try:
                self.amount = float(self.amount)
                self.value += self.amount
                print(f"Your new amount of money is {self.value}.")
                break
            except:
                print("Please, only type valid numbers. Try again.")
    
    @abstractmethod
    def withdrawn_money(self):
        while True:
            self.amount = input("How much would you like to withdrawn?\n")
            try:
                self.amount = float(self.amount)
                self.value -= self.amount
                print(f"Your new amount of money is {self.value}.")
                break
            except:
                print("Please, only type valid numbers. Try again.")
    
    @abstractmethod
    def __repr__(self) -> str:
        return f"Account type {self.type}\nBank {self.bank}\n\
Agency {self.agency}\nNumber {self.number} "

class CheckingsAccount(Account):
    def __init__(self, bank=None, agency=None, number=None):
        super().__init__(bank=None, agency=None, number=None)
        self.type="Checkings Account"
        
    def withdrawn_money(self):
        while True:
            self.amount = input("How much would you like to withdrawn?\n")
            try:
                self.amount = float(self.amount)
                if self.amount - self.value < (-500.0):
                    self.value -= self.amount
                    print(f"Your withdrawn left you owning the bank, but we still\
lend you some. Your new amount in our account is {self.value}.")
                    break
                else:
                    print("We cannot allow you to withdrawn that amount of money, \
or you will be in debt.")
                    break
            except:
                print("Please, only type valid numbers. Try again.")
        
    def __repr__(self) -> str:
        return f"Your Checkings Account Details:\nBank {self.bank}\n\
Agency {self.agency}\nNumber {self.number}"

class SavingsAccount(Account):
    def __init__(self, bank=None, agency=None, number=None, type="Checkings Account"):
        super().__init__(bank=None, agency=None, number=None)
        self.type="Savings Account"
        
    def withdrawn_money(self):
        while True:
            self.amount = input("How much would you like to withdrawn?\n")
            try:
                self.amount = float(self.amount)
                if self.amount - self.value > 0:
                    print(f"We cannot allow you to withdrawn that amount of money \
from your savings account. You only have {self.value}.")
                    break
                else:
                    self.value -= self.amount
                    print(f"You withdrawn {self.value} from your savings account.\
You now have {self.value}.")
                    break
            except:
                print("Please, only type valid numbers. Try again.")
                
    def __repr__(self) -> str:
        return f"Your Savings Account Details:\nBank {self.bank}\n\
Agency {self.agency}\nNumber {self.number}"

class Bank:
    def __init__(self) -> None:
        pass


###################

username = input("What is your name?\n")
user_age = input("What is your age?\n")
person1 = Client(username, user_age)
print(person1)
person1.open_account()
print()
print()
print(person1)
print()
print()
print(person1.account)
print()
print()
person1.account.deposit_money()
person1.account.withdrawn_money()
person1.account.withdrawn_money()
