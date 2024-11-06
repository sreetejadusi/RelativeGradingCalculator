# Relative Grading System in Python

This project calculates relative grades for a class of students based on their marks. Using standard statistical methods, such as the mean and standard deviation, this Python script assigns grades relative to the overall performance of the class, based on predefined thresholds.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)
- [Grade Distribution](#grade-distribution)
- [License](#license)

## Overview
In the relative grading system, students' grades are assigned based on their performance relative to the class average and standard deviation. This approach is often more fair and consistent than absolute grading as it accounts for variations in difficulty levels of exams and assessments.

## Features
- Calculates the average (`μ`) and standard deviation (`σ`) of the class marks.
- Assigns grades from "O" (Outstanding) to "F" (Fail) based on a normal distribution.
- Customizable grading thresholds for flexible grading schemes.
- Supports cases where the class size is at least 21 students.
- Handles special cases such as students with insufficient attendance or withdrawal.

## Prerequisites
- Python 3.x
- `numpy` and `pandas` packages for statistical calculations

Install prerequisites via pip:
```bash
pip install numpy pandas
```

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/relative-grading-system.git
    cd relative-grading-system
    ```
2. Prepare a list of student marks in a text or CSV file, or edit the array of marks directly in the code.
3. Run the script:
    ```bash
    python relative_grading.py
    ```

The script will display the grade distribution along with the corresponding grade points for each student.

## Example

### Sample Input
A list of student marks:
```python
marks = [64, 48, 48, 46, 54, 60, 58, 57, 55, 46, 52, 38, 36, 54, 41, 62, 58, 44, 56, 52, 61, ...]
```

### Sample Output
```plaintext
Marks: 64, Grade: O, Grade Points: 10
Marks: 48, Grade: B+, Grade Points: 7
Marks: 60, Grade: A+, Grade Points: 9
...
```

## Grade Distribution
The grades and their conditions are as follows:

| Grade | Description | Criteria                                 | Grade Points |
|-------|-------------|------------------------------------------|--------------|
| O     | Outstanding | `Marks >= μ + 1.5 * σ`                  | 10           |
| A+    | Excellent   | `μ + 1.0 * σ <= Marks < μ + 1.5 * σ`    | 9            |
| A     | Very Good   | `μ + 0.5 * σ <= Marks < μ + 1.0 * σ`    | 8            |
| B+    | Good        | `μ - 0.5 * σ <= Marks < μ + 0.5 * σ`    | 7            |
| B     | Above Avg   | `μ - 1.0 * σ <= Marks < μ - 0.5 * σ`    | 6            |
| C     | Average     | `μ - 1.5 * σ <= Marks < μ - 1.0 * σ`    | 5            |
| P     | Pass        | `35 <= Marks < μ - 1.5 * σ`             | 4            |
| F     | Fail        | `Marks < 35`                            | 0            |

### Special Cases
- **Ab (Absent)**: Indicates a student was absent for the assessment.
- **S (Satisfactory)**: Assigned for non-graded courses.
- **U (Unsatisfactory)**: Assigned for non-graded courses.
- **R (Insufficient Attendance)**: Indicates the student had insufficient attendance.
- **W (Withdrawal)**: Indicates the student withdrew from the course.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
