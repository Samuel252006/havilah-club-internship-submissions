# Day 15 — Python Automation Project

**Student:** Enyichukwu Samuel

**GitHub Username:** Samuel252006

**Project:** Student Performance Report Generator

**Project Type:** Option B — Report Generator

**Programme:** Havilah Club Internship — Week 3

## 1. Project Description

This project is a Python automation tool that reads student records from a CSV file, calculates basic performance statistics, and automatically generates a formatted text report.

It reduces the need for manually calculating student statistics and demonstrates how Python can automate repetitive data-processing tasks.

## 2. Automation Plan

The automation follows the structure:

**Input → Process → Output → Edge Cases**

### Input

A CSV file named `data/scores.csv` containing 10 student records with the following columns:

- `name` — Student's name
- `score` — Student's numerical score
- `subject` — Subject associated with the record
- `department` — Student's department
- `course_code` — Course identification code

The program uses the `name` and `score` fields for processing. The other columns provide additional information.

### Process

1. Read the CSV file using `csv.DictReader`.
2. Check that the required columns exist.
3. Convert student scores into numerical values.
4. Calculate the total number of students.
5. Calculate the average, highest, and lowest scores.
6. Format the statistics into a readable report.

### Output

A text report saved automatically to:

`data/output/report.txt`

### Edge Cases

The program handles several situations that may prevent successful processing:

- Missing input CSV file.
- Empty CSV file or no usable student records.
- Missing required CSV columns.
- Blank student names or invalid numerical scores.
- Errors while creating or writing the output file.

## 3. Requirements

- Python 3
- Python's built-in `csv` module
- Python's built-in `os` module

No additional libraries or `pip install` commands are required.

## 4. Project Structure

```text
day-15-automation-project/
├── main.py
├── README.md
├── test_submission.py
└── data/
    ├── scores.csv
    └── output/
        └── report.txt
```

**File descriptions:**

- `main.py` — Contains the Python automation program.
- `README.md` — Provides instructions, project information and test documentation.
- `test_submission.py` — Original instructor-provided submission checks, not modified.
- `data/scores.csv` — Contains the input dataset.
- `data/output/report.txt` — Contains the generated performance report.

The original `data/.gitkeep` file is also retained in the repository.

## 5. How to Run

The project was developed and manually tested using GitHub Codespaces.

### Method 1 — From the Day 15 Folder

Open a terminal in the Day 15 project folder and run:

```bash
python main.py
```

### Method 2 — From the Repository Root

Run:

```bash
python week-3/day-15-automation-project/main.py
```

Both methods work because the program constructs file paths relative to the location of `main.py`.

The input data is read automatically, and the generated report is saved in the output folder.

## 6. Functions Used

The automation uses five clearly named functions.

| Function | Purpose |
|---|---|
| `load_data(filepath)` | Reads and validates student records from the CSV file |
| `generate_report(students)` | Calculates statistics and formats the report |
| `save_report(report, output_path)` | Creates the output directory and writes the report |
| `process(input_path, output_path)` | Coordinates loading, processing and saving |
| `main()` | Starts the automation and displays its completion status |

The program applies functions, loops, conditional statements, lists, dictionaries and `try/except` error handling.

## 7. Example Output

The program successfully processed all 10 student records and generated the following report:

```text
===== STUDENT PERFORMANCE REPORT =====
Total Students: 10
Average Score: 77.40
Highest Score: 94.0
Lowest Score: 55.0
======================================
```

The output was saved to `data/output/report.txt`.

The generated file was opened and checked to confirm that its contents matched the report displayed in the terminal.

## 8. Testing, Errors Encountered and Solutions

The project was manually tested in GitHub Codespaces using normal input and deliberately introduced error scenarios.

### Test 1 — Initial Input File Not Found

**Problem:** During the first execution, the program displayed:

```text
Error: Input CSV file was not found.
No valid student records available.
Automation could not be completed.
```

**Cause:** The required `data/scores.csv` file had not yet been created at the expected location.

**Solution:** Created the CSV file using a custom dataset containing 10 student records.

**Result:** The program successfully located and processed the dataset.

**Status:** Resolved.

