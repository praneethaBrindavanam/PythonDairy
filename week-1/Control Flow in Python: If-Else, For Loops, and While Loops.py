In Python, control flow structures determine the order in which your code executes, enabling you to make decisions, repeat tasks, and branch your logic. Three essential structures used for control flow are if-else statements, for loops, and while loops. Let’s explore each one in detail.

1. If-Else Statements
The if-else statement allows you to execute code based on a condition. If the condition evaluates to True, the code block inside the if statement is executed. If the condition is False, the else block (if provided) will execute.

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

2. For Loops
A for loop allows you to iterate over a sequence (such as a list, tuple, or string) and execute a block of code multiple times.

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))



You can also use for loops with the range() function to generate a sequence of numbers.

Example with range():

for i in range(5):
    print(i)
Output:

0
1
2
3
4

break and continue Statements
The break statement breaks out of the innermost enclosing for or while loop:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break


The continue statement continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")


3. While Loops
A while loop keeps executing as long as its condition remains True. This is useful when you don’t know how many times you need to repeat the loop ahead of time.

count = 0

while count < 3:
    print(count)
    count += 1
This prints:


0
1
2
The loop stops once count becomes 3 because the condition (count < 3) is no longer True.

Combining Control Structures
You can combine if-else statements with loops to create more complex logic.

Example:

for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
Output:

0 is even
1 is odd
2 is even
3 is odd
4 is even
Conclusion
Control flow in Python is essential for making decisions (if-else), iterating over sequences (for loops), and repeating tasks until a condition is met (while loops). By mastering these structures, you can write more dynamic, efficient, and complex programs that respond to different inputs and conditions. Understanding when and how to use each control flow mechanism is key to becoming a proficient Python programmer.
