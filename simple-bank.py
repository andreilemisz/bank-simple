###
from abc import ABC, abstractmethod
import random
import os

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
american_bank = ["1", "2", "3"]
french_bank = ["4", "5"]
swiss_bank = ["6", "7", "8"]
brazilian_bank = ["9", "10"]

############

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
        if self.account:
            return f"Person is {self._name}\nAge {self._age}\n\
Account type {self.account.type}\nBank {self.account.bank}\n\
Agency {self.account.agency}\nNumber {self.account.number}"
        
        return f"Person is {self._name} | Age {self._age}"

class Account(ABC):
    def __init__(self) -> None:
        pass
    
    def open_account(self):
        while True:
            print("Which bank would you like to choose?")
            self.bank = input("[1] American\n[2] French\n[3] Swiss\n[4] Brazilian\n")
            match self.bank:
                case "1":
                    self.bank = "American"
                    self.agency = random.randrange(1,3)
                    self.number = random.randrange(1,3)
                    break
                case "2":
                    self.bank = "French"
                    self.agency = random.randrange(4,5)
                    self.number = random.randrange(4,5)
                    break
                case "3":
                    self.bank = "Swiss"
                    self.agency = random.randrange(6,8)
                    self.number = random.randrange(6,8)
                    break
                case "4":
                    self.bank = "Brazilian"
                    self.agency = random.randrange(9,10)
                    self.number = random.randrange(9,10)
                    break
                case _:
                    print("You did not choose a valid bank. Try again.")
        print(f"You chose the {self.bank} bank.")
        print(f"Your agency number is {self.agency}")
        print(f"Your account number is {self.number}")
        
    def deposit_money(self):
        while True:
            self.amount = input("How much would you like to deposit?\n")
            self.value = 0
            try:
                self.amount = float(self.amount)
                self.value += self.amount
                print(f"Your new amount of money is {self.value}.")
                break
            except:
                print("Please, only type valid numbers. Try again.")
    
    # @abstractmethod
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
    
    # @abstractmethod
    def __repr__(self) -> str:
        return f"Account type {self.type}\nBank {self.bank}\n\
Agency {self.agency}\nNumber {self.number} "

class CheckingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.type="Checkings Account"
        
        
    def withdrawn_money(self):
        while True:
            self.amount = input("How much would you like to withdrawn?\n")
            self.value = self.client_info.value
            try:
                self.amount = float(self.amount)
                self.result = self.value - self.amount
                if self.result >= 0:
                    self.value -= self.amount
                    print(f"You withdrew {self.amount}. You now have {self.value} \
in your account.")
                    break
                elif self.result < 0 and self.result >= float(-500):
                    self.value -= self.amount
                    print(f"Your withdrawn left you owning the bank, but we still \
lend you some. Your new amount in our account is {self.value}.")
                    break
                else:
                    print("We cannot allow you to withdrawn that amount of money, \
or you will be more in debt than we can allow.")
                    break
            except:
                print("Please, only type valid numbers. Try again.")
        
    def __repr__(self) -> str:
        return f"Your Checkings Account Details:\nBank {self.bank}\n\
Agency {self.agency}\nNumber {self.number}"

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.type="Savings Account"
        
    def withdrawn_money(self):
        while True:
            self.amount = input("How much would you like to withdrawn?\n")
            self.value = self.client_info.value
            try:
                self.amount = float(self.amount)
                if self.value - self.amount < 0:
                    print(f"We cannot allow you to withdrawn that amount of money \
from your savings account. You only have {self.value}.")
                    break
                else:
                    self.value -= self.amount
                    print(f"You withdrawn {self.amount} from your savings account.\
You now have {self.value}.")
                    break
            except:
                print("Please, only type valid numbers. Try again.")
                
    def __repr__(self) -> str:
        return f"Your Savings Account Details:\nBank {self.bank}\n\
Agency {self.agency}\nNumber {self.number}"

class Bank():
    def __init__(self) -> None:
        pass
    
    def client_information(self):
        username = input("What is your name?\n")
        age = input("What is your age?\n")
        self.client_info = Client(username, age)
        self.type_account = Client.open_account(self)
        self.account_info = Account()
        Account.open_account(self.account_info)
        
    def deposit_money_bank(self):
        print("You chose to deposit. We need to verify your information first.")
        Bank.authentication(self)
        if self.authenticated == True:
            self.account_value = Account.deposit_money(self.client_info)
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
            print(f"Banco escolhido {self.bank_name_auth} - Banco Determinado {self.account_info.bank}\n \
                Agencia escolhida {self.bank_agency_auth} - Agencia Determinada {self.account_info.agency}\n \
                    Conta escolhida {self.bank_account_auth} - Conta Determinada {self.account_info.number}")
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
            if self.client_info.type_of_account == "checkings":
                CheckingsAccount.withdrawn_money(self)
                self.authenticated = None
            elif self.client_info.type_of_account == "savings":
                SavingsAccount.withdrawn_money(self)
                self.authenticated = None

    def __repr__(self) -> str:
        return f"This is the return"        
#         return f"Name is {self.client_info._name} Age is {self.client_info._age} \
# Bank is {self.client_info.bank} Agency is {self.account_info.agency} Account is {self.account_info.number}"
# # Type of Account is {self.type_account.account.type} \

###################
user = Bank()
Bank.client_information(user)
Bank.deposit_money_bank(user)
Bank.withdrawn_money_bank(user)
print(user)


###################
# client_one = None
# client_one = Bank(client_one)
# client_one = Bank.Create_Client(client_one)
# client_one = Bank.Open_Bank_Account(client_one)

# username = input("What is your name?\n")
# user_age = input("What is your age?\n")
# person1 = Client(username, user_age)
# # print(person1)
# person1.open_account()
# # print()
# # print()
# # print(person1)
# # print()
# # print()
# # print(person1.account)
# # print()
# # print()
# person1.account.deposit_money()
# person1.account.withdrawn_money()
# person1.account.withdrawn_money()

"""
Arrumar 132 e 144 - Estão em comentário
"""