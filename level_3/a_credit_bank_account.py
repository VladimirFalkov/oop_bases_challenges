"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount

    def __str__(self) -> str:
        return f"Mister {self.owner_full_name} has ${self.balance} on your account"


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == "__main__":
    account_1 = BankAccount("Rothschild", 2000)
    print(account_1)
    account_1.increase_balance(100)
    print(account_1)
    account_1.decrease_balance(59)
    print(account_1)
    account_2 = CreditAccount("Buffett", 1001.99)
    print(account_2)
    account_2.increase_balance(100)
    print(account_2)
    account_2.decrease_balance(102)
    print(account_2)
    print(account_2.is_eligible_for_credit())
