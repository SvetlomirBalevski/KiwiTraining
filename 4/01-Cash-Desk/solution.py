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

import collections


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

    def __hash__(self):
        return self.ammount

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

    def __len__(self):
        return len(self.Bills)

    def total(self):
        total_bills = 0

        for bill in self.Bills:
            total_bills += bill.ammount

        return total_bills

    def __getitem__(self, index):
        return self.Bills[index]


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
        self.inside = {}

    def take_money(self, money):
        if type(money) is Bill and money in self.inside:
            self.inside[money.ammount] +=1

        elif type(money) is Bill:
            self.inside.update({money.ammount : 1})

        elif type(money) is BatchBill:
            for single_bill in money:
                if single_bill.ammount in self.inside:
                    self.inside[single_bill.ammount]+=1
                else:
                    self.inside.update({single_bill.ammount : 1})

    def total(self):
        total = 0
        for value in self.inside:
            total += self.inside[value] * value
        return total

    def inspect(self):
        response_first_line = "We have a total of {0}$ in the desk".format(self.total())
        response_second_line = "We have the following count of bills, sorted in ascending order:"
        sorted_inside = collections.OrderedDict(sorted(self.inside.items()))

        response_third_line=""

        for i in sorted_inside:
            response_third_line += "{0}$ bills - {1}\n".format(i, sorted_inside[i])

        new_line = "\n"

        response_third_line = response_third_line[:-1] # remove last new line from the string

        return response_first_line + new_line+ response_second_line + new_line + response_third_line
