# Netflix Library Explorer 📺📊

**Hello developers!** Welcome to the **Netflix Library Explorer Project**.

Chef is building a data exploration tool to analyze Netflix's content catalog using **tabular data**. Netflix stores thousands of movies and TV shows, but raw CSV data alone doesn't provide meaningful insights.

Chef wants to explore the Netflix library to:

- **Understand the size and structure of the catalog**
- **Discover recently released content**
- **Identify popular content ratings**

Your task is to use the **Pandas** library to transform raw Netflix data into simple, readable insights.

---

## What's Already Provided ✅

- You are given a single file: `main.py`
- All required function names are already defined.
- The program flow is already written.
- You only need to fill in the missing logic (________) using the **Pandas** library.
- **Do NOT** change function names or print statements.

---

## Dataset 📁

You will work with a Netflix dataset stored in a CSV file:

- **File name:** `netflix.csv`
- The dataset contains information such as:
  - Title
  - Content type (Movie / TV Show)
  - Release year
  - Rating
  - Country

---

## Your Tasks 🧭

### 1. Load Netflix Dataset (inside `load_data()`)

- Load the Netflix CSV file using Pandas.
- Print the first 5 rows showing:
  - `title`
  - `type`
  - `release_year`
- Return the Pandas `DataFrame` so it can be used in other functions.

Docs: `pd.read_csv()`, `DataFrame.head()`

---

### 2. Explore Dataset Structure (inside `explore_dataset(df)`)

- Print:
  - Shape of the dataset (rows × columns)
  - List of column names as a Python list

Docs: `DataFrame.shape`, `DataFrame.columns`

---

### 3. Analyze Content Distribution (inside `count_content_types(df)`)

- Count how many **Movies** and **TV Shows** are present.
- Print the distribution.

Docs: `Series.value_counts()`

---

### 4. Filter Recent Content (inside `filter_recent_content(df)`)

- Filter content released **after the year 2015**.
- Print the first 5 rows showing:
  - `title`
  - `type`
  - `release_year`
- Return the filtered `DataFrame`.

Docs: `DataFrame.head()`

---

### 5. Find Popular Ratings (inside `top_ratings(df)`)

- Identify and print the **top 5 most common content ratings**.

Docs: `Series.value_counts()`, `DataFrame.head()`

---

### 6. View Latest Netflix Content (inside `sort_by_release_year(df)`)

- Sort content by `release_year` in **descending** order.
- Print the first 5 rows showing:
  - `title`
  - `type`
  - `release_year`

Docs: `DataFrame.sort_values()`, `DataFrame.head()`

---

> Good luck! Use Pandas to implement each function in `main.py` and follow the doc hints above. Make sure your printed output matches the required fields for each step.
