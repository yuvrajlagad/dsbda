# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:13:01 2023

@author: YUVRAJ
"""


import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\movies edited.csv")
df


#checcking for missing value
missing_value = df.isnull().sum()
print("missing value")
print(missing_value)


#geeting initial statics
statistics = df.describe()
print("statistics:")
print(statistics)

var_des=df.dtypes
print("variabledescription")
print(var_des)

dimension=df.shape
print(dimension)

sorted_data= df.sort_values(by='votes')
print("sorted values")
print(sorted_data)


selection_by_position= df.iloc[3:4,2:4]
print(selection_by_position)


selection_by_rows = df[10:20]
print("Selection by rows:")
print(selection_by_rows)

selection_by_label = df.loc[df['votes'] == 'value']
print("Selection by Label:")
print(selection_by_label)
