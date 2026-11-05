# Q1. Write a Python program to check whether a number is even or odd.

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# Q2. Write a program to find the largest of three numbers.


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest =", a)
# elif b >= a and b >= c:
#     print("Largest =", b)
# else:
#     print("Largest =", c)

# Q3. Write a program to check whether a given number is prime.


# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime Number")
# else:
#     print("Not Prime")

# Q4. Write a program to print the Fibonacci series up to n terms.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# Q5. Write a program to find the factorial of a number using a loop.

# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial =", fact)

# 2. String Programs

# Q6. Write a program to reverse a string without using [::-1].

# text = input("Enter a string: ")

# reverse = ""

# for ch in text:
#     reverse = ch + reverse

# print("Reverse =", reverse)

# Q7. Write a program to check whether a string is a palindrome.

# text = input("Enter a string: ")

# reverse = ""

# for ch in text:
#     reverse = ch + reverse

# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Q8. Write a program to count the number of vowels and consonants in a string.

# text = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for ch in text.lower():
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels =", vowels)
# print("Consonants =", consonants)
# 3. List Programs

# Q9. Write a program to find the sum of all elements in a list.

# numbers = [10, 20, 30, 40, 50]

# total = 0

# for num in numbers:
#     total += num

# print("Sum =", total)

# Q10. Write a program to find the largest and smallest element in a list without using max() or min().

# numbers = [10, 50, 20, 5, 40]

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest =", largest)
# print("Smallest =", smallest)

# Q11. Write a program to remove duplicate elements from a list.

# numbers = [10, 20, 30, 20, 40, 10]

# result = []

# for num in numbers:
#     if num not in result:
#         result.append(num)

# print("List without duplicates =", result)

# Q12. Write a program to count how many times each element appears in a list using a dictionary.

# numbers = [10, 20, 10, 30, 20, 10]

# frequency = {}

# for num in numbers:
#     frequency[num] = frequency.get(num, 0) + 1

# print(frequency)

# Q13. Write a program to find the second-largest number in a list.

# numbers = [10, 20, 50, 30, 40]

# unique = list(set(numbers))
# unique.sort()

# if len(unique) >= 2:
#     print("Second Largest =", unique[-2])
# else:
#     print("Second largest does not exist")

# Q14. Write a program to sort a list without using sort() or sorted().


# numbers = [40, 10, 30, 20, 50]

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] > numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]

# print("Sorted List =", numbers)

# Q15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.

# def even_numbers(numbers):

#     result = []

#     for num in numbers:
#         if num % 2 == 0:
#             result.append(num)

#     return result

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print("Even Numbers =", even_numbers(numbers))
# 4. String and List Logic Programs

# Q16. Write a program to find the frequency of each character in a string.

# text = input("Enter a string: ")

# frequency = {}

# for ch in text:
#     frequency[ch] = frequency.get(ch, 0) + 1

# print(frequency)

# Q17. Write a program to check whether two strings are anagrams of each other.

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if sorted(str1.lower()) == sorted(str2.lower()):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

# Q18. Write a program to find all duplicate values in a list.

# numbers = [10, 20, 30, 20, 40, 10, 50]

# duplicates = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate Values =", duplicates)

# Q19. Write a program that takes a sentence and finds the longest word.
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest Word =", longest)
# print("Length =", len(longest))

# 5. Student Marks Program
# Q20. Create a simple student marks program that:
# Accepts marks for 5 subjects.
# Calculates the total and percentage.
# Assigns a grade.
# Displays whether the student passed or failed.

# Grade criteria (example):

# 90 and above: A
# 80 and above: B
# 70 and above: C
# 60 and above: D
# Below 60: F
# Passing marks: 35 in each subject.
# marks = []

# for i in range(1, 6):
#     m = int(input("Enter marks for subject " + str(i) + ": "))
#     marks.append(m)

# total = sum(marks)
# percentage = total / 5

# print("Total Marks =", total)
# print("Percentage =", percentage, "%")

# if any(m < 35 for m in marks):
#     print("Result: Fail")
#     print("Grade: F")

# elif percentage >= 90:
#     print("Grade: A")
#     print("Result: Pass")

# elif percentage >= 80:
#     print("Grade: B")
#     print("Result: Pass")

# elif percentage >= 70:
#     print("Grade: C")
#     print("Result: Pass")

# elif percentage >= 60:
#     print("Grade: D")
#     print("Result: Pass")

# else:
#     print("Grade: F")
#     print("Result: Pass")