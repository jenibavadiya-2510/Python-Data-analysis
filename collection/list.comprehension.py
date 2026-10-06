
# Level 1 — Basic

# Q1. Create a list of numbers from 1 to 10 using list comprehension.
# numbers = [i for i in range(1, 11)]
# print(numbers)

# Q2. Create a list containing the squares of numbers from 1 to 10.
# numbers = [i ** 2 for i in range(1, 10)]
# print(numbers)

# Q3. Create a list containing the cubes of numbers from 1 to 10.
# numbers = [i ** 3 for i in range(1, 10)]
# print(numbers)

# Q4. Create a list of numbers from 1 to 20 where each number is multiplied by 5.
# numbers = [i * 5 for i in range(1, 21)]
# print(numbers)

# Q5. Create a list of all characters from this string:
# name = "PYTHON"
# name = "PYTHON"
# letters = [ch for ch in name]
# print(letters)

# 🟡 Level 2 — With if Condition

# Q6. Create a list of all even numbers from 1 to 20.
# even = [i for i in range(1, 11) if i % 2 == 0]
# print(even)

# Q7. Create a list of all odd numbers from 1 to 20.
# odd = [i for i in range(1, 11) if i % 2 != 0]
# print(odd)

# Q8. Create a list of numbers from 1 to 50 that are divisible by 5.
# numbers = [i for i in range(1, 51) if i % 5 == 0]
# print(numbers)

# Q9. Create a list of numbers from 1 to 30 that are divisible by both 3 and 5.
# numbers = [i for i in range(1, 31) if i % 3 == 0 and i % 5 == 0]
# print(numbers)

# Q10. Given:
# numbers = [-5, 10, -3, 7, -1, 8, -9, 20]
# Create a list containing only positive numbers.
# numbers = [-5, 10, -3, 7, -1, 8, -9, 20]
# positive = [i for i in numbers if i > 0]
# print(positive)

# 🟠 Level 3 — Strings
# Q11. Convert every character of "python" to uppercase using list comprehension.
# name = "python"
# result = [ch.upper() for ch in name]
# print(result)

# Q12. Given:
# words = ["cat", "python", "dog", "computer", "pen", "table"]
# Create a list containing only words whose length is greater than 4.
# words = ["cat", "python", "dog", "computer", "pen", "table"]
# result = [word for word in words if len(word)>4]
# print(result)

# Q13. Given:
# words = ["apple", "banana", "orange", "grapes"]
# Create a list containing the length of each word.
# words = ["apple", "banana", "orange", "grapes"]
# result = [len(word) for word in words]
# print(result)

# Q14. Given:
# name = "DataAnalyst"
# Create a list containing only the vowels.
# name ="DataAnalyst"
# vowels = [ch for ch in name if ch.lower() in "aeiou"]
# print(vowels)

# Q15. Given:
# name = "Python123"
# Create a list containing only the digits.
# name = "Python123"
# digits = [ch for ch in name if ch.isdigit()]
# print(digits)