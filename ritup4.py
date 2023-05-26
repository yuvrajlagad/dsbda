# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:29:59 2023

@author: YUVRAJ
"""



import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\movies edited.csv")
df

data_types = df.dtypes
print("Data Types:")
print(data_types)

df['petal length (cm)'] = df['petal length (cm)'].astype(int)
