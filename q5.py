import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)

a = pd.read_csv("student_performance.csv")

print("first five rows")
print(a.head())

rows, columns = a.shape
print("rows:", rows)
print("columns:", columns)

print("column names")
print(a.columns)

print("missing values per column")
print(a.isnull().sum())

average = a["Final_Score"].mean()
print("average final score:", average)

topstudent = a[a["Final_Score"] == a["Final_Score"].max()]
print("student with highest final score")
print(topstudent)

a["Improvement"] = a["Final_Score"] - a["Previous_Score"]

goodattendance = a[a["Attendance"] >= 80]
print("students with attendance 80 or higher")
print(goodattendance)

a = a.sort_values("Final_Score", ascending=False)
print("sorted by final score, highest first")
print(a)

a.to_csv("processed_student_performance.csv", index=False)
