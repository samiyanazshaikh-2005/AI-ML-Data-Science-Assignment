# 1. Data Types
# Q1. Find the data type of every value in a mixed list.

# my_list = [10, 20.5, "Python", True, 5+2j]

# for value in my_list:
#     print(value, ":", type(value))


# Q2. Convert a nested list into a tuple of tuples.

# my_list = [[1, 2], [3, 4], [5, 6]]

# result = tuple(tuple(i) for i in my_list)

# print(result)

# Q3. Remove all duplicate values from a mixed list while preserving the original order.
# my_list = [10, 20, "Python", 10, "Java", 20]

# result = []

# for item in my_list:
#     if item not in result:
#         result.append(item)

# print(result)
# 2. Operators
# Q4. Check whether a number is a power of 2 using operators.
# num = int(input("Enter a number: "))

# if num > 0 and (num & (num - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")
# Q5. Swap two numbers using bitwise XOR.
# a = 10
# b = 20

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("a =", a)
# print("b =", b)
# Q6. Find whether a number is divisible by both 4 and 6 using logical operators.
# num = int(input("Enter a number: "))

# if num % 4 == 0 and num % 6 == 0:
#     print("Divisible by both 4 and 6")
# else:
#     print("Not divisible by both")
# Q7. Calculate the total electricity bill using different unit rates.

# Example rates:

# First 100 units: ₹2 per unit
# Next 100 units: ₹3 per unit
# Above 200 units: ₹5 per unit
# units = int(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + (units - 100) * 3
# else:
#     bill = (100 * 2) + (100 * 3) + (units - 200) * 5

# print("Total bill =", bill)
# 3. Conditional Statements
# Q8. Check whether three sides can form a triangle.
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     print("Valid Triangle")
# else:
#     print("Not a Triangle")
# Q9. Determine the type of triangle (Equilateral, Isosceles, Scalene).
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Equilateral Triangle")
#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")
#     else:
#         print("Scalene Triangle")
# else:
#     print("Invalid Triangle")
# Q10. Create a simple ATM menu (Withdraw, Deposit, Balance).
# balance = 5000

# while True:
#     print("\n1. Withdraw")
#     print("2. Deposit")
#     print("3. Balance")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         amount = int(input("Enter amount: "))
#         if 0 < amount <= balance:
#             balance -= amount
#             print("Withdrawal successful")
#         else:
#             print("Invalid amount")

#     elif choice == 2:
#         amount = int(input("Enter amount: "))
#         if amount > 0:
#             balance += amount
#             print("Deposit successful")
#         else:
#             print("Invalid amount")

#     elif choice == 3:
#         print("Balance =", balance)

#     elif choice == 4:
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice")
# Q11. Calculate income tax based on different tax slabs.

# Example slabs (illustrative):

# Income up to ₹2,50,000: No tax
# ₹2,50,001 to ₹5,00,000: 5%
# ₹5,00,001 to ₹10,00,000: 20%
# Above ₹10,00,000: 30%
# income = float(input("Enter annual income: "))

# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = (income - 250000) * 0.05
# elif income <= 1000000:
#     tax = (250000 * 0.05) + (income - 500000) * 0.20
# else:
#     tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

# print("Income Tax =", tax)

# Note: These are example slabs for programming practice, not current Indian tax rules.


# Q12. Create a menu-driven calculator using if-elif.

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     print("Result =", a + b)
# elif choice == 2:
#     print("Result =", a - b)
# elif choice == 3:
#     print("Result =", a * b)
# elif choice == 4:
#     if b != 0:
#         print("Result =", a / b)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid choice")
# 4. Loops

# Q13. Print all prime numbers between 1 and n.

# n = int(input("Enter n: "))

# for num in range(2, n + 1):
#     prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num)

# Q14. Find the factorial of a number using a loop.

# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial =", fact)

# Q15. Print the Fibonacci series up to n terms.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# Q16. Check whether a number is an Armstrong number.

# num = int(input("Enter a number: "))

# temp = num
# power = len(str(num))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total += digit ** power
#     temp //= 10

# if total == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

# Q17. Reverse a number and check if it is a palindrome.

# num = int(input("Enter a number: "))

# temp = num
# reverse = 0

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp //= 10

# print("Reverse =", reverse)

# if num == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome")

# Q18. Find the Greatest Common Divisor (GCD) of two numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD =", a)

# 5. Functions

# Q19. Write a function to check if a string is a palindrome.
# def palindrome(text):
#     if text == text[::-1]:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"

# word = input("Enter a string: ")

# print(palindrome(word))

# Q20. Write a function to count vowels and consonants in a string.

# def count_letters(text):
#     vowels = 0
#     consonants = 0

#     for ch in text.lower():
#         if ch.isalpha():
#             if ch in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     print("Vowels =", vowels)
#     print("Consonants =", consonants)

