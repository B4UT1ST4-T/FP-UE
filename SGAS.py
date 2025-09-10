while True:
    # Ask for teh name of student
    name = input("Enter student name: ")

    # Input the absences and grade
    try:
        score = int(input("Enter your score (0-100): "))
    except ValueError:
        print("Invalid input. Score must be a number.")
        continue

    try:
        absences = int(input("Enter number of absences (max 5): "))
    except ValueError:
        print("Invalid input. Absences must be a number.")
        continue

    # Grade calculation
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif 0 <= score < 60:
        grade = "F"
    else:
        grade = "Invalid"

    # Fail check
    failed = False
    fail_reason = ""

    if grade == "Invalid":
        failed = True
        fail_reason = "Invalid grade entered."
    elif grade == "F":
        failed = True
        fail_reason = "Grade is F."
    elif grade == "D":
        failed = True
        fail_reason = "Grade is D."
    elif absences > 5:
        failed = True
        fail_reason = "Too many absences."

    # Status
    if failed:
        status = "Failed"
    else:
        status = "Passed"

    # Remarks 
    match grade:
        case "A":
            remarks = "Excellent"
        case "B":
            remarks = "Good job"
        case "C":
            remarks = "Needs Improvement"
        case "D":
            remarks = "On Probation"
        case "F":
            remarks = "Failed"
        case _:
            remarks = "Invalid grade"

    # Print result
    print("--- Student Report ---")
    print("Name:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("Absences:", absences)
    print("Status:", status)
    if failed:
        print("Reason for failure:", fail_reason)
    print("Remarks:", remarks)
    print("----------------------")

    # Ask to run again
    again = input("Would you like to check another grade? (yes/no): ").lower()
    if again != "yes":
        print("System Ended.")
        break