
# Day 14 — Python and APIs
# Havilah Club Internship
# Student: Enyichukwu Samuel
# Project: Book Search Utility

import requests

BASE_URL = "https://openlibrary.org/search.json"


# Step 1: Fetch Data

def fetch_data(query):
    params = {
        "q": query,
        "limit": 3,
        "fields": "title,author_name,first_publish_year,edition_count"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=15
        )

        print("\nHTTP Status Code:", response.status_code)
        print("Request URL:", response.url)

        if response.status_code == 200:
            data = response.json()

            # Inspect the JSON response
            print("\n--- RAW JSON RESPONSE ---")
            print(data)

            return data
        else:
            print("API request was unsuccessful.")
            return None

    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        return None

    except ValueError:
        print("Error: The response is not valid JSON.")
        return None


# Step 2: Parse and Display Results

def display_results(data):
    books = data.get("docs", [])

    if len(books) == 0:
        print("No books found.")
        return

    print("\n========== BOOK SEARCH RESULTS ==========")

    for book in books:
        title = book.get("title", "Unknown Title")
        authors = book.get("author_name", ["Unknown Author"])
        year = book.get("first_publish_year", "Unknown")
        editions = book.get("edition_count", 0)

        print("\nBook Title:", title)
        print("Author:", ", ".join(authors))
        print("First Published:", year)
        print("Number of Editions:", editions)
        print("----------------------------------------")


# Main Program

def main():
    print("WELCOME TO THE BOOK SEARCH UTILITY")

    query = input("Enter a book title or topic: ").strip()

    if query == "":
        print("Please enter a search term.")
        return

    data = fetch_data(query)

    if data is not None:
        display_results(data)


if __name__ == "__main__":
    main()
