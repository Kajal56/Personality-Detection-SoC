from pickle import FALSE
import pandas as pd
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

print("The dataframe we are working on is : ")
print(df)
print("Now, the outpus is given below : ")
df1=df.loc[df['grps']=='a']
dff1=df1.sort_values(by=['vals'],axis=0,ascending=False)
#print("---------------")
dff1.reset_index(inplace = True)
print("a   " ,dff1.loc[0].at['vals']+dff1.loc[1].at['vals']+dff1.loc[2].at['vals'])

df2=df.loc[df['grps']=='b']
dff2=df2.sort_values(by=['vals'],axis=0,ascending=False)
#print("---------------")
dff2.reset_index(inplace = True)
print("b   ",dff2.loc[0].at['vals']+dff2.loc[1].at['vals']+dff2.loc[2].at['vals'])

df3=df.loc[df['grps']=='c']
dff3=df3.sort_values(by=['vals'],axis=0,ascending=False)
#print("---------------")
dff3.reset_index(inplace = True)
print("c   ",dff3.loc[0].at['vals']+dff3.loc[1].at['vals']+dff3.loc[2].at['vals'])



#print("---------------")
