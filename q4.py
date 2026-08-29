import numpy as np
hours = np.array([1,2,3,4,5])
attendance = np.array([75,85,96,67,69])
prevscore = np.array([67,68,71,91,1])
finalscore = np.array([71,88,77,95,2])
print("hours shape:", hours.shape, "dtype:", hours.dtype)
print("attendance shape:", attendance.shape, "dtype:", attendance.dtype)
print("prevscore shape:", prevscore.shape, "dtype:", prevscore.dtype)
print("finalscore shape:", finalscore.shape, "dtype:", finalscore.dtype)
print("Mean score is:", finalscore.mean())
print("Max score is:", finalscore.max())
print("Min score is:", finalscore.min())
print("Std Deviation of score is:", finalscore.std())

finalscore+=5
pas= finalscore>=75
print("final score after bonus marks", finalscore)
print("boolean array", pas)
