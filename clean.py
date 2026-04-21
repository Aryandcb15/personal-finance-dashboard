import pandas as pd

# Load the data
df = pd.read_csv('personal_transactions.csv')

# Convert Date to proper date format
df['Date'] = pd.to_datetime(df['Date'])

# Add Month and Year columns (useful for Tableau)
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Month_Year'] = df['Date'].dt.to_period('M').astype(str)

# Remove Credit Card Payment rows (these are just transfers, not real expenses)
df = df[df['Category'] != 'Credit Card Payment']

# Split into income and expenses
df_expenses = df[df['Transaction Type'] == 'debit']
df_income = df[df['Transaction Type'] == 'credit']

# Save cleaned files
df_expenses.to_csv('expenses_clean.csv', index=False)
df_income.to_csv('income_clean.csv', index=False)

print("Done! Expenses rows:", len(df_expenses))
print("Done! Income rows:", len(df_income))
print(df_expenses.head())