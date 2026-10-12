# 1) Check if a number is positive, negative, or zero.
# a=int(input("enter a number:"))
# if(a>0):
#     print("Number is positive")
# elif(a<0):
#     print("Number is negative")
# else:
#     print("Number is zero")

# 2) Check whether a number is even or odd.
# b=int(input("Enter a number : "))
# if b % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# 3) Find the greater of two numbers.
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2 : "))
# if num1 > num2:
#     print("num1 is greater then num2")
# else:
#     print("num2 is greater than num1")

# 4) Find the greatest of three numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Greatest number is:", a)
# elif b >= a and b >= c:
#     print("Greatest number is:", b)
# else:
#     print("Greatest number is:", c)

# 5) Check if a person is eligible to vote (age ≥ 18).
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# 6) Check whether a year is a leap year.
# year = int(input("Enter a year: "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# 7)Check if a character is a vowel or consonant.
# ch = input("Enter a character: ").lower()
# if ch in "aeiou" and len(ch) == 1:
#     print("Vowel")
# elif ch.isalpha() and len(ch) == 1:
#     print("Consonant")
# else:
#     print("Enter a single alphabet")

#8)Check whether a number is divisible by 5 and 11.
# num = int(input("Enter a number: "))

# if num % 5 == 0 and num % 11 == 0:
#     print("Number is divisible by 5 and 11")
# else:
#     print("Number is not divisible by 5 and 11")

# 9) Check if a number is a multiple of both 3 and 7.
# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 7 == 0:
#     print("Multiple of both 3 and 7")
# else:
#     print("Not a multiple of both 3 and 7")

#10) Assign grades based on marks:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F

# marks = int(input("Enter your marks: "))

# if marks < 0 or marks > 100:
#     print("Invalid marks")
# elif marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

# 11) Check if a character is uppercase or lowercase
# ch = input("Enter a character: ")

# if ch.isupper():
#     print("Uppercase")
# elif ch.islower():
#     print("Lowercase")
# else:
#     print("Not an alphabet")

#12) Find whether the entered alphabet is a vowel using if-elif.
# ch = input("Enter an alphabet: ").lower()

# if ch == 'a':
#     print("Vowel")
# elif ch == 'e':
#     print("Vowel")
# elif ch == 'i':
#     print("Vowel")
# elif ch == 'o':
#     print("Vowel")
# elif ch == 'u':
#     print("Vowel")
# else:
#     print("Consonant")

#13) Check if three sides can form a triangle.
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
#     print("Triangle can be formed")
# else:
#     print("Triangle cannot be formed")

# 14) Determine the type of triangle (Equilateral, Isosceles, Scalene).
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
#     print("Invalid triangle")
# elif a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

# 15) Find the largest among four numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a >= b and a >= c and a >= d:
#     print("Largest number:", a)
# elif b >= a and b >= c and b >= d:
#     print("Largest number:", b)
# elif c >= a and c >= b and c >= d:
#     print("Largest number:", c)
# else:
#     print("Largest number:", d)

#16) Check whether a number is a three-digit number.
# num = int(input("Enter a number: "))

# if 100 <= abs(num) <= 999:
#     print("Three-digit number")
# else:
#     print("Not a three-digit number")

# 17) Calculate electricity bill using slab rates
# units = int(input("Enter electricity units: "))

# if units < 0:
#     print("Invalid units")
# elif units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + (units - 100) * 7
# else:
#     bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# if units >= 0:
#     print("Electricity Bill: ₹", bill)

# 18) Calculate income tax based on income slabs
# income = float(input("Enter your annual income: "))

# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = income * 0.05
# elif income <= 1000000:
#     tax = income * 0.20
# else:
#     tax = income * 0.30

# print("Income Tax: ₹", tax)

#19) Check if a student passes (minimum 35 marks in each subject).
# s1 = int(input("Enter marks in subject 1: "))
# s2 = int(input("Enter marks in subject 2: "))
# s3 = int(input("Enter marks in subject 3: "))

