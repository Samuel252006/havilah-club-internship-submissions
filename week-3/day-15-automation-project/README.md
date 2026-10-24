# Day 15 — Python Automation Project

**Student:** Enyichukwu Samuel
**Project:** Student Performance Report Generator

## What Does This Project Do?

This Python program automatically reads student records from a CSV file, calculates basic performance statistics, and generates a formatted text report.

It helps organise student performance information without manually calculating each statistic.

## Project Type

**Option B — Report Generator**

## Automation Plan

**Input:** A CSV file containing at least eight student records with `name` and `score` columns.

**Process:**

1. Read the CSV file using `csv.DictReader`.
2. Convert student scores to numerical values.
3. Calculate the number of students, average score, highest score and lowest score.
4. Prepare a formatted report.

**Output:** A text file saved as `data/output/report.txt`.

**Edge Cases:**

- Missing input CSV file.
- Empty CSV file or no student records.
- Missing required columns or invalid numerical values.
- Failure to save the output file.

## Requirements

- Python 3
- Python's built-in `csv` and `os` modules

No additional libraries or `pip install` commands are required.

## How to Run



Open the Day 15 project folder and run:

```bash
python main.py
```

The program automatically reads `data/scores.csv` and generates the report.

## Expected Output

```text
===== STUDENT PERFORMANCE REPORT =====
Total Students: 10
Average Score: 77.40  
Highest Score: 94.0
Lowest Score: 55.0
======================================
```

The results are saved in `data/output/report.txt`.

## Error Handling

The program checks whether the input CSV exists and contains usable records. It also handles missing required columns, invalid scores, and file-writing errors.

If the input is unavailable or invalid, the program displays an error message instead of generating a misleading report.

## Testing

The program will be tested using normal input and deliberate edge cases. Actual testing results will be documented after execution.

## Conclusion

This project demonstrates how Python can automate a sequence of tasks, from reading input data to processing it and generating a useful output.

It applies concepts from the previous Python classes, including functions, CSV processing, conditions, file handling and basic error handling.\*

### Issue — Input File Not Found When Running From Another Directory

**Problem:** The program successfully generated the student report when executed from the Day 15 folder but displayed `Error: Input CSV file was not found` when executed from the repository root.

**Cause:** The input and output paths were relative to the terminal's current working directory.

**Solution:** Used Python's built-in `os.path.abspath()`, `os.path.dirname()`, and `os.path.join()` to construct paths relative to the location of `main.py`.

**Lesson learned:** File paths must be handled carefully because a Python script may be executed from different working directories.
## Testing, Errors Encountered and Solutions

The automation was tested in GitHub Codespaces using a custom CSV containing 10 student records with the columns `name`, `score`, `subject`, `department`, and `course_code`.

### Successful Execution

The program successfully processed all 10 records and generated a text report containing:

- Total students: 10
- Average score: 77.40
- Highest score: 94
- Lowest score: 55

The generated report was verified by opening `data/output/report.txt`.

### Issue 1 — Input File Not Found

**Problem:** The program initially displayed `Error: Input CSV file was not found`.

**Cause:** The input file was initially missing. Later, the program also failed when executed from the repository root because it used relative paths.

**Solution:** Created the required `data/scores.csv` file and updated the program to build file paths relative to the location of `main.py` using Python's `os.path` functions.

**Result:** The program subsequently ran successfully from both the repository root and Day 15 directory.

### Issue 2 — Missing Input File

**Test:** Used a filename that did not exist: `data/missing.csv`.

**Result:** The program displayed the appropriate file-not-found message and stopped without generating a new report.

### Issue 3 — Invalid Student Score

**Test:** Created a temporary CSV containing a score written as `invalid`.

**Result:** The program displayed `Error: Invalid or missing score in the CSV file` and stopped without generating a new report.

**Lesson:** Numerical values must be converted carefully, and invalid values should be handled using `try/except`.

### Final Verification

After the error-handling tests, the original program was executed again using the correct dataset.

It successfully generated the same report, confirming that the temporary tests had not affected the original input data.

### What I Learned

This project helped me understand how to automate a complete data-processing workflow, organise tasks into functions, handle file paths correctly, process CSV records, calculate statistics and save useful reports.

It also demonstrated why testing both normal conditions and error scenarios is important.
### Issue 4 — Empty CSV File

**Test:** Created a temporary empty CSV file named `test_empty.csv` and attempted to process it.

**Result:** The program displayed:

```text
Error: The CSV file is empty.
No valid student records available.
```

The automation stopped without generating a new report.

**Lesson learned:** A program should check whether the input contains usable records before performing calculations. This prevents errors such as dividing by zero.

The temporary test file was deleted afterward.

### Issue 5 — Generated Report Ignored by Git

**Problem:** The generated `report.txt` file existed but did not appear in `git status` as an untracked file.

**Cause:** The repository's `.gitignore` contained the rule `output/`, which excluded the report's directory.

**Solution:** The required report can be explicitly staged using `git add -f` without changing the repository's `.gitignore`.

**Lesson learned:** Git may ignore generated files by default, but specific files required for an assignment can be explicitly included in a commit.