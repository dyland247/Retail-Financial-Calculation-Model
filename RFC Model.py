# Install required libraries
# pip install pandas numpy

import pandas as pd

# Function to calculate average order cost
def calculate_average_order_cost(costs):
    return sum(costs) / len(costs)

# Get user input for sales and cost data
num_entries = int(input("Enter the number of sales entries: "))
data = {'Date': [], 'Product': [], 'Sales': [], 'Cost': []}

for _ in range(num_entries):
    date = input("Enter date (YYYY-MM-DD): ")
    product = input("Enter product: ")
    sales = float(input("Enter sales amount: "))
    cost = float(input("Enter cost amount: "))

    data['Date'].append(date)
    data['Product'].append(product)
    data['Sales'].append(sales)
    data['Cost'].append(cost)

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate average order cost
df['OrderCost'] = df.groupby('Date')['Cost'].transform(calculate_average_order_cost)

# Calculate daily sales
daily_sales = df.groupby('Date')['Sales'].sum()

# Calculate profit margins
df['ProfitMargin'] = (df['Sales'] - df['Cost']) / df['Sales'] * 100

# Display the results
print("\nAverage Order Cost:")
print(df[['Date', 'Product', 'OrderCost']])
print("\nDaily Sales:")
print(daily_sales)
print("\nProfit Margins:")
print(df[['Date', 'Product', 'ProfitMargin']])
