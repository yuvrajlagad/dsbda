# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:02:07 2023

@author: YUVRAJ
"""



import pandas as pd
import numpy as np
import seaborn as sns


df=pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\per.csv")
df

missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)

sns.boxplot(data=df[['age','test_score']])

df['transformed_test_score']=np.log(df['test_score'])
