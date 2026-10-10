"""
Student Academic Performance Analysis and Visualization
Using Pandas and Matplotlib
Lab Sheet 3 - Python Libraries and Applications

Run:
    pip install -r requirements.txt
    python main.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "student_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    # 1. Load data
    df = pd.read_csv(DATA_FILE)
    print("\n========== ORIGINAL DATA ==========")
    print(df.head())

    # 2. Basic cleaning and transformation
    df.columns = df.columns.str.strip()
    df["Student_Name"] = df["Student_Name"].astype(str).str.strip()
    df = df.drop_duplicates(subset=["Student_ID"])
    numeric_cols = [
        "Attendance", "Study_Hours", "Assignment_Marks",
        "Internal_Assessment_Marks", "Python_Marks", "DBMS_Marks",
        "AI_Marks", "Final_Exam_Marks"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    subject_cols = ["Python_Marks", "DBMS_Marks", "AI_Marks", "Final_Exam_Marks"]
    df["Average_Marks"] = df[subject_cols].mean(axis=1).round(2)
    df["Performance_Level"] = df["Average_Marks"].apply(
        lambda x: "High" if x >= 75 else ("Average" if x >= 50 else "Low")
    )

    # 3. Display useful analysis
    print("\n========== DATA SUMMARY ==========")
    print(df.describe(numeric_only=True).round(2))
    print("\n========== HIGH-PERFORMING STUDENTS (Average >= 75) ==========")
    high = df[df["Average_Marks"] >= 75][["Student_ID", "Student_Name", "Average_Marks"]]
    print(high.to_string(index=False) if not high.empty else "No students meet this threshold.")

    print("\n========== LOW-PERFORMING STUDENTS (Average < 50) ==========")
    low = df[df["Average_Marks"] < 50][["Student_ID", "Student_Name", "Average_Marks"]]
    print(low.to_string(index=False) if not low.empty else "No students meet this threshold.")

    print("\n========== SUBJECT-WISE AVERAGE ==========")
    print(df[subject_cols].mean().round(2).to_string())
    print("\n========== DEPARTMENT-WISE AVERAGE ==========")
    print(df.groupby("Department")["Average_Marks"].mean().round(2).sort_values(ascending=False))
    print("\n========== ATTENDANCE AND PERFORMANCE CORRELATION ==========")
    print("Attendance vs Average Marks:", round(df["Attendance"].corr(df["Average_Marks"]), 3))
    print("Study Hours vs Average Marks:", round(df["Study_Hours"].corr(df["Average_Marks"]), 3))

    # Save the analyzed dataset
    df.to_csv(OUTPUT_DIR / "analyzed_student_data.csv", index=False)

    # 4. Visualization: subject-wise average marks
    subject_means = df[subject_cols].mean()
    plt.figure(figsize=(9, 5))
    subject_means.plot(kind="bar")
    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "subject_wise_average.png", dpi=150)
    plt.close()

    # 5. Visualization: department-wise performance
    department_means = df.groupby("Department")["Average_Marks"].mean().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    department_means.plot(kind="bar")
    plt.title("Department-wise Average Performance")
    plt.xlabel("Department")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "department_wise_performance.png", dpi=150)
    plt.close()

    # 6. Visualization: attendance vs marks
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Attendance"], df["Average_Marks"])
    plt.title("Relationship Between Attendance and Performance")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Marks")
    plt.xlim(0, 105)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "attendance_vs_performance.png", dpi=150)
    plt.close()

    # 7. Visualization: study hours vs marks
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Study_Hours"], df["Average_Marks"])
    plt.title("Relationship Between Study Hours and Performance")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_hours_vs_marks.png", dpi=150)
    plt.close()

    # 8. Performance level distribution
    level_counts = df["Performance_Level"].value_counts()
    plt.figure(figsize=(7, 5))
    level_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Student Performance Level Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "performance_distribution.png", dpi=150)
    plt.close()

    print("\nCharts and analyzed CSV saved in the 'outputs' folder.")
    print("Analysis completed successfully.")

if __name__ == "__main__":
    main()
