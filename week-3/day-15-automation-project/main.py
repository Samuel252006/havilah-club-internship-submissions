
# Day 15 — Python Automation Project
# Havilah Club Internship
# Student: Enyichukwu Samuel
# Project: Student Performance Report Generator

import os
import csv


# Configuration

# Get the folder containing this Python script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build paths relative to the script's location
INPUT_PATH = os.path.join(BASE_DIR, "data", "scores.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output")


# Function 1: Load Student Data

def load_data(filepath):
    students = []

    try:
        with open(filepath, "r", newline="") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: The CSV file is empty.")
                return []

            if "name" not in reader.fieldnames or "score" not in reader.fieldnames:
                print("Error: CSV must contain name and score columns.")
                return []

            for row in reader:
                name = row["name"].strip()
                score = float(row["score"].strip())

                if name == "":
                    print("Error: A student name is blank.")
                    return []

                students.append({
                    "name": name,
                    "score": score
                })

    except FileNotFoundError:
        print("Error: Input CSV file was not found.")
        return []

    except (ValueError, TypeError, AttributeError):
        print("Error: Invalid or missing score in the CSV file.")
        return []

    return students


# Function 2: Generate the Report

def generate_report(students):
    scores = []

    for student in students:
        scores.append(student["score"])

    total_students = len(students)
    average_score = sum(scores) / total_students

    highest_score = max(scores)
    lowest_score = min(scores)

    report = "===== STUDENT PERFORMANCE REPORT =====\n"
    report += f"Total Students: {total_students}\n"
    report += f"Average Score: {average_score:.2f}\n"
    report += f"Highest Score: {highest_score}\n"
    report += f"Lowest Score: {lowest_score}\n"
    report += "======================================\n"

    return report


# Function 3: Save the Report

def save_report(report, output_path):
    os.makedirs(output_path, exist_ok=True)

    report_file = os.path.join(output_path, "report.txt")

    with open(report_file, "w") as file:
        file.write(report)

    print("Report saved to:", report_file)


# Core Automation Function

def process(input_path, output_path):
    students = load_data(input_path)

    if len(students) == 0:
        print("No valid student records available.")
        return False

    report = generate_report(students)

    print("\n" + report)

    try:
        save_report(report, output_path)

    except OSError as error:
        print("Error saving report:", error)
        return False

    return True


# Main Program

def main():
    print("Starting automation...")

    if process(INPUT_PATH, OUTPUT_PATH):
        print("Done.")
    else:
        print("Automation could not be completed.")


if __name__ == "__main__":
    main()
