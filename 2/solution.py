# Implement a function num_add(a, b) which adds two numbers together

def num_add(a, b):
    return a + b


# Implement a function num_sub(a, b) which subtracts two numbers

def num_sub(a, b):
    return a - b


# Implement a function num_mul(a, b) which multiplies two numbers

def num_mul(a, b):
    return a * b


# Implement a function num_div(a, b) which divides the two numbers

def num_div(a, b):
    return a / b


# Implement a function num_floor(a, b) which implements floor division

def num_floor(a, b):
    return a // b


# Implement a function num_rem(a, b) which implements remainder division

def num_rem(a, b):
    return a % b


# Define boolean constant IS_TRUE

IS_TRUE = True

# Define boolean constant IS_FALSE

IS_FALSE = False

# Define the PANCAKE_INGREDIENTS dictionary to include the following keys and values
# flour - 2
# eggs - 4
# milk - 200
# butter - False
# salt - 0.001

PANCAKE_INGREDIENTS = {"flour": 2, "eggs": 4, "milk": 200, "butter": False, "salt": 0.001}


# Implement a function ingredient_exists(ingr, dict) which returns boolean if the ingredient ingr exists in the dictionary `dict

def ingredient_exists(ingr, dict):
    return ingr in dict


# Implement a function fatten_pancakes(dict) which returns a dictionary. The return value contains the pancake ingredients
#  where eggs == 6 and butter == True. NOTE: don't change the
# PANCAKE_INGREDIENTS constant! Use dict.copy() method!

def fatten_pancakes(dict=PANCAKE_INGREDIENTS):
    temp = dict.copy()
    temp.update(eggs=6, butter=True)

    return temp


# Implement a function add_sugar(dict) which adds 'sugar' to the list of ingredients and returns a new dictionary

def add_sugar(dict=PANCAKE_INGREDIENTS):
    temp = dict.copy()
    temp.update({"sugar": 1})

    return temp


# Implement a function remove_salt(dict) which removes 'salt' from the list of igredients and returns a new dictionary

def remove_salt(dict):
    dict.pop("salt")

    return dict.copy()


# Define a list called FIBONACCI_NUMBERS which contains the first 12 Fibonacci numbers:
#
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


# Implement a function add_fibonacci(lst) which extends the list of numbers with the next Fibonacci number

def add_fibonacci(lst):
    n = len(lst)
    lst.append(lst[n - 2] + lst[n - 1])

    return lst


# Implement a function fib_exists(lst, n) which returns boolean. The function checks if the number n exists in the Fibonacci sequence lst

def fib_exists(lst, n):

    return n in lst


# Implement a function which_fib(lst, n) which returns integer. This is the index of the number n inside the sequence lst counting from 1.

def which_fib(lst, n):
    lst.insert(0, 0)

    return lst[n]

# if __name__ == '__main__':
#     print(which_fib(FIBONACCI_NUMBERS,99999))