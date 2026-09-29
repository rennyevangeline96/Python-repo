while True:
    try:
        user_input = input("Enter your mark (0-100): ").strip()

        if user_input == "":
            print("Invalid input. Please enter a number.")
            continue

        mark = int(user_input)

        if mark < 0 or mark > 100:
            print("Invalid mark. Please enter a number between 0 and 100.")
            continue

        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"

        print(f"Mark: {mark}")
        print(f"Grade: {grade}")
        break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

