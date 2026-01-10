# Hello developers! Welcome to the **Weekly Fitness Progress Analyzer Project!** 🏃‍♀️📊

Chef is building a fitness analytics tool to understand daily physical activity. Fitness apps track thousands of steps every day, but raw numbers alone are hard to read.

Chef wants a tool that can instantly analyze a week's worth of data to:

1. **See the Total steps** for the week.
2. **Find the Average** daily activity.
3. **Identify Which Day** was the most active (Peak Performance) vs. the least active (Rest Day).
4. **See the step counts sorted** from lowest to highest.

Your task is to use the **NumPy** library to transform raw data into these meaningful fitness insights.

---

## What's Already Provided

You are given a single file: `main.py`

- All required **function names** are already defined.
- The program flow and print statements are set up for you.
- You only need to **fill in the missing logic (TODO)** using the NumPy Library.
- **Do NOT** change function names or print statements.

## Dataset

You will not load an external file. Instead, you will generate the data:

- **Data Type:** Daily step counts for **7 days** (1 week).
- **Values:** Random integers between **3000 and 12000**.

---

## Your Tasks

Open `main.py` and complete the missing logic marked with `TODO`.

1. **Generate Step Data**

Inside `generate_step_data()`:

- Generate **7 random integers** representing daily steps.
- The steps should be between **3000 and 12000**.
- The random seed is fixed (`np.random.seed(42)`), so we get the same random numbers every time.

Docs: `np.random.randint()`

2. **Reshape Weekly Data**

Inside `reshape_weekly_data()`:

- Convert the 1D array (7 items) into a **2D Matrix** with shape `(1, 7)`.
- This represents **1 week** with **7 days**.

Docs: `numpy.reshape()`

3. **Weekly Analysis**

Inside `analyze_weekly_data()`:

- Calculate the **sum** of steps (Total Weekly Steps) along rows.
- Calculate the **mean** of steps (Average Daily Steps) along rows.

Docs: `numpy.sum()` | `numpy.mean()`

4. **Identify Peak Activity**

Inside `find_peak_activity()`:

- Find the **index** (day number) of the maximum value.
- Find the **index** (day number) of the minimum value.

Docs: `np.argmax()` | `np.argmin()`

5. **Sort Data**

Inside `sort_step_counts()`:

- Sort the daily steps in **ascending order** (lowest to highest).

Docs: `np.sort()`

---

## Expected Output

```
Weekly Fitness Progress Analyzer...

Daily Step Counts (Raw): [10270 3860 8390 8191 8734 9265 3466]
Weekly Matrix Shape: (1, 7)

Total Weekly Steps: 52176
Average Daily Steps: 7453.71

Most Active Day Index: 0 (Steps: 10270)
Least Active Day Index: 6 (Steps: 3466)

Sorted Steps: [ 3466 3860 8191 8390 8734 9265 10270]
```

Good luck and have fun building the analyzer! ✅
