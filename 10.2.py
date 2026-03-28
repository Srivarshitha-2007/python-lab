import pandas as pd
df = pd.read_csv("C:\\Users\\91798\\PycharmProjects\\.venv\\Lib\\site-packages\\numpy\\_core\\tests\\data\\umath-validation-set-tanh.csv")
print(df.sort_values(by=df.columns[0]))
print(df.sort_values(by=df.columns[0], ascending=False))
print(df[0:5])
print(df[2:8])
