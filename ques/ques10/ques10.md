Hello developers! Welcome to Project 5: Customer Purchase Insights! 🧾📊

Chef runs a growing retail shop that sells electronics items! However, his sales records are messy. 😵

Some entries are incomplete, some contain missing values, and he has no quick way to understand:

- Which customers spend the most?
- Which product sells the fastest?
- How much revenue is actually being generated?

Your task is to transform these raw transaction logs into meaningful business insights! 💡

---

## What's Already Provided

You are given a single file: `main.py`

- All required **function names** are already defined.
- The program flow is already set up.
- You only need to **complete the missing logic**.
- Do **NOT** change function names or print statements.

---

## Dataset

You will work with `retail_store_sales.csv`. It contains transaction records.

It contains the following columns:

- `Transaction_ID`: Unique ID for the order
- `Customer_ID`: Unique ID for the customer
- `Item`: Name of the product purchased
- `Price_Per_Unit`: Cost of one unit ($)
- `Quantity`: Number of units purchased

---

## Your Tasks

1. Load the Dataset

Inside `load_sales_data()`:

- Read the dataset (`retail_store_sales.csv`).
- Print a preview of the first 5 records to check if it loaded correctly.

Docs: `pd.read_csv()` | `df.head()`

---

2. Clean the Data

Inside `clean_data(df)`: Real-world data is rarely perfect. We need to handle missing values.

- Drop Invalid Rows:
  - Remove rows where `Customer_ID` is missing.
  - Crucial: Use `.copy()` after dropping to avoid the "SettingWithCopyWarning".
- Impute Missing Values: Fill missing `Quantity` and `Price_Per_Unit` with their **median** values (this is more robust than using the average).
- Print the count of dropped rows.

Docs: `df.dropna()` | `df.fillna()`

---

3. Feature Engineering

Inside `add_total_price(df)`:

We need to calculate the total value of each order.

- Create a new column `Total_Amount` by multiplying `Price_Per_Unit` and `Quantity`.

---

4. NumPy Matrix Analysis

Inside `perform_numpy_analysis(df)`:

- Convert: Select the numerical columns (`Price`, `Quantity`, `Total`) and convert them to a NumPy array.
- Aggregate: Calculate the **Max** and **Mean** along the columns.
- Print: Display these four values:
  1. Max Price (up to 2 decimal places)
  2. Max Quantity
  3. Max Total Order Value (up to 2 decimal places)
  4. Average Order Value (up to 2 decimal places)

Docs: `df.to_numpy()` | `np.max()` | `np.mean()`

---

5. Business Insights

Inside `analyze_statistics(df)`:

Calculate:

- Total Revenue: Sum of `Total_Amount` (up to 2 decimal places).
- Average Order Value: Average of `Total_Amount` (up to 2 decimal places).
- Top Customer: Find which `Customer_ID` has the highest total spending.
- Top Item: Find which `Item` has the highest total `Quantity` sold.
- Return these results as a dictionary.

Docs: `df.groupby()` | `df.idxmax()` | `df.sum()` | `df.mean()`

---

## Expected Output:

When you run the program, it should print messages like this:

```
Customer Purchase Insights...

Dataset Preview:
   Transaction_ID  Customer_ID       Item  Price_Per_Unit  Quantity
0            1001         C001  Wireless Mouse            25.0       2.0
1            1002         C002  Mechanical Keyboard       85.0       1.0
2            1003          NaN  USB Cable                 12.0       5.0
3            1004         C003  Monitor                    NaN       2.0
4            1005         C001  HDMI Cable                15.0       NaN

Cleaning Data:
Rows dropped (Missing ID): 5
Missing values in Price/Quantity filled with Median.

Added 'Total_Amount' column.

NumPy Matrix Analysis:
Matrix Shape: (20, 3)
Max Price: $300.00
Max Quantity in one order: 10
Max Total Order Value: $300.00
Avg Order Value: $90.50

Customer Insights:
Total Store Revenue: $1810.00
Average Order Value: $90.50
Top Spending Customer: C003
Most Popular Item: USB Cable
```

---

Good luck and happy data cleaning! 🧹📈
