###
from abc import ABC, abstractmethod
import random
import os
import json

############ Banks and Agencies
"""
## American Bank ##
Agencies 1, 2, 3
Numbers 1, 2, 3

## French Bank ##
Agencies 4, 5
Numbers 4, 5

## Swiss Bank ##
Agencies 6, 7, 8
Numbers 6, 7, 8

## Brazilian ##
Agencies 9, 10
Numbers 9, 10
"""
american_bank = [1, 2, 3]
french_bank = [4, 5]
swiss_bank = [6, 7, 8]
brazilian_bank = [9, 10]

#######################################################################
#######################################################################
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
    
#######################################################################
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
                    self.account = CheckingsAccount()
                    self.type_of_account = "checkings"
                    break
                case "s":
                    print("You chose [s]avings.")
                    self.account = SavingsAccount()
                    self.type_of_account = "savings"
                    break
                case _:
                    print("You did not choose a type of account. Try again.")

    def __repr__(self) -> str:
        return f"{self.type}"

#######################################################################
#######################################################################
class Account(ABC):
    def __init__(self):
        pass
    
    def open_account(self):
        while True:
            print("\nWe work with 4 differente banks, which one would you like to be yours?")
            self.bank = input("[1] American\n[2] French\n[3] Swiss\n[4] Brazilian\n")
            match self.bank:
                case "1":
                    self.bank = "American"
                    self.agency = random.randrange((american_bank[0]),american_bank[-1])
                    self.number = random.randrange((american_bank[0]),american_bank[-1])
                    break
                case "2":
                    self.bank = "French"
                    self.agency = random.randrange((french_bank[0]),french_bank[-1])
                    self.number = random.randrange((french_bank[0]),french_bank[-1])
                    break
                case "3":
                    self.bank = "Swiss"
                    self.agency = random.randrange((swiss_bank[0]),swiss_bank[-1])
                    self.number = random.randrange((swiss_bank[0]),swiss_bank[-1])
                    break
                case "4":
                    self.bank = "Brazilian"
                    self.agency = random.randrange((brazilian_bank[0]),brazilian_bank[-1])
                    self.number = random.randrange((brazilian_bank[0]),brazilian_bank[-1])
                    break
                case _:
                    print("You did not choose a valid bank. Try again.")
        os.system("cls")
        print(f"The bank issue an Agency number and an Account number. \
You should save these numbers to use in our authentication process later.\n\n \
    Your bank is {self.bank} bank.\n \
    Your agency number is {self.agency}.\n \
    Your account number is {self.number}.\n \
    Your account is a {self}")

    @abstractmethod
    def deposit_money(self):
        while True:
            self.amount = input("How much would you like to deposit?\n")
            try:
                self.amount = float(self.amount)
                self.money_in_bank += self.amount
                print(f"Your new amount of money is ${self.money_in_bank}.")
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
                print(f"Your new amount of money is ${self.value}.")
                break
            except:
                print("Please, only type valid numbers. Try again.")
    
    @abstractmethod
    def __repr__(self) -> str:
        return f"{self.type}"

#######################################################################
class CheckingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.type="Checkings Account"

    def deposit_money(self):
        while True:
            self.amount = input("How much would you like to deposit?\n")
            try:
                self.amount = float(self.amount)
                self.money_in_bank += self.amount
                print(f"Your new amount of money is ${self.money_in_bank}.")
                break
            except:
                print("Please, only type valid numbers. Try again.")
        
    def withdrawn_money(self):
        while True:
            self.amount = input("How much would you like to withdrawn?\n")
            try:
                self.amount = float(self.amount)
                self.result = self.money_in_bank - self.amount
                if self.result >= 0:
                    self.money_in_bank -= self.amount
                    print(f"You withdrew ${self.amount}. You now have ${self.money_in_bank} \
in your account.")
                    break
                elif self.result < 0 and self.result >= float(-500):
                    self.money_in_bank -= self.amount
                    print(f"Your withdrawn left you owning the bank, but we still \
lend you some. Your new amount in our account is ${self.money_in_bank}.")
                    break
                else:
                    print("We cannot allow you to withdrawn that amount of money, \
or you will be more in debt than we can allow.")
                    break
            except:
                print("Please, only type valid numbers. Try again.")
                

    def __repr__(self) -> str:
        return f"{self.type}"

