# 📊 Exam Marks Statistics Project

Hello developers! Welcome to the **Exam Marks Statistics Project** 🎉📈

Chef is building an analytics tool to understand **student exam performance** using numerical data.  
Schools often collect exam marks, but raw numbers alone don’t provide meaningful insights.

This project uses the **NumPy library** to transform raw exam marks into useful statistical insights.

---

## 🎯 Objectives

Chef wants to analyze exam scores to:

- Understand overall class performance
- Identify high-performing students
- Detect failing students
- Find the highest and lowest scores

---

## 🧰 What’s Already Provided

You are given a single file:

- `main.py`

### Important Notes

- All required **function names are already defined**
- The **program flow is already set up**
- You only need to **fill in the missing logic (`_____`) using NumPy**
- ❌ **Do NOT change function names or print statements**

---

## 📂 Dataset




You will work with the following exam marks dataset:

```78, 85, 33, 66, 15, 88, 90, 59, 29, 70```



Each value represents a **student's exam score**.

---

## 📝 Tasks

### 1️⃣ Load Exam Marks

Inside the function `load_data()`:

- Create a NumPy array containing the given exam marks
- Return the NumPy array for reuse in other functions

📌 **Hint:** Use `np.array()`

---

### 2️⃣ Compute Class Statistics

Inside the function `compute_statistics()`:

Compute the following:

- **Average marks**
- **Median marks**
- **Standard deviation** (rounded to 2 decimal places)

📌 **Functions to use:**
- `np.mean()`
- `np.median()`
- `np.std()`
- `round()`

---

### 3️⃣ Analyze Student Performance

Inside the function `analyze_performance()`:

Using the exam marks and average marks:

- Identify students who scored **above average**
- Count how many students scored above average
- Identify students who **failed** (marks < 35)
- Count the number of failed students

📌 **Hint:** Use `len()` and NumPy filtering

---

### 4️⃣ Find Highest and Lowest Scores

Inside the function `find_extremes()`:

Determine:

- **Highest exam score**
- **Lowest exam score**

📌 **Functions to use:**
- `np.argmax()`
- `np.argmin()`

---

---

## 🚀 Tech Stack

- **Python**
- **NumPy**

---

## 🧠 Learning Outcome

By completing this project, you will learn how to:

- Use NumPy arrays for data analysis
- Compute statistical measures
- Perform data filtering and analysis
- Extract meaningful insights from raw data

Happy coding! 💻✨  
Feel free to extend this project further 🚀



