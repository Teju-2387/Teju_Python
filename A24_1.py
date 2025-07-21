import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data={
    'Name':['Amit', 'Sagar', 'Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82],

}

df=pd.DataFrame(data)


df['Math_normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())

print("After Normalized Maths Columns:")
print(df)