#######################################################################
class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.type="Savings Account"
        
    def deposit_money(self):
        while True:
            self.amount = input("How much would you like to deposit?\n")
            try:
                self.amount = float(self.amount)
                self.money_in_bank += self.amount
                print(f"Your new amount of money is ${self.money_in_bank}.")
                break
            except:
                print("Please, only type valid numbers. Try again.")
        
    def withdrawn_money(self):
        while True:
            self.amount = input("How much would you like to withdrawn?\n")
            try:
                self.amount = float(self.amount)
                if self.money_in_bank - self.amount < 0:
                    print(f"We cannot allow you to withdrawn that amount of money \
from your savings account. You only have ${self.money_in_bank}.")
                    break
                else:
                    self.money_in_bank -= self.amount
                    print(f"You withdrawn ${self.amount} from your savings account.\
You now have ${self.money_in_bank}.")
                    break
            except:
                print("Please, only type valid numbers. Try again.")
                
    def __repr__(self) -> str:
        return f"{self.type}"

#######################################################################
#######################################################################
class Bank():
    def __init__(self) -> None:
        self.money_in_bank = 0
        pass
    
    def client_information(self):
        username = input("What is your name?\n")
        age = input("What is your age?\n")
        self.client_info = Client(username, age)
        self.type_account = Client.open_account(self)
        if self.type_of_account == "checkings":
                self.account_info = CheckingsAccount()
        elif self.type_of_account == "savings":
                self.account_info = SavingsAccount()
        self.account_info.open_account()
        
    def deposit_money_bank(self):
        print("You chose to deposit. We need to verify your information first.")
        Bank.authentication(self)
        if self.authenticated == True:
            if self.type_of_account == "checkings":
                CheckingsAccount.deposit_money(self)
                self.authenticated = None
            elif self.type_of_account == "savings":
                SavingsAccount.deposit_money(self)
                self.authenticated = None
            
    def authentication(self):
        while True:
            self.bank_name_auth = input("What is your bank?\n[1] American\n[2] French\n[3] Swiss\n[4] Brazilian\n")
            match self.bank_name_auth:
                    case "1":
                        self.bank_name_auth = "American"
                    case "2":
                        self.bank_name_auth = "French"
                    case "3":
                        self.bank_name_auth = "Swiss"
                    case "4":
                        self.bank_name_auth = "Brazilian"
                    case _:
                        pass
            self.bank_agency_auth = input("What is your agency number?\n")
            self.bank_account_auth = input("What is your account number?\n")
            os.system("cls")
            if self.bank_name_auth == self.account_info.bank \
                and int(self.bank_agency_auth) == self.account_info.agency \
                and int(self.bank_account_auth) == self.account_info.number:
                print("Your information is correct. You may proceed")
                self.authenticated = True
                break
            print("Your information is incorrect. Please try again.")
            self.authenticated = False
        
    def withdrawn_money_bank(self):
        print("You chose to withdrawn. We need to verify your information first.")
        Bank.authentication(self)
        if self.authenticated == True:
            if self.type_of_account == "checkings":
                CheckingsAccount.withdrawn_money(self)
                self.authenticated = None
            elif self.type_of_account == "savings":
                SavingsAccount.withdrawn_money(self)
                self.authenticated = None

    def save_information(self):
        print("Information being saved. Wait until completion to continue.")
        self.savefile = []
        self.savefile.append(self.client_info._name)
        self.savefile.append(self.client_info._age)
        self.savefile.append(self.account_info.bank)
        self.savefile.append(self.account_info.agency)
        self.savefile.append(self.account_info.number)
        self.savefile.append(self.account_info.type)
        self.savefile.append(self.money_in_bank)
        with open("simple-bank_savefile.json", "w", encoding="utf8") as file:
            json.dump(self.savefile, file)
        print("Information saved. You may continue.")

    def __repr__(self) -> str: 
        os.system("cls")
        return f'Your personal information is:\n \
        Your name is {self.client_info._name}.\n \
        Your age is {self.client_info._age}.\n\n\
Your bank information is as follows: \n \
        Your bank is {self.account_info.bank} bank.\n \
        Your agency number is {self.account_info.agency}.\n \
        Your account number is {self.account_info.number}.\n \
        Your account is a {self.account_info.type}\n \
        You currently have ${self.money_in_bank} in your account'

#######################################################################
#######################################################################

print("Welcome to the SimpleBank App! Here you can create your bank account, deposit and withdrawn money \
easily. Let us begin!")
print("First, we will need to collect some informations regarding yourself:")
user = Bank()
Bank.client_information(user)
print()

while True:
    user_input = input("What would you like to do with your account?\n\
        [D]eposit\n\
        [W]ithdrawn\n\
        [L]ist informations\n\
        [S]ave your informations\n\
        [E]xit the app\n").lower()
    match user_input:
        case "d":
            os.system("cls")
            user.deposit_money_bank()
        case "w":
            os.system("cls")
            user.withdrawn_money_bank()
        case "l":
            print(user)
            print()
        case "s":
            os.system("cls")
            user.save_information()
        case "e":
            os.system("cls")
            print("Thank you for using our service!")
            break
        case _:
            print("You did not choose a valid option. Try again.")
