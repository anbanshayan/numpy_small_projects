import numpy as np

# Define the sales data
sales_data = np.array([
    [50, 60, 55, 62, 58, 64, 70],  # Product 1
    [30, 35, 32, 31, 40, 38, 45],  # Product 2
    [20, 22, 18, 25, 24, 20, 21],  # Product 3
    [80, 78, 85, 88, 90, 87, 92],  # Product 4
    [10, 15, 12, 11, 14, 16, 20]   # Product 5
])

# Save the data into a CSV file
header = "Mon,Tue,Wed,Thu,Fri,Sat,Sun"  # Column names for the days
np.savetxt("sales_data.csv", sales_data, fmt='%d', delimiter=',', header=header, comments="")

print("Sales data has been saved to 'sales_data.csv'.")
