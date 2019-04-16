# # A Bank Account
#
#  `BankAccount` class, which behaves like that:
#
# ## Basic BankAccount usage
#
# Our `BankAccount` will have the following methods:
#
# * Constructor takes a `name` for the account, initial `balance` and a `currency`.
#   If `balance` is negative number, raise a `ValueError` error.
# * `deposit(amount)` - deposits money of `amount` to your balance.
#   If `amount` is negative number, raise a `ValueError` error.
# * `balance()` - returns the current balance
# * `withdraw(amount)` - takes `amount` money from the account. Returns `True` if it was successful. Otherwise, `False`
# * `__str__` should return: `"Bank account for {name} with balance of {amount}{currency}"`
# * `__int__` should return the balance of the `BankAccount`
# * `history()` - returns a list of strings, that represent the history of the bank account. Check examples below for more information.
#
#
# ```python
# >>> account = BankAccount("Rado", 0, "$")
# >>> print(account)
# 'Bank account for Rado with balance of 0$'
# >>> account.deposit(1000)
# >>> account.balance()
# 1000
# >>> str(account)
# 'Bank account for Rado with balance of 1000$'
# >>> int(account)
# 1000
# >>> account.history()
# ['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$']
# >>> account.withdraw(500)
# True
# >>> account.balance()
# 500
# >>> account.history()
# ['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$', '500$ was withdrawn', 'Balance check -> 500$']
# >>> account.withdraw(1000)
# False
# >>> account.balance()
# 500
# >>> account.history()
# ['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$', '500$ was withdrawn', 'Balance check -> 500$',
#  'Withdraw for 1000$ failed.', 'Balance check -> 500$']
# ```
#
# ## Extra usage
#
# **NOTE:** for this portion of the task there are no tests to validate the
# correct operation!!! In the next module we will learn about unit tests and
# revisit this!
#
# Also, we should be able to transfer money from one account to another:
#
# * `transfer_to(account, amount)` - transfers `amount` to `account` if they both have the same currencies! Returns `True` if successful.
#
# ```python
# >>> rado = BankAccount("Rado", 1000, "BGN")
# >>> ivo = BankAccount("Ivo", 0, "BGN")
# >>> rado.transfer_to(ivo, 500)
# True
# >>> rado.balance()
# 500
# >>> ivo.balance()
# 500
# >>> rado.history()
# ['Account was created', 'Transfer to Ivo for 500BGN', 'Balance check -> 500BGN']
# >>> ivo.history()
# ['Account was created', 'Transfer from Rado for 500BGN', 'Balance check -> 500BGN']
# ```


class BankAccount:

    def __init__(self, name, balance, currency):

        if name == "":
            raise ValueError

        self.name = name

        if balance < 0:
            raise ValueError("Negative balance")

        self._balance = balance  # Property should be named balance and method should be Balance, but a rewrite of test.py will be needed

        if currency == "":
            raise ValueError

        self.currency = currency
        self.log = ["Account was created"]

    def deposit(self, amount, to_add_to_history= True):

        if amount <= 0:
            raise ValueError("Negative amount")

        self._balance += amount
        if to_add_to_history:
            self.log.append("Deposited {0}$".format(amount))

    def balance(self):

        self.log.append("Balance check -> {0}$".format(self._balance))

        return self._balance

    def withdraw(self, amount, to_add_to_history = True):
        if amount > self._balance:
            if to_add_to_history:
                self.log.append("Withdraw for {0}$ failed.".format(amount))
                return False
        else:
            if to_add_to_history:
                self.log.append("{0}$ was withdrawn".format(amount))
            self._balance -= amount

            return True

    def __str__(self):
        return "Bank account for {0} with balance of {1}{2}".format(self.name, self._balance, self.currency)

    def __int__(self):
        self.log.append("__int__ check -> {0}$".format(self._balance))

        return self._balance

    def history(self):

        return self.log
    #
    # def transfer_to(self, account, amount):
    #     if account.currency != self.currency:
    #         raise TypeError
    #     if amount < 0:
    #         raise ValueError
    #     else:
    #         if self.balance() < amount:
    #             raise ValueError("Not enough money for transfer")
    #         else:
    #             self._balance -= amount
    #             account._balance += amount
    #             self.log.append("Transfer to {0} for {1}{2}".format(account.name, amount, account.currency))
    #             account.log.append("Transfer from {0} for {1}{2}".format(self.name, amount, account.currency))

    def transfer_to(self, account, amount):
        if account.currency != self.currency:
            raise TypeError
        if amount < 0:
            raise ValueError
        else:
            check_for_balance = self.withdraw(amount, False)
            if check_for_balance:
                account.deposit(amount, False)
            else:
                raise ValueError

            self.log.append("Transfer to {0} for {1}{2}".format(account.name, amount, account.currency))
            account.log.append("Transfer from {0} for {1}{2}".format(self.name, amount, account.currency))

        return True
