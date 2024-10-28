 NumPy and Pandas are two of the most widely used libraries in Python for data science, offering powerful tools for data manipulation and analysis.

NumPy
NumPy (Numerical Python) is the foundational library for numerical computing in Python. It provides support for arrays, matrices, and a collection of mathematical functions to operate on these data structures efficiently.

Key Features:
Supports multi-dimensional arrays and matrices.
Provides mathematical functions to perform operations on arrays.
Offers a variety of linear algebra, Fourier transform, and random number generation functions.
Example:
Here’s a simple example demonstrating how to create an array and perform basic operations using NumPy:

import numpy as np



# Create a 1D array

array_1d = np.array([1, 2, 3, 4, 5])

print("1D Array:", array_1d)



# Create a 2D array (matrix)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("2D Array:\n", array_2d)



# Perform element-wise operations

squared_array = array_1d ** 2

print("Squared Array:", squared_array)



# Sum of all elements

sum_array = np.sum(array_1d)

print("Sum of Array Elements:", sum_array)


Pandas
Pandas is a powerful data manipulation and analysis library built on top of NumPy. It introduces two primary data structures: Series (1D) and DataFrame (2D), making it easy to work with structured data.

Key Features:
Provides data structures for efficiently storing and manipulating data.
Supports operations for data cleaning, aggregation, and visualization.
Offers robust tools for handling missing data.
Example:
Here’s a simple example demonstrating how to create a DataFrame and perform basic operations using Pandas:



import pandas as pd



# Create a DataFrame

data = {

    'Name': ['Alice', 'Bob', 'Charlie'],

    'Age': [25, 30, 35],

    'City': ['New York', 'Los Angeles', 'Chicago']

}

df = pd.DataFrame(data)

print("DataFrame:\n", df)



# Access a specific column

ages = df['Age']

print("Ages:\n", ages)



# Calculate the average age

average_age = df['Age'].mean()

print("Average Age:", average_age)



# Filter rows where Age is greater than 28

filtered_df = df[df['Age'] > 28]

print("Filtered DataFrame (Age > 28):\n", filtered_df)
Summary
NumPy is essential for numerical computing and array manipulations, while Pandas provides a high-level interface for handling and analyzing structured data. Both libraries are integral to the data science workflow in Python, enabling efficient data manipulation and analysis.
