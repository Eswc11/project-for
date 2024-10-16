num_grades = int(input("Input amount of points: "))
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for _ in range(num_grades):
   while True:  
        try:
            grade = int(input("Введите оценку (0-100): "))
            if 0 <= grade <= 100:
                if 90 <= grade <= 100:
                    grade_counts['A'] += 1
                elif 75 <= grade <= 89:
                    grade_counts['B'] += 1
                elif 60 <= grade <= 74:
                    grade_counts['C'] += 1
                elif 50 <= grade <= 59:
                    grade_counts['D'] += 1
                else:
                    grade_counts['F'] += 1
                break
            else:
                print("Error")
        except ValueError:
            choice = input("Invalid input. Do you want to continue? (Y/N): ")
            if choice != 'Y':
                print("The program stopped due to incorrect input.")
                exit()
total_grades = sum(grade_counts.values())
for grade in grade_counts:
    count = grade_counts[grade]
    if total_grades > 0:
        percentage = (count / total_grades) * 100
    else:
        percentage = 0
    if count == 1:
        grade_word = "grade"
    else:
        grade_word = "grades"
    print(f"{grade}: {count} {grade_word} ({percentage:.2f}%)")
