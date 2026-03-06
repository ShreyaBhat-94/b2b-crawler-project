# B2B Marketplace Product Data Scraper

## Project Overview

This project collects product information from an online marketplace website and stores the extracted data in structured formats. The goal is to demonstrate how Python can be used for automated data collection and basic data processing.

The scraper retrieves product details such as product name, price, category, supplier information, location, and rating. The collected data is then saved into CSV and JSON files for further analysis.

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

---

## Features

* Sends HTTP requests to a product listing webpage
* Parses HTML content to extract product information
* Collects structured product data
* Stores the data in CSV and JSON formats
* Simple and lightweight implementation without browser automation

---

## Project Structure

```
project-folder/
│
├── scraper.py          # Main scraping script
├── products.csv        # Output dataset in CSV format
├── products.json       # Output dataset in JSON format
└── README.md           # Project documentation
```

---

## Data Fields Collected

The following product attributes are collected:

* **Product_Name** – Name of the product
* **Price** – Product price
* **Category** – Product category
* **Supplier** – Supplier or brand name
* **Location** – Supplier location
* **Rating** – Product rating

---

## Installation

1. Install Python (version 3.8 or above)

2. Install required libraries:

```
pip install requests beautifulsoup4 pandas
```

---

## How to Run the Project

Run the scraper script:

```
python scraper.py
```

After execution, the following files will be generated:

* `products.csv`
* `products.json`

---

## Sample Output

Example CSV record:

```
Product_Name,Price,Category,Supplier,Location,Rating
Industrial Drill Machine,5200,Industrial Tools,Alpha Machinery,Mumbai,4.5
```

Example JSON record:

```
{
"Product_Name": "Industrial Drill Machine",
"Price": 5200,
"Category": "Industrial Tools",
"Supplier": "Alpha Machinery",
"Location": "Mumbai",
"Rating": 4.5
}
```

---

## Use Cases

* Marketplace data analysis
* Supplier comparison
* Product pricing analysis
* Data engineering practice

---

## Author

Shreya Bhat
