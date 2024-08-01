# import matplotlib.pyplot library and numpy library
import matplotlib.pyplot as plt
import numpy as np

# given data
months = np.arange(1, 13) 
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000]) 
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]) 
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create a subplot with four subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# plot on the first subplot
axs[0, 0].plot(months, electronics_sales, color="r")
axs[0, 0].set_title("monthly electronic sales")
axs[0, 0].set_xlabel("months")
axs[0, 0].set_ylabel("electronic sales")

# plot on the second subplot
axs[0, 1].plot(months, clothing_sales, color="b")
axs[0, 1].set_title("monthly clothing sales")
axs[0, 1].set_xlabel("months")
axs[0, 1].set_ylabel("clothing sales")

# plot on the third subplot
axs[1, 0].plot(months, home_garden_sales, color = "g")
axs[1, 0].set_title("monthly home garden sales")
axs[1, 0].set_xlabel('months')
axs[1, 0].set_ylabel("home garden sales")

# plot on the fourth subplo
axs[1, 1].plot(months, sports_outdoors_sales, color = 'm')
axs[1, 1].set_title("monthly sport outdoor sales")
axs[1, 1].set_xlabel("months")
axs[1, 1].set_ylabel("sport outdoor sales")

# adjust layout to prevent overlap
plt.tight_layout()

# printing the plots
plt.show()
