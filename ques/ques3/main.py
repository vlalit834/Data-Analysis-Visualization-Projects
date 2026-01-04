import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import os
import matplotlib.pyplot as plt

# Ensure plots directory exists relative to this script
BASE_DIR = os.path.dirname(__file__)
PLOTS_DIR = os.path.join(BASE_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)


# 1. Load Data
def load_sales_data():
    """
    Returns lists of months and sales figures.
    """
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] 
    sales = [12000,15000,17000,16000,18000,20000,22000,21000,19000,23000,25000,27000]
    
    return months, sales


# 2. Line Plot (Trend)
def plot_sales_trend(months, sales):
    """
    Create a line chart and save it to a file inside plots/.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(
        months,
        sales,
        color='b',
        marker='o',
        linestyle='-',
        linewidth=2,
        label="Monthly Sales"
    )

    plt.title("Monthly Sales Trend (2025)")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")
    plt.grid(True)
    plt.legend()

    filename = os.path.join(PLOTS_DIR, "sales_trend.png")
    plt.savefig(filename)
    
    print(f"Chart saved: {filename}")


# 3. Bar Chart (Comparison)
def plot_sales_bar_chart(months, sales):
    """
    Create a bar chart and save it to a file inside plots/.
    """
    plt.figure(figsize=(10,6))
    plt.bar(
        months,
        sales,
        color='orange',
        label="Monthly Sales"
    )

    plt.title("Monthly Sales Comparison")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")
    plt.grid(True)
    plt.legend()

    filename = os.path.join(PLOTS_DIR, "sales_bar_chart.png")
    plt.savefig(filename)
    
    print(f"Chart saved: {filename}")


if __name__ == "__main__":
    print("Monthly Sales Visualization Project\n")
    months, sales = load_sales_data()
    plot_sales_trend(months, sales)
    plot_sales_bar_chart(months, sales)
