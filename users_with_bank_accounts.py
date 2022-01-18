
class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount <= 0:
            print("Insuffiecient funds: Charging a $5 fee.")
            self.balance = self.balance - 5 - amount
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "accnt1": BankAccount(int_rate=0.05, balance=1000),
            "accnt2": BankAccount(int_rate=0.02, balance=10000)
        }

    def display_user_balance(self):
        print(
            f"User: {self.name}, Account 1 Balance: {self.account['accnt1'].display_account_info()}")
        print(
            f"User: {self.name}, Account 2 Balance: {self.account['accnt2'].display_account_info()}")
        return self

    def make_transfer(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()


sue = User("Sue")

sue.account['accnt1'].deposit(100)
sue.display_user_balance()
