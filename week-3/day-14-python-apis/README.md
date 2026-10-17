# Day 14 — Python + APIs

**Student:** Enyichukwu Samuel  
**Project:** Book Search Utility  
**Programme:** Havilah Club Internship — Week 3

## 1. Project Description

This project is a Python program that connects to the Open Library Search API to search for books on different topics.

It uses the `requests` library to retrieve JSON data, extracts useful book information, and displays the results in a clear and readable format.

The project demonstrates how Python communicates with external APIs, processes JSON responses using dictionaries and lists, and handles errors that may occur during API requests.

## 2. API Information

- **API:** Open Library Search API
- **Endpoint:** https://openlibrary.org/search.json
- **Request Method:** GET
- **Authentication:** No API key required for public searches
- **Response Format:** JSON
- **Documentation:** https://openlibrary.org/dev/docs/api/search

### Parameters Used

| Parameter | Description |
|---|---|
| `q` | The book title or topic entered by the user |
| `limit` | Limits the number of returned books to three |
| `fields` | Specifies the book information requested |

### Information Extracted

The program displays four pieces of information for each book:

1. Book title
2. Author name
3. First publication year
4. Number of editions

## 3. How the Program Works

1. The user enters a book title or topic.
2. Python sends an HTTP GET request using `requests.get()`.
3. The program displays the HTTP status code and request URL.
4. If the request succeeds, the response is converted from JSON into Python data using `response.json()`.
5. The program prints the raw JSON response for inspection.
6. It accesses the book records from the `docs` list and extracts the required information.
7. The book details are displayed with descriptive labels.

The program uses two main functions:

- `fetch_data(query)` — Sends the API request, checks the response, and returns the JSON data.
- `display_results(data)` — Extracts and displays the useful book information.

The `main()` function collects the user's search term and calls the appropriate functions.

The program also uses `try` and `except` to handle network errors and invalid JSON responses without crashing.

## 4. Setup and Execution

The project was developed and tested using GitHub Codespaces.

### Step 1 — Open the Project Folder

From the repository root:

```bash
cd week-3/day-14-python-apis
```

### Step 2 — Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install Requests

```bash
python -m pip install requests
```

### Step 4 — Run the Program

```bash
python main.py
```

Enter a book title or topic when prompted.

The `.venv` folder is ignored by Git and must not be uploaded to GitHub.

## 5. Successful API Tests

The program was executed successfully in GitHub Codespaces using two different search terms.

| Search Query | HTTP Status | Books Displayed |
|---|---|---|
| Python programming | 200 | Core Python Programming; Black Hat Python; Core Python programming |
| Robotics | 200 | I, Robot; The Robots of Dawn; Robots and Empire |

Both requests returned valid JSON responses.

The program successfully extracted book titles, author names, publication years, and edition counts.

Changing the search query produced different results, confirming that the program correctly sends and processes different API requests.

## 6. Testing, Errors Encountered and Solutions

In addition to successful requests, the program was tested using deliberately introduced errors and unusual inputs to understand how it responds when something goes wrong.

### Test 1 — Python Could Not Find `main.py`

**Problem:** Running `python main.py` from the repository root produced the following error:

```text
python: can't open file '/workspaces/havilah-club-internship-submissions/main.py': [Errno 2] No such file or directory
```

**Cause:** The script was located inside `week-3/day-14-python-apis/`, not the repository root.

**Solution:** Changed into the correct folder before running the program:

```bash
cd week-3/day-14-python-apis
python main.py
```

**Lesson learned:** Python needs the correct file path to locate and execute a script.

### Test 2 — Empty Search Input

**Test:** Submitted an empty search term by pressing Enter without typing anything.

**Result:** The program displayed:

```text
Please enter a search term.
```

The program exited without sending an API request.

**Lesson learned:** Checking user input before processing it prevents unnecessary requests.

### Test 3 — Missing Book Information

**Test:** Supplied a simulated book record containing only a title.

**Result:** The program displayed:

```text
Book Title: Test Book
Author: Unknown Author
First Published: Unknown
Number of Editions: 0
```

**Lesson learned:** The `.get()` method allows dictionaries to return default values when optional fields are missing, helping the program avoid errors.

### Test 4 — Network Connection Failure

**Test:** Temporarily used `http://127.0.0.1:65534/search.json` as the API endpoint to simulate an unavailable server.

**Result:** The connection was refused, and the program displayed a network error instead of crashing.

The error included:

```text
Failed to establish a new connection: [Errno 111] Connection refused
```

**Lesson learned:** Using `try/except` with `requests.exceptions.RequestException` helps handle network failures gracefully.

### Test 5 — Invalid API Endpoint

**Test:** Sent a request to an endpoint that does not exist:

```text
https://openlibrary.org/this-endpoint-does-not-exist
```

**Result:** The API returned HTTP status code `404`.

The program displayed:

```text
API request was unsuccessful.
```

**Lesson learned:** A program should check `response.status_code` before treating a response as successful.

### Test 6 — No Matching Books

**Test:** Searched for:

```text
zzzxxyy987654321unlikelybook
```

**Result:** The API returned HTTP status code `200`, but the JSON response contained an empty `docs` list.

The program displayed:

```text
No books found.
```

**Lesson learned:** An HTTP request can succeed even when a search produces no matching records. Therefore, it is important to check both the HTTP status and the returned data.

### Test 7 — Invalid JSON Response

**Test:** Used Python's built-in `unittest.mock` module to simulate an API response with HTTP status code `200`, but with invalid JSON data.

**Result:** The program displayed:

```text
HTTP Status Code: 200
Request URL: https://example.com/test
Error: The response is not valid JSON.
```

**Lesson learned:** A successful HTTP status does not guarantee that the response contains valid JSON. Handling `ValueError` prevents the program from crashing when JSON conversion fails.

This test was simulated locally without modifying the project's source code.

### Troubleshooting Summary

| Test | Observed Result | Status |
|---|---|---|
| Python file path | Corrected working directory | Resolved |
| Empty search input | Appropriate message displayed | Passed |
| Missing JSON fields | Default values displayed | Passed |
| Network failure | Connection error handled | Passed |
| Invalid API endpoint | HTTP 404 handled | Passed |
| No matching books | Empty results handled | Passed |
| Invalid JSON response | Simulated invalid JSON was caught successfully | Passed |

These tests helped demonstrate the difference between input errors, network failures, HTTP errors, and successful requests that return no useful records.

## 7. Security

The Open Library Search API does not require an API key for public searches.

The original `.env.example` file is retained as required by the Havilah Club submission repository.

No secret API keys are needed for this project.

The `.venv` virtual environment is excluded from Git using `.gitignore`, and no `.env` file should be included in the submission.

## 8. Key Lessons Learned

Through this project, I practised:

1. Installing and using the Python `requests` library.
2. Creating and activating a Python virtual environment.
3. Sending HTTP GET requests to an external API.
4. Passing query parameters using a dictionary.
5. Checking HTTP status codes and request URLs.
6. Converting JSON responses into Python dictionaries and lists.
7. Extracting and presenting useful information.
8. Organising program logic using functions.
9. Handling errors using `try` and `except`.
10. Troubleshooting and documenting observed program behaviour.

## 9. Conclusion

Day 14 helped me understand how Python applications can retrieve and process information from external services.

By developing the Book Search Utility, I gained practical experience working with HTTP requests, APIs, JSON data, functions, and error handling.

Testing both successful requests and deliberate failure scenarios also helped me understand why input validation, response checking, and clear error messages are important when developing reliable programs.