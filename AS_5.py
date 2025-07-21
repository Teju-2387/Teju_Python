import pandas as pd
import numpy as np

data={
    'Name':['Amit', 'Sagar', 'Pooja'],
    'Math':[85,90,78],
    'Science':[85,90,78],
    'English':[85,90,78],

}

df=pd.DataFrame(data)

df['Name']= df['Name'].replace('pooja', 'puja')
