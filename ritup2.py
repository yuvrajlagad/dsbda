# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:15:16 2023

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

column_values=df.values
print(column_values)

descriptive_statistic =df.describe(include='all')
print(descriptive_statistic)

sorted_data = df.sort_index(axis=1)
print(sorted_data)
