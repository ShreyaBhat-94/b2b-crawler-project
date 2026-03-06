import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import os

#Folder for visualizations
if not os.path.exists("visualizations"):
    os.makedirs("visualizations")

# Load dataset
df = pd.read_csv("products.csv")


# Summary Statistics

print("==== Dataset Preview ====")
print(df.head())

print("\n==== Dataset Info ====")
print(df.info())

print("\n==== Summary Statistics ====")
print(df.describe())

# Count of records per category
category_counts = df['Category'].value_counts()
print("\n==== Product Counts by Category ====")
print(category_counts)

# Count of records per location
location_counts = df['Location'].value_counts()
print("\n==== Supplier Counts by Location ====")
print(location_counts)


# Common Attributes


# Top 10 product types (categories)
top_categories = df['Category'].value_counts().head(10)
print("\n==== Top 10 Categories ====")
print(top_categories)

# Top 10 price ranges
print("\n==== Price Statistics ====")
print("Min Price:", df['Price'].min())
print("Max Price:", df['Price'].max())
print("Mean Price:", round(df['Price'].mean(), 2))
print("Median Price:", df['Price'].median())
print("Standard Deviation:", round(df['Price'].std(), 2))

# Price distribution plot
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=10, kde=True, color='skyblue')
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("visualizations/price_distribution.png")
plt.show()

# Frequent keywords in product names
words = " ".join(df["Product_Name"].astype(str)).lower()
words = re.findall(r'\w+', words)
common_words = Counter(words).most_common(10)
print("\n==== Top 10 Frequent Words in Product Names ====")
for word, count in common_words:
    print(f"{word}: {count}")


# Regional Insights

plt.figure(figsize=(8,5))
sns.countplot(y='Location', data=df, order=location_counts.index, palette='Set2')
plt.title("Supplier Location Distribution")
plt.xlabel("Number of Products")
plt.ylabel("Location")
plt.tight_layout()
plt.savefig("visualizations/supplier_locations.png")
plt.show()


# Ratings Insights

print("\n==== Ratings Statistics ====")
print(df['Rating'].describe())

plt.figure(figsize=(8,5))
sns.histplot(df['Rating'], bins=5, kde=False, color='orange')
plt.title("Product Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("visualizations/ratings_distribution.png")
plt.show()


# Detect Anomalies & Data Quality
print("\n==== Missing Values ====")
print(df.isnull().sum())

print("\n==== Duplicate Records ====")
print(df.duplicated().sum())

# Price outliers using IQR
q1 = df['Price'].quantile(0.25)
q3 = df['Price'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5*iqr
upper_bound = q3 + 1.5*iqr
price_outliers = df[(df['Price'] < lower_bound) | (df['Price'] > upper_bound)]
print("\n==== Price Outliers ====")
print(price_outliers[['Product_Name','Price','Category','Supplier','Location']])

#Visualize outliers
plt.figure(figsize=(8,5))
sns.boxplot(x='Price', data=df, color='lightgreen')
plt.title("Price Outliers Detection")
plt.xlabel("Price")
plt.tight_layout()
plt.savefig("visualizations/price_outliers.png")
plt.show()