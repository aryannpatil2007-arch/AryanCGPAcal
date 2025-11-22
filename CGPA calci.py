# Function to calculate grade point from marks (assuming a 10-point scale)
def calculate_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    else:
        return 0 # Fail or below minimum passing grade

def calculate_cgpa():
    num_subjects = int(input("Enter the number of subjects: "))

    total_grade_points = 0
    total_credits = 0

    for i in range(num_subjects):
        print(f"\n--- Subject {i+1} ---")
        try:
            marks = float(input(f"Enter marks for Subject {i+1} (out of 100): "))
            credits = float(input(f"Enter credits for Subject {i+1}: "))

            if not (0 <= marks <= 100):
                print("Invalid marks. Marks should be between 0 and 100. Skipping subject.")
                continue
            if credits <= 0:
                print("Invalid credits. Credits must be positive. Skipping subject.")
                continue

            grade_point = calculate_grade_point(marks)
            total_grade_points += (grade_point * credits)
            total_credits += credits # Fixed typo: changed total_cre4dits to total_credits
        except ValueError:
            print("Invalid input. Please enter numeric values for marks and credits. Skipping subject.")
            continue

    if total_credits == 0:
        print("No valid subjects entered or total credits are zero. Cannot calculate CGPA.")
        return

    cgpa = total_grade_points / total_credits
    print(f"\nYour calculated CGPA is: {cgpa:.2f}")

# Run the CGPA calculation program
calculate_cgpa()
