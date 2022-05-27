import pandas as pd
data = {
    'Level': ['Beginner', 'Intermediate', 'Advanced', 'Beginner', 'Intermediate', 'Advanced', 
    'Beginner', 'Intermediate', 'Advanced', 'Beginner', 'Intermediate', 'Advanced', 'Beginner', 
    'Intermediate', 'Advanced', 'Beginner', 'Intermediate', 'Advanced'], 
    'Students': [10.0, 20.0, 10.0, 10.0, 20.0, 10.0, None, 20.0, 20.0, 40.0, 10.0, 30.0, 30.0, 10.0, 10.0, 10.0, 40.0, 20.0]
    }
df = pd.DataFrame.from_dict(data)

print("The sample dataframe taken is :")
print(df)
print("the no. of rows in original dataframe is :" ,len(df.index))
df_unique=df.drop_duplicates()
# print(len(df_unique.index))
people = df_unique.iloc[:, 1]
print("no. of rows after removing duplicates is: " ,len(people))


