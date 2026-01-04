import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def load_data():
    df = sns.load_dataset("penguins")
    df = df.dropna()
    print("Dataset loaded and cleaned successfully!\n")
    print("Sample Data (first 5 rows):")
    cols = ["species", "bill_length_mm", "bill_depth_mm", "body_mass_g"]
    print(df[cols].head().to_string())
    return df


def plot_bill_comparison(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species", palette="deep", s=100)
    plt.title("Bill Length vs. Bill Depth by Penguin Species")
    plt.xlabel("Bill Length (mm)")
    plt.ylabel("Bill Depth (mm)")
    plt.savefig("bill_comparison.png")
    print("Scatter plot saved as: bill_comparison.png")


def plot_body_mass_distribution(df):
    plt.figure(figsize=(8, 6))
    ax = sns.boxplot(data=df, x="species", y="body_mass_g", hue="species", palette="Set2")
    if ax.get_legend():
        ax.get_legend().remove()
    plt.title("Body Mass Distribution by Penguin Species")
    plt.ylabel("Body Mass (g)")
    plt.savefig("body_mass_distribution.png")
    print("Box plot saved as: body_mass_distribution.png")


def embed_images_in_md():
    try:
        md_path = "ques4.md"
        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()
        changed = False
        if "![](bill_comparison.png)" not in text:
            text += "\n\n![](bill_comparison.png)\n"
            changed = True
        if "![](body_mass_distribution.png)" not in text:
            text += "\n\n![](body_mass_distribution.png)\n"
            changed = True
        if changed:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(text)
    except Exception:
        pass


if __name__ == '__main__':
    print('Penguin Species Explorer Project\n')
    df = load_data()
    plot_bill_comparison(df)
    plot_body_mass_distribution(df)
    embed_images_in_md()
