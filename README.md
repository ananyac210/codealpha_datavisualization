# CodeAlpha Data Analytics Internship — Data Visualization

## Overview

This project was completed as part of the **CodeAlpha Data Analytics Internship**.

The objective was to create meaningful visualizations from the scraped book dataset and identify patterns in book prices, ratings, and categories.

## Visualizations Created

The project includes the following charts:

1. Average Price by Category
2. Price Distribution
3. Price vs. Rating
4. Rating Distribution
5. Top Categories by Number of Books

All generated charts are available in the `charts/` folder.

## Dataset

The visualization project uses the book dataset containing **1,000 book records**.

The dataset includes information such as:

* Book title
* Price
* Rating
* Availability
* Category

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## Files

```text id="2d8m6j"
codealpha_datavisualization/
├── README.md
├── visualize.py
├── books_data.csv
└── charts/
    ├── avg_price_by_category.png
    ├── price_distribution.png
    ├── price_vs_rating.png
    ├── rating_distribution.png
    └── top_categories.png
```

## Setup

Install the required libraries:

```bash id="p5u3x1"
pip install pandas matplotlib seaborn
```

## Usage

Run the visualization script with:

```bash id="g0u7n2"
python visualize.py
```

The generated charts are saved automatically in the `charts/` folder.

## Output

The project provides visual representations of:

* Book price distribution
* Average prices across categories
* Relationship between price and rating
* Distribution of book ratings
* Most frequently occurring categories

## Internship Task

**CodeAlpha Data Analytics Internship — Task 3: Data Visualization**
