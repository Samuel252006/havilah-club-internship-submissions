
# Day 13 — Working With Data
# Havilah Club Internship
# Student: Enyichukwu Samuel

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# Step 1: Load and clean CSV data

def load_data(filepath):
    rows = []

    with open(filepath, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Clean product names
            name = row["name"].strip()
            name = name.replace("_", " ")
            name = name.replace("-", " ")
            name = name.replace("/", " ")
            row["name"] = name.title()

            # Clean category names
            row["category"] = row["category"].strip().lower()

            # Convert numerical values
            row["price"] = float(row["price"].strip())
            row["quantity"] = int(row["quantity"].strip())

            rows.append(row)

    return rows


# Step 2: Print data summary

def print_summary(rows):
    prices = []

    for row in rows:
        prices.append(row["price"])

    total_products = len(rows)

    if total_products == 0:
        print("No products found.")
        return

    minimum_price = min(prices)
    maximum_price = max(prices)
    average_price = sum(prices) / total_products

    print("\n========== PRODUCT DATA SUMMARY ==========")
    print("Total Products:", total_products)
    print("Minimum Price:", minimum_price)
    print("Maximum Price:", maximum_price)
    print("Average Price:", round(average_price, 2))
    print("==========================================")


# Step 3: Filter products priced at 30 or above

def filter_data(rows):
    filtered = []

    for row in rows:
        if row["price"] >= 30:
            filtered.append(row)

    print("\n--- PRODUCTS PRICED AT 30 OR ABOVE ---")

    for product in filtered:
        print(
            product["name"],
            "- Price:", product["price"],
            "- Quantity:", product["quantity"],
            "- Category:", product["category"]
        )

    return filtered


# Step 4: Sort and export results

def save_data(rows, filepath):
    sorted_rows = sorted(
        rows,
        key=lambda row: row["price"],
        reverse=True
    )

    with open(filepath, "w", newline="") as file:
        fieldnames = ["name", "price", "quantity", "category"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(sorted_rows)


# Main program

def main():
    rows = load_data(INPUT_FILE)

    print_summary(rows)

    filtered = filter_data(rows)

    save_data(filtered, OUTPUT_FILE)

    print(
        f"\nDone. {len(filtered)} products written to {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
