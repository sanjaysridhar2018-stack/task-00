import os
import pandas as pd
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)

a = pd.read_csv("processed_student_performance.csv")

plt.figure(figsize=(20, 6))
plt.bar(a["Student"], a["Final_Score"])
plt.title("Student Names vs Final Scores")
plt.xlabel("student")
plt.ylabel("final score")
plt.xticks(rotation=90, fontsize=6)
plt.tight_layout()
plt.savefig("final_scores.png")
plt.close()

plt.figure(figsize=(8, 6))
plt.scatter(a["Hours_Studied"], a["Final_Score"])
plt.title("hours studied vs final score")
plt.xlabel("Hours studied")
plt.ylabel("Final dcore")
plt.tight_layout()
plt.savefig("study_vs_score.png")
plt.close()

plt.figure(figsize=(8, 6))
plt.hist(a["Final_Score"], bins=10, edgecolor="black")
plt.title("Distribution of final scores")
plt.xlabel("Final score")
plt.ylabel("No. of students")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.close()

plt.figure(figsize=(8, 6))
plt.scatter(a["Attendance"], a["Final_Score"])
plt.title("Attendance vs ginal score")
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("custom_plot.png")
plt.close()
