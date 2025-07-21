import pandas as pd
import numpy as np

data={
    'Name':['Amit', 'Sagar', 'Pooja'],
    'Math':[85,90,78],
    'Science':[85,90,78],
    'English':[85,90,78],

}

df=pd.DataFrame(data)
df['Total']=df['Math']+df['Science']+df['English']

df_new=df.sort_values(by='Total', ascending=False)

print("Data before Sorting")
print(df)

print("After Sorting:")
print(df_new)
