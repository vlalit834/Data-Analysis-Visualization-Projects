# Project 3: YouTube Content Strategy Analyzer 🎯📊

Chef loves watching YouTube! He has collected data from his favourite YouTube channels to understand what makes a video successful. The dataset contains metrics like **views**, **likes**, and **comments** for various trending videos.

Chef wants you to build a visual dashboard to answer questions like:

- Which videos are watched the most?
- Do more views actually translate into more likes?
- Which videos create the most discussion?

Your task is to turn this raw data into beautiful, insightful charts!

---

## Important Notes

You are given a single file: `main.py`.

- **Do NOT change function names:** The testing system relies on them.
- **Do NOT use `plt.show()`**: This project runs in a "headless" environment (no screen). You must use `plt.savefig("filename.png")` to generate output.
- **Do NOT close the plot after saving:** Do not call `plt.close()` or similar functions after saving the plot.
- All functions are already defined in `main.py`. You need to complete the missing logic.

---

## Dataset

You will work with the file `youtube.csv`. It contains columns such as:

- `title` (Video Name)
- `channel_title` (Channel Name)
- `views` (Total Views)
- `likes` (Total Likes)
- `comment_count` (Total Comments)

---

## Your Tasks

1. **Load the YouTube Dataset**

Inside `load_data()`:

- Read the CSV file using Pandas (see `pd.read_csv()` docs).

2. **Visualize Views vs. Likes (Scatter Plot)**

Inside `plot_scatter(df)`:

- Setup: Set figure size to 10 inches by 6 inches.
- Plotting: Create a scatter plot where:
  - X-axis: `views`
  - Y-axis: `likes`
  - Size (`s`): `comment_count * 0.3` (scale down for readability)
  - Color: `"purple"`
  - Transparency (`alpha`): `0.5`
  - Edge Color: `"black"`
- Styling:
  - Title: `"Views vs Likes (Size = Comment Count)"`
  - Labels: X-label = `"Views"`, Y-label = `"Likes"`
  - Grid: Enable grid with alpha 0.5
- Limits: Stretch axes to 110% of max values ((max value of columns) * 1.1) to let the data breathe.
- Save: Save the chart as `scatter_plot.png` using `plt.savefig()`.

3. **Compare Likes vs. Comments (Side-by-Side Bar Chart)**

Inside `bar_chart_side_by_side(df)`:

- Setup: Set figure size to 12 inches by 6 inches (wider for video titles).
- Logic: We need to manually shift the bars so they don't overlap:
  - Likes: Shift left (`x - width/2`), Color: `"skyblue"`.
  - Comments: Shift right (`x + width/2`), Color: `"orange"`.
- Styling:
  - Title: `"Engagement Analysis: Likes vs Comments"`
  - Labels: X-label = `"Video Title"`, Y-label = `"Count"`
  - Rotation: Rotate x-axis labels vertically so they don't overlap.
  - Legend: Add a legend to explain the colors.
  - Grid: Enable grid **only on the Y-axis** with alpha 0.7.
- Final Touch: `plt.tight_layout()` is already provided in the template to ensure long titles aren't cut off.
- Save: Save the chart as `bar_chart.png` using `plt.savefig()`.

---

## Expected Output

When you run the code, your program should print the following messages and generate two image files in the same directory:

**Console Output:**

```
YouTube Content Strategy Analyzer...

Dataset Preview:
   title            channel_title    views   likes   dislikes   comment_count
0  The New SpotMini  BostonDynamics   75752   9419    52         1230
1  VLOG Delhi Metro  TravelIndiaYT    204889  6031    225        510
2  U2 - The Blackout  U2VEVO         60506   5389    106        455
3  NF - Let You Down  NFVEVO        1774018 40417   5002       1686
4  _ Live in the now!  poopfables   95085   7909    1652       593

Chart saved: scatter_plot.png
Chart saved: bar_chart.png
```

---

Good luck and have fun building the dashboard! 🎉
