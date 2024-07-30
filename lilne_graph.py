# importing the matplotlib library
import matplotlib.pyplot as plt

# Data
x = [0, 5, 9, 10, 15, 20, 25] 
y = [0, 1, 2, 3, 4, 5, 6]

# ploting the line chart
plt.plot(x,y)

# labeling and heading
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)

plt.title("simple line graph")

# printing the graph
plt.show()
