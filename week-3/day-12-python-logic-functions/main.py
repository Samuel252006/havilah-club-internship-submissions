
# Day 12 — Python Logic and Functions
# Havilah Club Internship
# Student: Enyichukwu Samuel


# Function 1: Grade Calculator
# Takes a score from 0 to 100 and returns a letter grade.

def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


# Function 2: Multiplication Table
# Uses a for loop for the table and a while loop for repetition.

def multiplication_table():
    while True:
        user_input = input(
            "\nEnter a number (or type 'quit' to return): "
        )

        if user_input.lower() == "quit":
            break

        try:
            number = float(user_input)

            print("\n--- MULTIPLICATION TABLE ---")

            for multiplier in range(1, 13):
                result = number * multiplier
                print(number, "x", multiplier, "=", result)

        except ValueError:
            print("Invalid input. Please enter a number.")


# Function 3: Temperature Converter
# Receives Celsius as a parameter and returns Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Function 3: Your Choice (GitHub template)
# Uses the temperature converter required by the website.

def your_function():
    try:
        celsius = float(
            input("Enter temperature in Celsius: ")
        )

        fahrenheit = celsius_to_fahrenheit(celsius)

        print("Temperature in Fahrenheit:", fahrenheit, "°F")

    except ValueError:
        print("Invalid input. Please enter a number.")


# Main Menu
# Keeps running until the user selects Exit.

def main():
    while True:
        print("\n========== PYTHON UTILITY MENU ==========")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")
        print("=========================================")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                score = float(input("Enter score (0-100): "))
                grade = calculate_grade(score)
                print("Grade:", grade)

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            multiplication_table()

        elif choice == "3":
            your_function()

        elif choice == "4":
            print("Thank you for using the Python Utility!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
