"""
CodeAlpha Data Analytics Internship - Task 3: Data Visualization
--------------------------------------------------------------------
Turns books_data.csv into a set of charts for a portfolio / report.

Requirements:
    pip install pandas matplotlib seaborn

Usage:
    python visualize.py   (run AFTER scraper.py has created books_data.csv)

Output:
    charts/price_distribution.png
    charts/rating_distribution.png
    charts/avg_price_by_category.png
    charts/price_vs_rating.png
    charts/top_categories.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_PATH = "books_data.csv"
OUT_DIR = "charts"

sns.set_theme(style="whitegrid")


def ensure_output_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def plot_price_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["price_gbp"], bins=30, kde=True, color="steelblue")
    plt.title("Distribution of Book Prices")
    plt.xlabel("Price (£)")
    plt.ylabel("Number of Books")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/price_distribution.png", dpi=150)
    plt.close()


def plot_rating_distribution(df):
    plt.figure(figsize=(7, 5))
    order = sorted(df["rating"].dropna().unique())
    sns.countplot(x="rating", data=df, order=order, hue="rating",
                  palette="viridis", legend=False)
    plt.title("Distribution of Book Ratings")
    plt.xlabel("Rating (stars)")
    plt.ylabel("Number of Books")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/rating_distribution.png", dpi=150)
    plt.close()


def plot_avg_price_by_category(df, top_n=10):
    top_cats = df["category"].value_counts().head(top_n).index
    subset = df[df["category"].isin(top_cats)]
    avg_price = subset.groupby("category")["price_gbp"].mean().sort_values(ascending=False)

    plt.figure(figsize=(9, 6))
    sns.barplot(x=avg_price.values, y=avg_price.index, hue=avg_price.index,
                palette="mako", legend=False)
    plt.title(f"Average Price by Category (Top {top_n} Categories)")
    plt.xlabel("Average Price (£)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/avg_price_by_category.png", dpi=150)
    plt.close()


def plot_top_categories(df, top_n=10):
    cat_counts = df["category"].value_counts().head(top_n)
    plt.figure(figsize=(9, 6))
    sns.barplot(x=cat_counts.values, y=cat_counts.index, hue=cat_counts.index,
                palette="crest", legend=False)
    plt.title(f"Top {top_n} Categories by Number of Books")
    plt.xlabel("Number of Books")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/top_categories.png", dpi=150)
    plt.close()


def plot_price_vs_rating(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="rating", y="price_gbp", data=df, hue="rating",
                palette="flare", legend=False)
    plt.title("Price Distribution by Rating")
    plt.xlabel("Rating (stars)")
    plt.ylabel("Price (£)")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/price_vs_rating.png", dpi=150)
    plt.close()


def main():
    df = pd.read_csv(CSV_PATH)
    ensure_output_dir()

    plot_price_distribution(df)
    plot_rating_distribution(df)
    plot_avg_price_by_category(df)
    plot_top_categories(df)
    plot_price_vs_rating(df)

    print(f"All charts saved in the '{OUT_DIR}/' folder:")
    for f in os.listdir(OUT_DIR):
        print(f" - {OUT_DIR}/{f}")


if __name__ == "__main__":
    main()
