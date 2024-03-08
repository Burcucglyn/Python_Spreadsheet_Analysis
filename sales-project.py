# Imported the pandas library to read the data from spreadsheet
import pandas as pd

# for the visualization need to use matplotlib library so need to import it
import matplotlib.pyplot as plt

# 1.how can I read the data from spreadsheet?
#Used the read_data function and defined the path way seperately
file_path = '/Users/burdzhuchaglayan/Desktop/python_project feb 2024/sales.csv'

#used the read_csv function- competable with panda library

data = pd.read_csv(file_path)
#for make sure my code is working I display the rows with print command
print(data)

#2.how can I collect all of the sales from each month into a single list?
#have to created the an empty list

monthly_sales= []
#how do i iterate in phyon? using for loops
#iterated over each row below

for index, row in data.iterrows():
  #have to access the sales column to collect the data into single list.
    monthly_sales.append(row['sales'])

#use the print command to see if it's correct.
print("Monthly Sales:", monthly_sales)

#3.how to output the total sales across all months?
#use the monthly sales list, and defined to system first.

sales = [6226, 1521, 1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]

#calculate the total sales using sum function to add up all the values in list.
total_sales = sum(sales)

#use the print command to see total sales

print('total sales across all months:', total_sales)

# 4. Create a simple bar chart to visualize monthly sales
# Plotting the monthly sales data
plt.bar(range(1, 13), monthly_sales)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Analysis')
plt.show()

