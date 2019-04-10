# ## The Bill class
#
# Create a class, called `Bill` which takes one parameter to its constructor - the `amount` of the bill - an integer.
#
# This class will only have **dunders** so you won't be afraid of them anymore!
#
# The class should implement:
#
# * `__str__` and `__repr__`
# * `__int__`
# * `__eq__` and `__hash__`
# * If amount is negative number, raise an `ValueError` error.
# * If type of amount isn't `int`, raise an `TypeError` error.
# * **HINT:** raising exceptions is done with `raise ExceptionType("message")`
# * See this SO thread about the difference between `__str__` and `__repr__`
# http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
#
# Here is an example usage:
#
# ```python
# from solution import Bill
#
# a = Bill(10)
# b = Bill(5)
# c = Bill(10)
#
# int(a) # 10
# str(a) # "A 10$ bill"
# print(a) # A 10$ bill
#
# a == b # False
# a == c # True
#
# money_holder = {}
#
# money_holder[a] = 1 # We have one 10$ bill
#
# if c in money_holder:
#     money_holder[c] += 1
#
# print(money_holder) # { "A 10$ bill": 2 }
# ```

class Bill:


    def __init__(self, ammount):
        self.ammount = ammount

        if type(ammount) is not int:
            raise TypeError

        if ammount < 0:
            raise ValueError

    def __int__(self):
        return self.ammount

    def __eq__(self, other):
        if self.ammount == other.ammount:
            return True
        else:
            return False

    def __repr__(self):
        return "A {0}$ bill".format(self.ammount)

#
# ## The BatchBill class
#
# We are going to implement a class, which represents more than one bill. A `BatchBill`!
#
# The class takes a list of `Bills` as the single constructor argument.
#
# The class should have the following methods:
#
# * `__len__(self)` - returns the number of `Bills` in the batch
# * `total(self)` - returns the total amount of all `Bills` in the batch
#
# We should be able to iterate the `BatchBill` class with a for-loop.
#
# Here is an example:
#
# ```python
# from solution import Bill, BillBatch
#
# values = [10, 20, 50, 100]
# bills = [Bill(value) for value in values]
#
# batch = BillBatch(bills)
#
# for bill in batch:
#     print(bill)
#
# # A 10$ bill
# # A 20$ bill
# # A 50$ bill
# # A 100$ bill
# ```
#
# In order to do that, you need to implement the following method:
#
# ```python
# def __getitem__(self, index):
#     pass
# ```
#

class BatchBill:
    def __init__(self, Bills):
        self.Bills = Bills


# ## The CashDesk classs
#
# Finally, implement a `CashDesk` class, which has the following methods:
#
# * `take_money(money)`, where `money` can be either `Bill` or `BatchBill` class
# * `total()` - returns the total amount of money currenly in the desk
# * `inspect()` - returns a table representation of the money - for each bill, how many copies of it we have.
#
# For example:
#
# ```python
# from solution import Bill, BillBatch, CashDesk
#
# values = [10, 20, 50, 100, 100, 100]
# bills = [Bill(value) for value in values]
#
# batch = BillBatch(bills)
#
# desk = CashDesk()
#
# desk.take_money(batch)
# desk.take_money(Bill(10))
#
# print(desk.total()) # 390
# desk.inspect()
#
# # We have a total of 390$ in the desk
# # We have the following count of bills, sorted in ascending order:
# # 10$ bills - 2
# # 20$ bills - 1
# # 50$ bills - 1
# # 100$ bills - 3

class CashDesk:
    def __init__(self):
        pass

if __name__ == '__main__':
    t = Bill (5)
    print(int(t))