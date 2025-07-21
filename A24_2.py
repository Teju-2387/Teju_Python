import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data={
    'Name':['Amit', 'Sagar', 'Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82],
    'Gender': ['Male', 'Male', 'Female'] 

}

df=pd.DataFrame(data)


df_encoded = pd.get_dummies(df, columns=['Gender'])
print("After one Hot encoding:")
print(df_encoded)