# if s1 >= 35 and s2 >= 35 and s3 >= 35:
#     print("Student Passed")
# else:
#     print("Student Failed")

#20) Find whether a number is within a given range.
# num = int(input("Enter a number: "))
# start = int(input("Enter range start: "))
# end = int(input("Enter range end: "))

# if start <= num <= end:
#     print("Number is within the range")
# else:
#     print("Number is outside the range")

# 21) Build a simple calculator using if-elif-else (+, -, *, /).
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == '+':
#     print("Result:", a + b)
# elif op == '-':
#     print("Result:", a - b)
# elif op == '*':
#     print("Result:", a * b)
# elif op == '/':
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid operator")

# 22) Check if a year is a century leap year.
# year = int(input("Enter a year: "))

# if year % 100 == 0 and year % 400 == 0:
#     print("Century Leap Year")
# elif year % 100 == 0:
#     print("Century Year but not a Leap Year")
# else:
#     print("Not a Century Year")

#23) Determine the season based on the month number.
# month = int(input("Enter month number (1-12): "))

# if month in [3, 4, 5]:
#     print("Summer")
# elif month in [6, 7, 8, 9]:
#     print("Rainy Season")
# elif month in [10, 11]:
#     print("Autumn")
# elif month in [12, 1, 2]:
#     print("Winter")
# else:
#     print("Invalid month number")

# 24) Find the number of days in a month.
# month = int(input("Enter month number (1-12): "))
# year = int(input("Enter year: "))

# if month == 2:
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         print("29 days")
#     else:
#         print("28 days")
# elif month in [4, 6, 9, 11]:
#     print("30 days")
# elif 1 <= month <= 12:
#     print("31 days")
# else:
#     print("Invalid month number")

# 25) Check whether a password meets minimum conditions (length, digits, etc.).
# password = input("Enter your password: ")

# if (len(password) >= 8 and
#     any(ch.isdigit() for ch in password) and
#     any(ch.isupper() for ch in password) and
#     any(ch.islower() for ch in password) and
#     any(ch in "!@#$%^&*" for ch in password)):
#     print("Valid Password")
# else:
#     print("Invalid Password")

#26) Determine ticket price based on age category.
# age = int(input("Enter your age: "))

# if age < 5:
#     price = 0
# elif age <= 12:
#     price = 100
# elif age <= 59:
#     price = 200
# else:
#     price = 150

# print("Ticket Price: ₹", price)

# 27) Calculate discount based on purchase amount.
# amount = float(input("Enter purchase amount: "))

# if amount >= 5000:
#     discount = amount * 0.20
# elif amount >= 3000:
#     discount = amount * 0.10
# elif amount >= 1000:
#     discount = amount * 0.05
# else:
#     discount = 0

# final_amount = amount - discount

# print("Discount: ₹", discount)
# print("Final Amount: ₹", final_amount)

#28) Check if a person is eligible for a driving license (age and eyesight condition)
# age = int(input("Enter your age: "))
# eyesight = input("Is your eyesight normal? (yes/no): ").lower()

# if age >= 18 and eyesight == "yes":
#     print("Eligible for driving license")
# else:
#     print("Not eligible for driving license")

#29) Create a login system with username and password validation
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "12345":
#     print("Login successful")
# else:
#     print("Invalid username or password")

# 30) Create a menu-driven program using if-elif-else with options like:
# Addition
# Subtraction
# Multiplication
# Division
# Exit

# while True:
#     print("\n1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 5:
#         print("Exiting program...")
#         break

#     elif choice >= 1 and choice <= 4:
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))

#         if choice == 1:
#             print("Result:", a + b)
#         elif choice == 2:
#             print("Result:", a - b)
#         elif choice == 3:
#             print("Result:", a * b)
#         elif choice == 4:
#             if b != 0:
#                 print("Result:", a / b)
#             else:
#                 print("Cannot divide by zero")

#     else:
#         print("Invalid choice")
