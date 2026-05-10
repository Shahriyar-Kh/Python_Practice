# =========================================================
# CHAPTER 1 — HANDS-ON PRACTICE SET
# Programming Foundations
# =========================================================


# =========================================================
# 1. Install Python and run your first file in VS Code
# =========================================================

print("Python Installed Successfully")


# =========================================================
# 2. Open Python interactive shell and run 5 small commands
# =========================================================

print("Hello")
print(3 + 4)
print(3 - 2)
print(4 * 3)
print(9 / 3)


# =========================================================
# 3. Write a program that prints your name, age, and city
# =========================================================

print("Shary")
print(25)
print("Islamabad")


# =========================================================
# 4. Create 5 valid and 5 invalid identifiers
# =========================================================

# Valid Identifiers
name = "Ali"
u_name = "Khan"
num1 = 10
num_1 = 20
myName = "Python"

# Invalid Identifiers Examples
# 1name
# @name
# user name
# u-name
# if

# Corrected Versions
name1 = "Ali"
user_name = "Khan"
userName = "Ahmed"
u_name_fixed = "Python"
user_if = "Data"


# =========================================================
# 5. Write a program with proper indentation using if and else
# =========================================================

age = 30

if age == 25:
    print("Eligible")
else:
    print("Not Eligible")


# =========================================================
# 6. Add comments to a small program
# =========================================================

# Create variable A and assign value 4
A = 4

# Print value of A
print(A)


# =========================================================
# 7. Write a docstring for a simple function
# =========================================================

def add():
    """Function for addition"""
    pass


# =========================================================
# 8. Store values in variables and reassign them 3 times
# =========================================================

a = 1
print(a)

a = 2
print(a)

a = 3
print(a)


# =========================================================
# 9. Check the type of int, float, bool, and str values
# =========================================================

print(type("Khan"))
print(type(34))
print(type(True))
print(type(3.3))


# =========================================================
# 10. Convert string input into integer and float
# =========================================================

num = "100"

num_int = int(num)
num_float = float(num)

print(num_int)
print(num_float)


# =========================================================
# 11. Use print() with sep and end
# =========================================================

print("Python", "C++", "JS", sep=" | ", end=" -> Languages\n")


# =========================================================
# 12. Take user input and print a formatted message
# =========================================================

name = input("Enter Username: ")

print(f"User name is {name}")


# =========================================================
# 13. Use arithmetic operators on two numbers
# =========================================================

A = 4
B = 5

result = A + B
print("Addition:", result)

result = A - B
print("Subtraction:", result)

result = A * B
print("Multiplication:", result)

result = A / B
print("Division:", result)


# =========================================================
# 14. Use comparison operators to compare two values
# =========================================================

A = 3
B = 3

print(A == B)
print(A != B)
print(A > B)
print(A < B)


# =========================================================
# 15. Use logical operators in one condition
# =========================================================

age = 25
city = "isb"

if age == 25 and city == "isb":
    print("Eligible for vote")


# =========================================================
# 16. Use membership operators with a string and list
# =========================================================

print("h" in "Shary")

numbers = [1, 2, 3]

print(2 in numbers)
print(5 not in numbers)


# =========================================================
# 17. Trace a small program line by line
# =========================================================

x = 5
print("Step 1:", x)

x = x + 2
print("Step 2:", x)

x = x * 3
print("Step 3:", x)


# =========================================================
# 18. Add print-debugging to find a wrong result
# =========================================================

a = 10
b = 5

print("Value of a:", a)
print("Value of b:", b)

result = a + b

print("Result:", result)


# =========================================================
# 19. Catch invalid input using try-except
# =========================================================

try:
    a = 20
    div = a / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Code executed")


# =========================================================
# 20. Handle division by zero safely
# =========================================================

try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Invalid input")

finally:
    print("Program Finished")


# =========================================================
# END OF CHAPTER 1 PRACTICE SET
# =========================================================