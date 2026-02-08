import pandas as pd

data={
    "StudyHours" :[2,4,6,8,9,5,3,7],
    "Attendance": [60, 70, 80, 90, 95, 75, 65, 85],
    "Sleep": [5, 6, 7, 8, 8, 6, 5, 7],
    "Marks": [40, 55, 70, 85, 92, 65, 50, 78]

}
df=pd.DataFrame(data)

df.to_csv("Student.csv",index=False)

