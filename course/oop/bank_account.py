from typing import Self, Type
from math import sqrt


class BankAccount:
    def __init__(self, name: str = "John", balance: float = 1000):
        self.name = name
        self.balance = balance

    def deposite(self, balance: float):
        self.balance += balance

    def withdraw(self, balance: float):
        if balance > self.balance:
            print(f'Vous n\'avez pas assez d\'argent sur le compte')
            return

        self.balance -= balance

    def display(self) -> str:
        return f'{self.name} - {self.balance}€'

    def transfer(self, destination: Type[Self], amount: float):
        if amount > self.balance:
            print(f'Vous n\'avez pas assez d\'argent')
            return

        self.balance -= amount
        destination.balance += amount


ju_account = BankAccount('Ju')
do_account = BankAccount('Do')

# print(ju_account.display())
# print(do_account.display())
# ju_account.deposite(5000)
# print(ju_account.display())
# ju_account.transfer(do_account, 3000)
# print(ju_account.display())
# print(do_account.display())
# do_account.withdraw(1500)
# print(do_account.display())


class SavingsAccount(BankAccount):
    def __init__(self, name="John", balance=1000, monthly_rate=0.3):
        super().__init__(name, balance)
        self.monthly_rate = monthly_rate / 100

    def set_rate(self, rate) -> None:
        self.monthly_rate = rate / 100  # Convertit le taux en décimal

    def capitalization(self, month_count:int) -> None:
        self.balance *= (1 + self.monthly_rate) ** month_count

    def __str__(self) -> str:
        return f"Name : {self.name} \nBalance : {self.balance:.2f} \nRate : {self.monthly_rate}%"
# Créez deux comptes d'épargne différents
ju_account = SavingsAccount("Ju", 1000, 0.3)
savings_account2 = SavingsAccount("Do", 500)

print(ju_account)
ju_account.capitalization(12)
print('=====================')
print(ju_account)
