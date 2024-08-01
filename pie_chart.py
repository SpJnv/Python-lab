# importing matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# data given
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# ploting the pie chart
plt.pie(monthly_income, labels = income_sources, autopct='%1.1f%%')

# title
plt.title("monthly income")

# print the output
plt.show()
