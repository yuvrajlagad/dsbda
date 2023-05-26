# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:47:57 2023

@author: YUVRAJ
"""



import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\movies edited.csv")
df
encoded_data = pd.get_dummies(df, columns=['movie_name'])

missing_values_count = df['votes'].isnull().sum()
print("Missing Values Count in 'specific_column':", missing_values_count)

missing_values_groupby = df.groupby('votes')['yuvraj'].apply(lambda x: x.isnull().sum())
print("Groupby Count of Missing Values in 'specific_column':")
print(missing_values_groupby)
