num_grades = int(input("Input amount of points: "))
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for _ in range(num_grades):
    grade = int(input("Input point (0-100): "))
    if 90 <= grade <= 100:
        grade_counts['A'] += 1
    elif 75 <= grade <= 89:
        grade_counts['B'] += 1
    elif 60 <= grade <= 74:
        grade_counts['C'] += 1
    elif 50 <= grade <= 59:
        grade_counts['D'] += 1
    elif 0 <= grade <= 49:
        grade_counts['F'] += 1
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