### Test 2 — Running the Program From Different Directories

**Problem:** The program ran correctly from the Day 15 folder but initially failed when executed from the repository root.

**Cause:** The original input and output paths were relative to the terminal's current working directory.

**Solution:** Updated the path configuration using Python's built-in functions:

```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_PATH = os.path.join(BASE_DIR, "data", "scores.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output")
```

These functions locate the input and output files relative to the Python script.

**Result:** The program successfully generated identical reports when executed from both the repository root and the Day 15 folder.

**Status:** Passed.

### Test 3 — Normal CSV Processing

**Input:** The complete `scores.csv` containing 10 student records.

**Result:** The automation calculated:

- Total students: 10
- Average score: 77.40
- Highest score: 94.0
- Lowest score: 55.0

It successfully created the output text file and displayed `Done.`

**Status:** Passed.

### Test 4 — Missing Input File

**Test:** Attempted to process a nonexistent file named `data/missing.csv`.

**Result:**

```text
Error: Input CSV file was not found.
No valid student records available.
```

The program stopped without generating a new report.

**Lesson learned:** `FileNotFoundError` can be handled using `try/except` to prevent an unhandled crash when an input file is unavailable.

**Status:** Passed.

### Test 5 — Invalid Student Score

**Test:** Created a temporary CSV file containing an invalid numerical value.

```csv
name,score
Amaka,78
Tunde,invalid
```

**Result:**

```text
Error: Invalid or missing score in the CSV file.
No valid student records available.
```

The program stopped without generating a new report.

**Lesson learned:** Numerical values should be validated before calculations. Conversion errors can be handled using `ValueError`.

The temporary test file was deleted afterward.

**Status:** Passed.

### Test 6 — Empty CSV File

**Test:** Created an empty temporary CSV file named `test_empty.csv`.

**Result:**

```text
Error: The CSV file is empty.
No valid student records available.
```

The program stopped without generating a new report.

**Lesson learned:** Checking for available records prevents invalid calculations, such as division by zero.

The temporary test file was deleted afterward.

**Status:** Passed.

### Test 7 — Final Normal Execution

After the error-handling tests, the original program was executed again using the complete dataset.

**Result:** The program successfully processed all 10 student records and generated the same report with the expected statistics.

This confirmed that the temporary testing activities did not affect the original dataset.

**Status:** Passed.

## 9. GitHub Troubleshooting

### Generated Report Ignored by Git

**Problem:** The generated `report.txt` existed in the project folder but did not appear as an untracked file when running `git status`.

**Investigation:**

```bash
git check-ignore -v data/output/report.txt
git ls-files data/output/report.txt
```

**Cause:** The repository's `.gitignore` contained the rule `output/`, which excluded the generated report folder.

**Solution:** Explicitly staged the required report using:

```bash
git add -f data/output/report.txt
```

This allowed the file to be included in the commit without changing the repository's existing `.gitignore` rules.

**Result:** The generated report was successfully committed and pushed to GitHub.

**Lesson learned:** Git may ignore generated files by default, but a specific file required for submission can be force-added without removing the ignore rule.

## 10. Key Lessons Learned

Through this project, I practised:

1. Planning an automation using Input → Process → Output.
2. Reading structured CSV data using Python.
3. Converting text-based numbers into numerical values.
4. Calculating statistics using `len()`, `sum()`, `max()` and `min()`.
5. Organising Python code into reusable functions.
6. Creating folders and writing text files.
7. Handling missing files, invalid values and empty datasets.
8. Building reliable file paths using the `os.path` functions.
9. Testing both normal execution and deliberate error scenarios.
10. Investigating Git ignore rules and staging required output files.

## 11. Conclusion

Day 15 helped me combine several Python concepts into a complete automation project.

I successfully developed a Student Performance Report Generator that reads CSV data, calculates important statistics and saves a formatted report automatically.

The program was manually tested under normal conditions and multiple error scenarios. Problems involving input files, file paths, invalid values and Git staging were identified and resolved.

The completed project was documented, committed and successfully pushed to my GitHub fork.

This exercise strengthened my understanding of Python automation, data processing, file handling, debugging and version control.