# text = input("Enter a string: ")

# count_letters(text)

# Q21. Create a function to calculate simple and compound interest.

# def interest(p, r, t):
#     si = (p * r * t) / 100
#     ci = p * (1 + r / 100) ** t - p

#     print("Simple Interest =", si)
#     print("Compound Interest =", ci)

# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))

# interest(p, r, t)

# Q22. Write a function to return all factors of a number.

# def factors(num):
#     result = []

#     for i in range(1, num + 1):
#         if num % i == 0:
#             result.append(i)

#     return result

# n = int(input("Enter a number: "))

# print("Factors =", factors(n))

# Q23. Write a function to find the second-largest number in a list.

# def second_largest(numbers):
#     unique = list(set(numbers))
#     unique.sort()

#     if len(unique) < 2:
#         return "Second largest does not exist"

#     return unique[-2]

# numbers = [10, 20, 30, 40, 50]

# print("Second Largest =", second_largest(numbers))

# 6. Lists

# Q24. Merge two lists without duplicates.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# result = []

# for item in list1 + list2:
#     if item not in result:
#         result.append(item)

# print(result)

# Q25. Find the second-largest and second-smallest elements.

# numbers = [10, 20, 30, 40, 50]

# unique = sorted(set(numbers))

# if len(unique) >= 2:
#     print("Second Smallest =", unique[1])
#     print("Second Largest =", unique[-2])
# else:
#     print("Not enough unique elements")

# Q26. Rotate a list to the left by k positions.

# numbers = [1, 2, 3, 4, 5]

# k = int(input("Enter rotation: "))

# k = k % len(numbers)

# result = numbers[k:] + numbers[:k]

# print(result)

# Q27. Separate even and odd numbers into two lists.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even Numbers =", even)
# print("Odd Numbers =", odd)

# Q28. Find the common elements between two lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)

# print("Common Elements =", common)

# 7. Tuples & Sets

# Q29. Count the frequency of each element in a tuple.
# my_tuple = (1, 2, 3, 2, 1, 4, 2)

# for item in set(my_tuple):
#     print(item, ":", my_tuple.count(item))

# Q30. Find the union, intersection, and difference of two sets.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print("Union =", set1 | set2)
# print("Intersection =", set1 & set2)
# print("Difference =", set1 - set2)

# Q31. Check whether one set is a subset of another.

# set1 = {1, 2}
# set2 = {1, 2, 3, 4, 5}

# if set1.issubset(set2):
#     print("Subset")
# else:
#     print("Not a Subset")
# 8. Dictionaries

# Q32. Count the frequency of words in a sentence.

# sentence = input("Enter a sentence: ")

# words = sentence.lower().split()

# frequency = {}

# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1

# print(frequency)

# Q33. Create a dictionary from two lists (keys and values).

# keys = ["name", "age", "city"]
# values = ["Sam", 21, "Jalgaon"]

# result = dict(zip(keys, values))

# print(result)

# Q34. Sort a dictionary by its values.

# my_dict = {
#     "A": 50,
#     "B": 20,
#     "C": 80,
#     "D": 40
# }

# result = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# print(result)

# 9. File Handling

# Q35. Read a text file and count the number of lines, words, and characters.
# with open("sample.txt", "r") as file:
#     text = file.read()

# lines = text.splitlines()
# words = text.split()
# characters = len(text)

# print("Lines =", len(lines))
# print("Words =", len(words))
# print("Characters =", characters)

# Q36. Copy only the even-numbered lines from one file to another.

# with open("input.txt", "r") as file:
#     lines = file.readlines()

# with open("output.txt", "w") as file:
#     for i in range(1, len(lines), 2):
#         file.write(lines[i])

# print("Even-numbered lines copied")

# 10. Exception Handling

# Q37. Handle invalid integer input using try-except.
# try:
#     num = int(input("Enter an integer: "))
#     print("Number =", num)

# except ValueError:
#     print("Invalid input! Please enter an integer.")

# Q38. Handle file-not-found errors while reading a file.

# try:
#     with open("sample.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found!")

# 11. Modules

# Q39. Create a random password generator using the random and string modules.

# import random
# import string

# length = int(input("Enter password length: "))

# characters = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(length):
#     password += random.choice(characters)

# print("Generated Password =", password)

# Q40. Use the datetime module to calculate the number of days between two dates.

# from datetime import datetime

# date1 = input("Enter first date (DD-MM-YYYY): ")
# date2 = input("Enter second date (DD-MM-YYYY): ")

# d1 = datetime.strptime(date1, "%d-%m-%Y")
# d2 = datetime.strptime(date2, "%d-%m-%Y")

# difference = abs((d2 - d1).days)

# print("Difference =", difference, "days")