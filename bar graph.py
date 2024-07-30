# importing the matplotlib.pyplot module
import matplotlib.pyplot as plt

# Given Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# ploting the bar graph
plt.bar(categories, expenses)

# labeling and title
plt.xlabel("categories")
plt.ylabel("expenses")
plt.title("Monthly expenses")

# Showing the output
plt.show()
