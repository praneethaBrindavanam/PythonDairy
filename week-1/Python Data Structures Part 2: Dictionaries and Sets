 

Python Data Structures Part 2: Dictionaries and Sets
In Python, dictionaries and sets are versatile data structures that allow for efficient storage and manipulation of data. Let's explore each in detail, including their use cases and examples.

Dictionaries
A dictionary in Python is an unordered collection of items. Each item is a pair made up of a key and a value. Dictionaries are mutable, meaning their contents can be modified. They are also indexed by keys, which must be unique and immutable, such as strings, numbers, or tuples.

Key Characteristics of Dictionaries:
Key-value pairs: Each element in a dictionary is stored as a key-value pair. Keys are unique, while values can be duplicated.
Unordered: Items are not stored in any specific order.
Mutable: You can add, modify, or remove elements.
Creating a Dictionary
# Creating a dictionary
student = {
    'name': 'John',
    'age': 22,
    'courses': ['Math', 'Computer Science']
}
print(student)

Accessing Values
You can access values in a dictionary using their corresponding keys:

# Accessing a value by its key
print(student['name'])  # Output: John

Adding or Updating a Key-Value Pair
# Adding a new key-value pair
student['grade'] = 'A'

# Modifying an existing value
student['age'] = 23
print(student)

Removing a Key-Value Pair
# Removing a key-value pair
del student['grade']
print(student)

Use Cases of Dictionaries
Storing configurations: Dictionaries are great for managing configuration settings, where the settings name serves as the key, and the corresponding values are the configuration values.
Counting occurrences: Using a dictionary to count the frequency of elements in a list or a string.
Mapping relationships: Dictionaries are useful for representing mappings, such as an employee ID to employee details.
Example: Word Frequency Counter
# Example: Counting word frequency
text = "hello world hello"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # Output: {'hello': 2, 'world': 1}

Sets
A set in Python is an unordered collection of unique elements. Sets are mutable, but the elements they contain must be immutable (e.g., numbers, strings, or tuples). Sets do not allow duplicates, making them useful for storing collections of distinct items.

Key Characteristics of Sets:
Unordered: The order of elements in a set is not guaranteed.
Unique elements: Duplicate elements are automatically removed.
Mutable: You can add or remove elements.
Creating a Set
# Creating a set
fruits = {'apple', 'banana', 'cherry'}
print(fruits)

Adding and Removing Elements
# Adding an element
fruits.add('orange')
# Removing an element
fruits.remove('banana')
print(fruits)

Set Operations
Sets support various mathematical operations like union, intersection, and difference.

Union (|): Combines two sets, including all unique elements from both.
Intersection (&): Returns only the elements common to both sets.
Difference (-): Returns elements that are in one set but not in the other.
Example of Set Operations
# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}

# Intersection of two sets
intersection_set = set1 & set2  # {3}

# Difference of two sets
difference_set = set1 - set2  # {1, 2}

Removing duplicates: Easily eliminate duplicate entries from a list.
Membership testing: Sets offer a fast way to check if an item is present in a collection.
Mathematical operations: Useful for performing union, intersection, and difference operations.
Example: Removing Duplicates from a List
# Removing duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}


Summary
Dictionaries are useful for storing key-value pairs, where each key is unique, and values can be accessed or modified via their corresponding keys.
Sets are collections of unique elements that support fast membership tests and allow for mathematical operations like union, intersection, and difference.
Both dictionaries and sets add flexibility and efficiency to Python programming, making them essential for various use cases involving data management and manipulation.
