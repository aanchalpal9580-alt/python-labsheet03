# Student Academic Performance Analysis and Visualization

**Lab Sheet 3 — Python Libraries and Applications (BCA)**

## Project title
Student Academic Performance Analysis and Visualization Using Pandas and Matplotlib

## Aim
To load, clean, transform, analyze, and visualize student academic data using Pandas and Matplotlib.

## Dataset
`student_data.csv` contains sample records with:
- Student ID, name, gender, and department
- Attendance and study hours
- Assignment and internal assessment marks
- Python, DBMS, AI, and final exam marks

The records are sample/demo data and should be replaced with authorized college data if required.

## Requirements
- Python 3.10 or later
- Pandas
- Matplotlib

## How to run
Open a terminal in this project folder and run:

```bash
pip install -r requirements.txt
python main.py
```

## Analysis included
1. Loads the CSV file using Pandas.
2. Cleans column names, removes duplicate student IDs, and handles missing numeric values.
3. Calculates average marks and classifies performance as High, Average, or Low.
4. Lists high- and low-performing students.
5. Calculates subject-wise and department-wise averages.
6. Calculates correlations between attendance/study hours and average marks.
7. Saves an analyzed CSV and five charts in the `outputs` folder.

## Output files
After running the program, check the `outputs/` folder for:
- `analyzed_student_data.csv`
- `subject_wise_average.png`
- `department_wise_performance.png`
- `attendance_vs_performance.png`
- `study_hours_vs_marks.png`
- `performance_distribution.png`

## Suggested GitHub repository description
Python project to analyze student academic performance using Pandas and visualize trends using Matplotlib.
