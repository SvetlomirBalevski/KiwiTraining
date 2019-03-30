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

def nim_div(a, b):
    return a / b


# Implement a function num_floor(a, b) which implements floor division

def num_floor(a, b):
    return a // b

# Implement a function num_rem(a, b) which implements remainder division

def num_rem(a,b):
    return a%b

# Define boolean constant IS_TRUE

IS_TRUE = bool

# Define boolean constant IS_FALSE

IS_FALSE = bool

# Define the PANCAKE_INGREDIENTS dictionary to include the following keys and values
# flour - 2
# eggs - 4
# milk - 200
# butter - False
# salt - 0.001

PANCAKE_INGREDIENTS = {"flour" : 2, "eggs" : 4, "milk" : 200, "butter" : False, "salt":0.001}


# Implement a function ingredient_exists(ingr, dict) which returns boolean if the ingredient ingr exists in the dictionary `dict

def ingredient_exists(ingr, dict):
    return ingr in dict

# Implement a function fatten_pancakes(dict) which returns a dictionary. The return value contains the pancake ingredients where eggs == 6 and butter == True. NOTE: do
# n't change the PANCAKE_INGREDIENTS constant! Use dict.copy() method!



# Implement a function add_sugar(dict) which adds 'sugar' to the list of ingredients and returns a new dictionary
#
# Implement a function remove_salt(dict) which removes 'salt' from the list of igredients and returns a new dictionary
#
# Define a list called FIBONACCI_NUMBERS which contains the first 12 Fibonacci numbers:
#
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
#
# Implement a function add_fibonacci(lst) which extends the list of numbers with the next Fibonacci number
#
# Implement a function fib_exists(lst, n) which returns boolean. The function checks if the number n exists in the Fibonacci sequence lst
#
# Implement a function which_fib(lst, n) which returns integer. This is the index of the number n inside the sequence lst counting from 1.

# if __name__ == '__main__':
#     print(ingredient_exists("floor",PANCAKE_INGREDIENTS))
#     print(ingredient_exists("Floor",PANCAKE_INGREDIENTS))
