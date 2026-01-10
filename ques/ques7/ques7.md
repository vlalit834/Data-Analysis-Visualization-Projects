# Hello developers! Welcome to **Project 2: Course Enrollment Data Cleaner!** ✏️📊

Chef is reviewing course enrollment data from an online learning platform. The dataset contains valuable insights like **course titles**, **subjects**, **pricing**, and **student enrollments**.

However, raw data is rarely perfect. It often contains duplicates, missing values, or inconsistent formatting. Chef needs you to build a robust **Data Cleaning Pipeline** to:

1. **Standardize** text formatting (Title Case).
2. **Remove** redundant duplicate entries.
3. **Handle** missing data so analysis doesn't crash.
4. **Estimate** revenue potential.

Your job is to use the **Pandas** library to transform the raw CSV file into a clean, analysis-ready dataset.

---

## What's Already Provided

You are given a single file: `main.py`

- All required **function names** are already defined.
- The program flow is already set up.
- You need to complete the missing parts marked with `TODO`.
- **Important:** Do NOT change function names or print statements.

## Dataset

You will work with a real dataset: `udemy_courses.csv`. It contains columns such as:

- `course_title` (Name of the course)
- `subject` (Category, e.g., "Business Finance")
- `price` (Cost in $)
- `num_subscribers` (Total students enrolled)
- `num_lectures` (Count of video lectures)

---

## Your Tasks

1. **Load Dataset**

Inside `load_data()`:

- Read the dataset (`udemy_courses.csv`) into a Pandas DataFrame.
- We are returning the Pandas DataFrame so that it can be reused in other functions.

Docs: `pd.read_csv()`

2. **Inspect the Data**

Inside `inspect_data()`:

- Print the head of the DataFrame, its info, and summary statistics.

Docs: `DataFrame.head()` | `DataFrame.info()` | `DataFrame.describe()`

3. **Remove Duplicate Records**

Inside `remove_duplicates()`:

- Remove duplicate courses based on the combination of `['course_title', 'subject']`.
- Keep only the **first** occurrence.

Docs: `DataFrame.drop_duplicates()`

4. **Clean Strings & Fix Data Types**

Inside `fix_data_types()`:

- Strings: Strip whitespace and convert to **Title Case** for both `course_title` and `subject` columns.
- Numbers:
  - Convert `price` to `float`.
  - Convert `num_subscribers` to `int`.

Docs: `Series.str.strip()` | `Series.str.title()` | `DataFrame.astype()`

5. **Create New Derived Column**

Inside `add_new_columns()`:

- Create a new column named `revenue_estimate`.
- Formula: `price * num_subscribers`.
- This helps Chef estimate the total earnings for each course.

6. **Save the Cleaned Dataset**

Inside `save_cleaned_data()`:

- Save the final DataFrame to a file named `cleaned_udemy_courses.csv`.
- **Important:** Do not save the index numbers.

Docs: `DataFrame.to_csv()`

---

## Expected Output

```
Online Course Enrollment Data Cleaner...

Original Dataset Preview:
   course_id                 course_title  price  num_subscribers  num_reviews  num_lectures           subject
0   1070968  Ultimate Investment Banking Course  200.0           2147           23            51  Business Finance
1   1113822  Complete GST Course & Certification - Grow You...   75.0           2792          923           274  Business Finance
2   1006314  Financial Modeling for Business Analysts and C...   45.0           2174           74            51  Business Finance
3   1210588  Beginner to Pro - Financial Analysis in Excel ...   95.0           2451           11            36  Business Finance
4   1011058  How To Maximize Your Profits Trading Options    200.0           1276           45            26  Business Finance

Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3728 entries, 0 to 3727
Data columns (total 7 columns):
#   Column          Non-Null Count  Dtype
---  ------          --------------  -----
0   course_id       3728 non-null   int64
1   course_title    3728 non-null   object
2   price           3557 non-null   float64
3   num_subscribers 3537 non-null   float64
4   num_reviews     3728 non-null   int64
5   num_lectures    3728 non-null   int64
6   subject         3728 non-null   object

dtypes: float64(2), int64(3), object(2)
memory usage: 204.0+ KB
None

Summary Statistics:
           course_id        price  num_subscribers  num_reviews  num_lectures
count  3.728000e+03  3557.000000      3537.000000  3728.000000  3728.000000
mean   6.772924e+05    66.935620      3262.531524   159.183745    40.296674
std    3.433877e+05    61.663863      9655.295493   932.314879    50.422460
min    8.324000e+03     0.000000         0.000000     0.000000     0.000000
25%    4.088045e+05    20.000000       114.000000     5.000000    15.000000
50%    6.889210e+05    45.000000       945.000000    18.000000    25.000000
75%    9.633865e+05    95.000000      2610.000000    69.000000    46.000000
max    1.282064e+06   200.000000    268923.000000 27445.000000   779.000000

Cleaned Dataset Preview:
   course_id                 course_title  price  num_subscribers  num_reviews  num_lectures           subject  revenue_estimate
0   1070968  Ultimate Investment Banking Course  200.0           2147           23            51  Business Finance         429400.0
1   1113822  Complete Gst Course & Certification - Grow You...   75.0           2792          923           274  Business Finance         209400.0
2   1006314  Financial Modeling For Business Analysts And C...   45.0           2174           74            51  Business Finance          97830.0
3   1210588  Beginner To Pro - Financial Analysis In Excel ...   95.0           2451           11            36  Business Finance         232845.0
4   1011058  How To Maximize Your Profits Trading Options    200.0           1276           45            26  Business Finance         255200.0

Cleaned data saved to 'cleaned_udemy_courses.csv'
```

Good luck and happy cleaning! ✅
