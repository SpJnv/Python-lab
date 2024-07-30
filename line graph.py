# importing the matplotlib.pyplt library
import matplotlib.pyplot as plt

# Give data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# ploting the data for histogram
plt.plot(days, temperature)

# labels and title
plt.ylabel("Temperature")
plt.xlabel("Days")
plt.title("temperature distribution in a month")

# printing output
plt.show()
