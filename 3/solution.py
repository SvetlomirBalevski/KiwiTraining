# Sum of all digits of a number
#
#     Given an integer, implement a function, called sum_of_digits(n) that calculates the sum of n's digits.
#
#     If a negative number is given, our function should work as if it was positive.
#
#     Keep in mind that in Python, there is a special operator for integer division!
#
#       >>> 5 / 2
#       2.5
#       >>> 5 // 2
#       2
#       >>> 5 % 2
#       1
#
#     Function signature
#
#       def sum_of_digits(n):
#           pass
# 121 / 10 = 12 . reminder =1 ; 12 /10 = 1, reminder 2, 1 / 10 = 0, reminder = 1
def sum_of_digits(n):
    summary = 0
    n = -(n) if n < 0 else n
    while n != 0:
        summary += n % 10
        n = n // 10
    return summary


# Turn a number into a list of digits
#
#     Implement a function, called to_digits(n), which takes an integer n and returns a list, containing the digits of n.
#
#     Signature
#
#       def to_digits(n):
#           pass

def to_digits(n):
    digits = []
    n = -(n) if n < 0 else n
    while n != 0:
        digits.append(n%10)
        n = n // 10
    digits.reverse()
    return digits

# Turn a list of digits into a number
#
#     Implement a function, called to_number(digits), which takes a list of integers - digits and returns the number, containing those digits.
#
#     Signature
#
#       def to_number(digits):
#           pass
#
# Vowels in a string
#
#     Implement a function, called count_vowels(str), which returns the count of all vowels in the string str. Count uppercase vowels as well! The English vowels are aeiouy.
#
#     Signature
#
#       def count_vowels(str):
#           pass

def count_vowels(str):
    str = str.lower()
    sum_of_vowels = 0
    vowels = "aeiouy"
    for letter in str:

        if letter in vowels:
            sum_of_vowels += 1

    return sum_of_vowels

# Consonants in a string
#
#     Implement a function, called count_consonants(str), which returns the count of all consonants in the string str. Count uppercase consonants as well! The English consonants are bcdfghjklmnpqrstvwxz.
#
#     Signature
#
#       def count_consonants(str):
#           pass

def count_consonants(str):
    str = str.lower()
    sum_of_consonants = 0
    consonants = "bcdfghjklmnpqrstvwxz"

    for letter in str:
        if letter in consonants:
            sum_of_consonants +=1

    return sum_of_consonants

# Prime Number
#
#     Check if a given number is prime in prime_number(number) and return boolean result.
#
#     For the purposes of this task consider 1 to be a prime number as well.
#
#     Hint:
#
#       >>> 5 % 2
#       1
#
#     Signature
#
#       def prime_number(n):
#           pass
#
# Factorial Digits
#
#     Implement a function fact_digits(n), that takes an integer and returns the sum of the factorials of each digit of n.
#
#     For example, if n = 145, we want 1! + 4! + 5!
#
#     Signature
#
#       def fact_digits(n):
#           pass
#
#     Hint - use the functions that you have defined previously. What other functions do you need ?
#
# First nth members of Fibonacci
#
#     Implement a function, called fibonacci(n) that returns a list with the first n members of the Fibonacci sequence.
#
#     Signature
#
#       def fibonacci(n):
#           pass
#
# Fibonacci number
#
#     Implement a function, called fib_number(n), which takes an integer n and returns a number, which is formed by concatenating the first n Fibonacci numbers. For example, if n = 3, the result is 112.
#
#     Signature
#
#       def fib_number(n):
#           pass
#
#     Hint - use the functions that you have defined previously. What other functions do you need?
#
# Palindrome
#
#     Implement a function, called palindrome(obj), which takes a number or a string and checks if it is a representation is a palindrome. For example, the integer 121 and the string "kapak" are palindromes. The function should work with both.
#
#     Hint - check Python's str() function
#
#     Signature
#
#       def palindrome(n):
#           pass
#
# Char Histogram
#
#     Implement a funcion, called char_histogram(string), which takes a string and returns a dictionary, where each key is a character from string and its value is the number of occurrences of that char in string.
#
#     Signature
#
#       def char_histogram(string):
#           pass
#
# TIP: Use test.py to validate your solution is correct.

if __name__ == '__main__':
    count_vowels("Python")