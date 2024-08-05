# import pandas library
import pandas as pd

# given data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# performing series operation
series = pd.Series(expenses, categories)

# print output
print(series)

# Output
"""
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
dtype: int64
"""
