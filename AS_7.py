import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data={
    'Name':['Amit', 'Sagar', 'Pooja'],
    'Math':[85,90,78],
    'Science':[85,90,78],
    'English':[85,90,78],

}

df=pd.DataFrame(data)
df['Total']=df['Math']+df['Science']+df['English']


plt.bar(df['Name'], df['Total'])

plt.xlabel("Students Name")
plt.ylabel("Total Marks")
plt.title("Bar Plot")
plt.show()
