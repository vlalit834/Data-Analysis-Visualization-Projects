import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt


def load_sales_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = [12000, 15000, 17000, 16000, 18000, 20000,
             22000, 21000, 19000, 23000, 25000, 27000]
    return months, sales


def plot_sales_trend(months, sales):
    plt.figure(figsize=(10, 6))
    plt.plot(months, sales, color='b', marker='o', linestyle='-', linewidth=2, label='Monthly Sales')
    plt.title('Monthly Sales Trend (2025)')
    plt.xlabel('Month')
    plt.ylabel('Sales Amount ($)')
    plt.grid(True)
    plt.legend()
    plt.savefig('sales_trend.png')


def plot_sales_bar_chart(months, sales):
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales, color='orange', label='Monthly Sales')
    plt.title('Monthly Sales Comparison')
    plt.xlabel('Month')
    plt.ylabel('Sales Amount ($)')
    plt.grid(True, axis='y')
    plt.legend()
    plt.savefig('sales_bar_chart.png')


if __name__ == '__main__':
    print('Monthly Sales Visualization Project\n')
    months, sales = load_sales_data()
    plot_sales_trend(months, sales)
    print('Chart saved: sales_trend.png')
    plot_sales_bar_chart(months, sales)
    print('Chart saved: sales_bar_chart.png')
