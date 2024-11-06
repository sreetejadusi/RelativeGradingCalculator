import numpy as np


def calculate_relative_grades(marks):
    mean = np.mean(marks)
    std_dev = np.std(marks)

    grade_boundaries = {
        "O": mean + 1.5 * std_dev,
        "A+": mean + 1.0 * std_dev,
        "A": mean + 0.5 * std_dev,
        "B+": mean - 0.5 * std_dev,
        "B": mean - 1.0 * std_dev,
        "C": mean - 1.5 * std_dev,
    }

    grades = []
    for mark in marks:
        if mark >= grade_boundaries["O"]:
            grades.append(("O", 10))
        elif grade_boundaries["A+"] <= mark < grade_boundaries["O"]:
            grades.append(("A+", 9))
        elif grade_boundaries["A"] <= mark < grade_boundaries["A+"]:
            grades.append(("A", 8))
        elif grade_boundaries["B+"] <= mark < grade_boundaries["A"]:
            grades.append(("B+", 7))
        elif grade_boundaries["B"] <= mark < grade_boundaries["B+"]:
            grades.append(("B", 6))
        elif grade_boundaries["C"] <= mark < grade_boundaries["B"]:
            grades.append(("C", 5))
        elif 35 <= mark < grade_boundaries["C"]:
            grades.append(("P", 4))
        else:
            grades.append(("F", 0))

    return grades


marks = [] #enter array of marks

grades = calculate_relative_grades(marks)


for i, (mark, (grade, grade_point)) in enumerate(zip(marks, grades), 1):
    print(f"Student {i}: Mark = {mark}, Grade = {grade}, Grade Point = {grade_point}")
