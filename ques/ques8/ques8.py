import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files
import matplotlib.pyplot as plt

# 1. Load Dataset
def load_data():
    """
    Load and return the YouTube dataset.
    """
    # TODO: Load the dataset from "youtube.csv"
    path = "youtube.csv"
    df = pd.read_csv(path)
    
    print("Dataset Preview:")
    print(df.head())
    return df


# 2. Scatter Plot: Views vs Likes
def plot_scatter(df):
    """
    Create a scatter plot comparing Views vs Likes.
    Marker size proportional to comment count + slight transparency.
    """
    # TODO: Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10,6))

    # TODO: Create a scatter plot
    # - x: views
    # - y: likes
    # - s (size): 0.3 times of comment_count
    # - color: purple
    # - alpha: 0.5 for transparency
    # - edgecolors: black
    plt.scatter(
        x=df['views'],
        y=df['likes'],
        s = 0.3 * df['comment_count'],
        color= 'purple',
        alpha=0.5,
        edgecolors= 'black'
    )


    # TODO: Add Title, X-label, and Y-label
    plt.title("Views vs Likes (Size = Comment Count)")
    plt.xlabel("Views")
    plt.ylabel("Likes")

    # TODO: Enable grid with alpha=0.5
    plt.grid(True,alpha=0.5)

    # TODO: Set Axis Limits
    # xlim: 0 to 110% of max views
    # ylim: 0 to 110% of max likes
    plt.xlim(0, (1.1*df['views'].max()))
    plt.ylim(0, (1.1*df['likes'].max()))

    # TODO: Save the plot as "scatter_plot.png"
    plt.savefig('scatter_plot.png')

    print("Chart saved: scatter_plot.png")


# 3. Side-by-Side Bar Chart
def bar_chart_side_by_side(df):
    """
    Compare Likes and Comments per video using side-by-side bars.
    """
    titles = df["title"]
    likes = df["likes"]
    comments = df["comment_count"]

    # We are creating an array of indices for the X-axis (0 to len(titles))
    x = np.arange(len(titles)) 

    # Width of the bars
    width = 0.35

    # TODO: Set figure size to 12 inches by 6 inches
    plt.figure(figsize=(12,6))

    # TODO: Plot 'Likes' bars shifted to the LEFT with color = skyblue
    plt.bar(
        x - width/2,
        likes,
        width=width,
        color="skyblue",
        label="Likes"
    )
    # TODO: Plot 'Comments' bars shifted to the RIGHT with color = orange
    plt.bar(
        x + width/2,
        comments,
        width=width,
        color="orange",
        label="Comments"
    )

    # TODO: Add Title, X-label, and Y-label
    plt.title("Engagement Analysis: Likes vs Comments")
    plt.xlabel("Video Title")
    plt.ylabel("Count")

    
    # TODO: Set X-axis ticks to be the video titles, rotated vertically
    plt.xticks(x, titles, rotation=90)
    
    # TODO: Show Legend
    plt.legend()


    # Show grid with alpha=0.7 and show only horizontal lines
    plt.grid(axis="y", alpha=0.7)
    plt.tight_layout()

    # We are adjusting layout to prevent clipping of tick-labels using tight_layout()
    plt.tight_layout()

    # TODO: Save the plot as "bar_chart.png"
    plt.savefig("bar_chart.png")

    print("Chart saved: bar_chart.png")


if __name__ == "__main__":
    print("YouTube Content Strategy Analyzer...\n")

    # Load Data
    df = load_data()

    if df is not None:
        # Scatter Plot: Views vs Likes 
        plot_scatter(df)

        # Bar Chart: Likes vs Comments
        bar_chart_side_by_side(df)


