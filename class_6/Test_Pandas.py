import pandas as pd
print(pd.__version__)

s = pd.Series([10, 20, 30, 40], index=['Rajeev', 'Anuj', 'Ivana', 'Ashiya'])
print(s)









#________________reading from csv________________

data = pd.read_csv(r"C:\Users\Ishan Titarmare\Desktop\ML_Webinar\class_6\students_raw.csv")
print(data)
print(data.info())
print("________________________________________")
print(data.describe())
print("_________________getting a column_______________________")
print(data[["student_name","passed"]].head())
print("_________________loc and iloc_______________________")
print(data.loc[1])

