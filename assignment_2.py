#Que 1: Even or Odd Function Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

# def is_even(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Taking input from the user
# num = int(input("Enter a number: "))

# # Calling the function
# print(is_even(num))

#Que 2:Largest of Two Numbers Write a function largest(a, b) that returns the larger number.

# def largest(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# # Taking input from the user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# # Calling the function
# print("Largest number is:", largest(a, b))

#Que 3:Print Numbers Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)

# # Taking input
# n = int(input("Enter a number: "))

# # Calling the function
# print_numbers(n)

#Que 4:Write a function sum_n(n) that returns the sum of numbers from 1 to n.


# def sum_n(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#     return total

# # Taking input
# n = int(input("Enter a number: "))

# # Calling the function
# print("Sum is:", sum_n(n))

#Que 5: Write a function table(n) that prints the multiplication table of n from 1 to 10.

# def table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)

# # Taking input
# n = int(input("Enter a number: "))

# # Calling the function
# table(n)

#Que 6: Write a function that takes a list and returns how many even numbers it contains.

# def count_even(numbers):
#     count = 0
#     for n in numbers:
#         if n % 2 == 0:
#             count += 1
#     return count

# # Calling the function
# print(count_even([1, 2, 3, 4, 6]))

#Que 7:Without using max(), write a function that returns the largest number in a list

# def largest(numbers):
#     big = numbers[0]

#     for n in numbers:
#         if n > big:
#             big = n

#     return big

#  Calling the function
# print(largest([10, 25, 5, 40, 15]))

#Que 8:Write a function that prints numbers from 1 to 100
# def print_numbers():
#     for i in range(1, 101):
#         print(i)

#  Calling the function
# print_numbers()

#Que 9:If divisible by 3, print "Fizz"
# def fizz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0:
#             print("Fizz")
#         else:
#             print(i)

# # Calling the function
# fizz(15)

#Que 10:If divisible by 5, print "Buzz".
# def buzz(n):
#     for i in range(1, n + 1):
#         if i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

#  Calling the function
# buzz(15)

#Que 11:If divisible by both, print "FizzBuzz".
# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# # Calling the function
# fizzbuzz(15)

#Que 12:Write a function that returns True if a string is a palindrome.
# def is_palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# # Taking input
# word = input("Enter a string: ")

# # Calling the function
# print(is_palindrome(word))

#Que 13:Write a function that counts the vowels in a string.
# def count_vowels(s):
#     count = 0
#     for ch in s:
#         if ch in "aeiouAEIOU":
#             count += 1
#     return count

# # Taking input
# word = input("Enter a string: ")

# # Calling the function
# print("Number of vowels:", count_vowels(word))

#Que 14:Write a function that returns the second largest number in a list without using sort().
# def second_largest(numbers):
#     largest = numbers[0]
#     second = None

#     for n in numbers:
#         if n > largest:
#             second = largest
#             largest = n
#         elif n != largest:
#             if second is None or n > second:
#                 second = n

#     return second

# # Calling the function
# print(second_largest([10, 20, 5, 40, 30]))

#Que 15:Generate a random number between 1 and 10.

# import random

# def random_number():
#     return random.randint(1, 10)

# # Calling the function
# print(random_number())

#Que:Keep asking the user to guess until they get it right.
# import random

# def guessing_game():
#     number = random.randint(1, 10)

#     while True:
#         guess = int(input("Guess a number between 1 and 10: "))

#         if guess == number:
#             print("Correct! You guessed it.")
#             break
#         else:
#             print("Wrong guess! Try again.")

# # Calling the function
# guessing_game()

#Que:Use a loop, conditionals, and functions.
# import random

# def guessing_game():
#     number = random.randint(1, 10)

#     while True:
#         guess = int(input("Guess a number between 1 and 10: "))

#         if guess == number:
#             print("Correct! You guessed it.")
#             break
#         elif guess < number:
#             print("Too low! Try again.")
#         else:
#             print("Too high! Try again.")

# # Calling the function
# guessing_game()

#Que:  Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"

# # Taking input
# marks = int(input("Enter your marks: "))

# # Calling the function
# print("Grade:", grade(marks))
