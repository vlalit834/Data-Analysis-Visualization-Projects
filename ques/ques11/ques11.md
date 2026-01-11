# Hello developers! Welcome to Project 6: Global Salary Index Analyzer! 📊🌍

Chef is curious to understand how salaries vary around the world. He collected employee data from multiple countries - including experience, job roles, and salary figures. But staring at spreadsheets is confusing! 😵‍💫

Chef needs your help to visualize the data and uncover meaningful global salary trends using Seaborn and Matplotlib.

---

## Important Notes

- You are given a single file: `main.py`.

- **Do NOT change function names**: The testing system relies on them.
- **Do NOT use `plt.show()`**: This project runs in a "headless" environment (no screen). You must use `plt.savefig("filename.png")` to generate output.
- **Do NOT close the plot after saving**: Do not call `plt.close()` or similar functions after saving the plot.
- All functions are already defined in `main.py`. You need to complete the missing logic.

## Dataset

You will work with `global_salaries.csv`. This dataset helps us compare remote vs onsite work across skills, experience, and geography.

It contains the following columns:

- `country`: Country where the employee works
- `job_role`: Type of role (Developer, Data Scientist, etc.)
- `experience_years`: Work experience in years
- `salary_remote`: Average remote salary (USD)
- `salary_onsite`: Average onsite salary (USD)
- `remote_ratio`: Percentage of work done remotely (0-100)

---

## Your Tasks

### 1. Compare Remote vs Onsite Salaries (Bar Chart)

Inside `plot_salary_comparison(df)`:

We want to compare two values (remote vs onsite) for each country side-by-side. To do this with Seaborn, we first need to reshape our data.

- Reshape: Convert the DataFrame into "long format" using `df.melt()` and assign it to `df_long`.
  - `id_vars`: The column to keep fixed (hint: we are comparing countries).
  - `value_vars`: The two columns containing the numerical data we want to stack.
  - `var_name`: Name the new category column `"salary_type"`.
  - `value_name`: Name the new value column `"amount"`.

- Plot: Create a side-by-side bar chart using `sns.barplot()`.
  - Mappings:
    - `x`: `country`
    - `y`: `amount`
    - Color the bars based on the salary type (Explore the `hue` parameter).

- Styling:
  - Set figure size to **12 inches by 6 inches**.
  - Use the color palette: `["#e74c3c", "#2c3e50"]`.
  - Disable the error bars.
  - Add Title: `"Average Salary Comparison: Remote vs Onsite"`.
  - Add X-label `"Country"` and Y-label `"Avg Salary (USD)"`.
  - Add a grid to the Y-axis with transparency set to **0.3** (Explore the `alpha` parameter).
  - Save the plot as `salary_comparison.png`.
    - Use `bbox_inches='tight'` to avoid cutting off labels.


### 2. Analyze Experience vs Remote Salary (Scatter Plot)

Inside `plot_salary_vs_experience(df)`:

Let's see if experience pays off! We also want to visualize how much "remote work" each data point represents.

- Plot: Create a scatter plot using `plt.scatter()` and assign it to `scatter`.
  - Mappings:
    - `x`: `experience_years`
    - `y`: `salary_remote`
    - Bubble Size should represent `remote_ratio` (scale it by multiplying by **5** for visibility).

- Styling:
  - Set figure size to **10 inches by 6 inches**.
  - Set point transparency to **0.7** (Explore the `alpha` parameter).
  - Add a **black** outline to the bubbles (Explore the `edgecolors` parameter).
  - Add Title: `"Experience vs Remote Salary (Size = Remote Ratio)"`.
  - Add X-label `"Years of Experience"` and Y-label `"Remote Salary (USD)"`.
  - Add a grid with transparency set to **0.3**.
  - Save the plot as `salary_experience_scatter.png`.
    - Use `bbox_inches='tight'` to avoid cutting off labels.


### 3. Salary Distribution by Role (KDE Plot)

Inside `plot_salary_kde(df)`:

Let's use a KDE (Kernel Density Estimate) to visualize the "shape" of salary distributions. Are they spread out or clustered?

- Plot: Create a density plot using `sns.kdeplot()`.
  - Mappings:
    - `x`: `salary_onsite`
    - Draw a separate curve for each job role (Explore the `hue` parameter).
    - Shade the area under the curves (Explore the `fill` parameter).

- Styling:
  - Set figure size to **10 inches by 6 inches**.
  - Set transparency to **0.4** (Explore the `alpha` parameter).
  - Add Title: `"Salary Distribution by Job Role (KDE)"`.
  - Add X-label `"Onsite Salary (USD)"`.
  - Add a grid with transparency set to **0.3**.
  - Save the plot as `salary_kde.png`.
    - Use `bbox_inches='tight'` to avoid cutting off labels.


### 4. Role-Based Faceted Salary Trends (Relational Plot)

Inside `plot_faceted_relplot(df)`:

Instead of one messy chart, let's create a separate chart for each job role automatically!

- Plot: Use Seaborn's figure-level function `sns.relplot()` and assign the result to variable `g`.
  - Mappings:
    - `x`: `experience_years`
    - `y`: `salary_onsite`
    - Color the points based on the `country` (Explore the `hue` parameter).
    - Create a separate chart for each job role (Explore the `col` parameter).
    - This plot should be of scatter kind (Explore the `kind` parameter).

- Styling:
  - Add a Super Title to the entire figure: `"Global Salary Trends by Role & Experience"`.
  - Push the title up slightly (Explore the `y` parameter in `suptitle`, try `1.03`).
  - Save the plot as `faceted_salary_roles.png`.
    - Use `bbox_inches='tight'` to avoid cutting off labels.

---

## Expected Output

When you run the code, your program should print the following messages and generate **4 image files** in the same directory:

1. Console Output:

```
Global Salary Index Analyzer Project...

Plotting Salary Comparison...
Melted DataFrame Preview:
    country       salary_type        amount
0   United States  salary_remote     95000
1   United States  salary_remote     125000
2   United States  salary_remote     135000
3   United States  salary_remote     165000
4   United States  salary_remote     155000
Chart saved: salary_comparison.png
Plotting Salary vs Experience...
Chart saved: salary_experience_scatter.png
Plotting Salary Density (KDE)...
Chart saved: salary_kde.png
Plotting Faceted Role Trends...
Chart saved: faceted_salary_roles.png
```

2. Generated Files:

- `salary_comparison.png`
- `salary_experience_scatter.png`
- `salary_kde.png`
- `faceted_salary_roles.png`

---

Good luck and have fun exploring global salary trends! 🚀