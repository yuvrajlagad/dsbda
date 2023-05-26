# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:49:40 2023

@author: YUVRAJ
"""
import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\movies edited.csv")
df
#checcking for missing value
missing_value = df.isnull().sum()
#geeting initial statics
statistics = df.describe()

print("missing value")
print(missing_value)
print("statistics:")
print(statistics)

df.head(n=5)
df.tail(n=5)

row_labels =df.index
print(row_labels)


column_lables=df.columns
print(column_lables)

#dimension

dim =df.shape
print(dim)
