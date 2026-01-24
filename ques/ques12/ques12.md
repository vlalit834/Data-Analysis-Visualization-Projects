# ✈️ FlightFlow Analysis Project

Welcome to **Project 2: FlightFlow Analysis** 📊✈️
In this project, you will analyze real-world flight delay data using **Python and Pandas** to uncover meaningful insights about airline reliability and travel delays.

---

## 📌 Project Overview

Air travel plays a crucial role in today’s fast-paced world, but delays can quickly turn a smooth journey into a frustrating experience.

Chef is planning multiple **domestic and international trips**. To avoid unnecessary delays, he has collected real-world flight data containing information such as:

* Flight dates
* Airlines
* Departure delays

Your task is to **clean, analyze, and extract insights** from this dataset using the **Pandas library**.

---

## 📂 What’s Already Provided

You are given **one file**:

* `main.py`

### Important Notes:

* ✅ All required **function names are already defined**
* ✅ Program flow is already set up
* ❗ You only need to **complete the missing logic using Pandas**
* ❌ **Do NOT change function names or print statements**

---

## 📊 Dataset Information

You will work with a CSV file named:

```
flights.csv
```

### Columns Description

| Column Name      | Description                              |
| ---------------- | ---------------------------------------- |
| `FlightDate`     | Date of the flight (`YYYY-MM-DD`)        |
| `Airline`        | Name of the airline                      |
| `Origin`         | Departure airport / city code            |
| `Destination`    | Arrival airport / city code              |
| `DepartureDelay` | Delay in minutes (NaN means **on time**) |
| `Cancelled`      | 0 = Not cancelled, 1 = Cancelled         |

---

### 📄 Dataset Preview (First 5 Rows)

```
FlightDate,Airline,Origin,Destination,DepartureDelay,Cancelled
2024-04-02,Akasa Air,DOH,SIN,103,1
2024-01-04,Singapore Airlines,JFK,DOH,20,0
2024-05-24,Akasa Air,SIN,LHR,57,1
2024-02-03,IndiGo,LHR,MUM,31,1
2024-04-07,Singapore Airlines,LHR,BLR,15,0
```

---

## 🧠 Tasks to Implement

### 1️⃣ Load Flight Data

**Function:** `load_flight_data(filename)`

* Load the CSV file using Pandas
* Convert `FlightDate` to datetime format (`YYYY-MM-DD`)

📚 Docs:

* `pandas.read_csv()`
* `pandas.to_datetime()`

---

### 2️⃣ Clean Delay Data

**Function:** `clean_delay_data(df)`

* Treat missing (`NaN`) values in `DepartureDelay` as **0 minutes**
* This indicates the flight was **on time**

📚 Docs:

* `fillna()`

---

### 3️⃣ Extract Day Features

**Function:** `extract_day_features(df)`

* Extract **day name** from `FlightDate`
* Store it in a new column: `Day_Name`

📌 Example:

* `2024-01-01` → Monday
* `2024-01-02` → Tuesday

📚 Docs:

* `pandas.Series.dt.day_name()`

---

### 4️⃣ Airline Reliability Analysis

**Function:** `airline_reliability_stats(df)`

For each airline, calculate:

* `Avg_Delay` → Mean of `DepartureDelay`
* `Total_Flights` → Number of flights

#### Requirements:

* Group by `Airline`
* Round average delay to **2 decimal places**

📚 Docs:

* `groupby()`
* `agg()`
* `round()`

---

### 5️⃣ Rank Airlines by Reliability

**Function:** `rank_airlines(stats_df)`

* Rank airlines from:

  * ✅ **Most reliable** (lowest average delay)
  * ❌ **Least reliable** (highest average delay)
* Sort data so **lowest average delay appears at the top**

📚 Docs:

* `sort_values()`

---

### 6️⃣ Identify Worst Days to Fly

**Function:** `identify_delayed_days(df)`

* Calculate **average delay** for each day of the week
* Sort days from **highest delay to lowest**
* Round values to **2 decimal places**

📚 Docs:

* `groupby()`
* `mean()`
* `sort_values()`

---

## ✅ Expected Output

```
### FlightFlow Analysis ###

Data Loaded & Cleaned: 250 flights processed.

Most Reliable Airlines (Lowest Avg Delay):

                Avg_Delay   Total_Flights
Airline
Qatar Airways      38.88            24
Emirates           44.04            25
IndiGo             48.28            25

Least Reliable Airlines (Highest Avg Delay):

                Avg_Delay   Total_Flights
Airline
Akasa Air          58.12            24
Lufthansa          62.95            19
British Airways    71.11            28

Worst Days to Fly (Highest Avg Delay):

Day_Name
Friday     65.28
Tuesday    57.11
Saturday   56.27
Name: DepartureDelay, dtype: float64
```

---

## 🚀 Goal

By completing this project, you will gain hands-on experience with:

* Data cleaning using Pandas
* Grouping & aggregation
* Sorting & ranking insights
* Real-world data analysis workflows

Happy Coding! 🎯🐼
