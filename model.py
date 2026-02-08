import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


df1=pd.read_csv('Student.csv')

X=df1[['StudyHours','Attendance','Sleep']]
Y=df1['Marks']

model=LinearRegression()
model.fit(X,Y)

joblib.dump(model,'model.pkl')