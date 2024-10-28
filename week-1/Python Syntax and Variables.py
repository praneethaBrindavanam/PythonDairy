 

Python Syntax: An Overview
Python’s syntax is known for its simplicity and readability, making it a popular choice among beginners. Let’s explore some of its essential rules:

Case Sensitivity: Python differentiates between uppercase and lowercase letters, so Variable and variable are treated as two different names.

Variable = 10
variable = 20
print(Variable)  # Output: 10
print(variable)  # Output: 20
Indentation: Python uses indentation (usually 4 spaces or a tab) to define code blocks rather than using curly braces {} as in other languages.

if 5 > 2:
    print("Five is greater than two.")  # Indented block
Incorrect indentation leads to an error:

if 5 > 2:
print("This will cause an error.")  # Not indented, SyntaxError
Comments: Comments are important for explaining code. In Python, single-line comments start with a # symbol.

# This is a comment
print("Comments make code easier to understand!")  # This is also a comment

Variables in Python
Variables store data that can be used and manipulated throughout your code. In Python, variables are created the moment you assign a value to them, and you don’t need to explicitly declare their type.

Assigning Values to Variables:

x = 5          # Integer
y = 3.14       # Float
name = "Alice" # String
In the above example:

x is an integer.
y is a floating-point number (a number with decimals).
name is a string (a sequence of characters).
Dynamic Typing: Python is dynamically typed, meaning the type of a variable is inferred from the value you assign to it. You can even change the type of a variable by reassigning it a different value.

a = 10     # Initially an integer
a = "ten"  # Now it's a string
Naming Rules for Variables:

Variable names must start with a letter or an underscore (_), followed by letters, digits, or underscores.
Variable names are case-sensitive.
Avoid using Python's reserved keywords (like if, else, for, etc.) as variable names.
Valid examples:

my_variable = 25
_counter = 10
Invalid examples:

2nd_value = 50    # Invalid: starts with a digit
class = "Python"  # Invalid: 'class' is a reserved keyword
Basic Data Types in Python
Python has several built-in data types. Let’s explore three fundamental types: strings, integers, and floats.

1. Strings (str)
A string is a sequence of characters enclosed in single (') or double (") quotes. Strings are used to represent text data.

Creating Strings:

name = "Alice"
message = 'Welcome to Python!'
String Concatenation: You can join two or more strings using the + operator.

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
Accessing Characters in a String: Strings are indexed, meaning you can access individual characters by referring to their position (starting at 0).

greeting = "Hello"
print(greeting[0])  # Output: H
print(greeting[-1]) # Output: o (negative index counts from the end)

String Length: Use the len() function to get the length of a string.

print(len(greeting))  # Output: 5
2. Integers (int)
Integers are whole numbers without a fractional part. They can be positive or negative.

num1 = 10
num2 = -25
You can perform arithmetic operations with integers:

Addition: +
Subtraction: -
Multiplication: *
Division: / (produces a float)
Exponentiation: **
Floor Division: // (discards the fractional part)
Modulus: % (returns the remainder)
Example:

a = 10
b = 3

print(a + b)  # Output: 13
print(a / b)  # Output: 3.333...
print(a // b) # Output: 3 (floor division)
print(a % b)  # Output: 1 (modulus)
3. Floats (float)
Floats are numbers that have a decimal point. They are used when more precision is required in calculations.

price = 19.99
temperature = 36.6
Floats can be involved in arithmetic operations similar to integers. Note that dividing two integers always results in a float:

x = 5
y = 2
print(x / y)  # Output: 2.5 (float)
Type Checking with type()
Python allows you to check the type of a variable using the type() function. This is useful when you’re working with different types and want to confirm the data type.

name = "Alice"
age = 30
pi = 3.14159

print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(pi))    # Output: <class 'float'>
Type Conversion
Sometimes, you’ll need to convert one type to another, such as turning a string into an integer or a float into a string. Python provides several functions for type conversion:

int(): Converts a value to an integer.
float(): Converts a value to a float.
str(): Converts a value to a string.
Example:

# Convert a float to an integer
height = 5.9
height_int = int(height)  # Output: 5 (decimal part discarded)

# Convert a string to a float
price_str = "19.99"
price = float(price_str)  # Output: 19.99 (float)

# Convert an integer to a string
age = 25
age_str = str(age)
Quick Exercise: Putting It All Together
Let’s create a small program that takes input from the user, performs some calculations, and prints the result.

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

# Perform some calculations
years_to_100 = 100 - age

# Output the results
print(name + ", you will turn 100 years old in " + str(years_to_100) + " years.")
print("Your height is " + str(height) + " meters.")
This program demonstrates how to work with strings, integers, and floats, along with basic input and output functions.

Conclusion
By now, you should have a solid understanding of Python’s syntax, how to work with variables, and the basic data types. These foundational concepts will help you handle more complex programming tasks as you progress. Keep experimenting, and stay tuned , where we’ll explore control structures in Python!
