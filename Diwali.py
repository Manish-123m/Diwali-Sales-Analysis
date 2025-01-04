import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the data
file_path = 'C:/Users/manis/Downloads/Project/Diwali Sales Data.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Check the first few rows
print(data.head())

# Check for null values and data types
print(data.info())
# Drop empty columns
data = data.drop(columns=['Status', 'unnamed1'])

# Handle missing values
data['Amount'].fillna(data['Amount'].median(), inplace=True)

# Verify the cleaned dataset
print(data.isnull().sum())
print("==============================================================================================")
# Countplot for gender
sns.countplot(x='Gender', data=data)
plt.title('Gender-wise Distribution')
plt.show()
print("===================================================================")
# Sales by age group
age_sales = data.groupby('Age Group')['Amount'].sum().reset_index()

# Barplot
sns.barplot(x='Age Group', y='Amount', data=age_sales)
plt.title('Sales by Age Group')
plt.show()
print("================================")
# Top 10 states by sales
state_sales = data.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)

# Barplot
state_sales.plot(kind='bar', figsize=(10, 5), color='skyblue')
plt.title('Top 10 States by Sales')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.show()
print("=========================")
# Categorize customers as High Spenders and Low Spenders
data['Spender_Type'] = np.where(data['Amount'] > data['Amount'].mean(), 'High Spender', 'Low Spender')

# Countplot for spender types
sns.countplot(x='Spender_Type', data=data)
plt.title('Customer Segmentation')
plt.show()

print("======================================================")
import plotly.express as px

# Interactive state sales plot
fig = px.bar(state_sales.reset_index(), x='State', y='Amount', title='Top 10 States by Sales')
fig.show()

# Save cleaned data
data.to_csv('Cleaned_Diwali_Sales_Data.csv', index=False)
print("Cleaned data saved successfully!")

