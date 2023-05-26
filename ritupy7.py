# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:19:21 2023

@author: YUVRAJ
"""


import pandas as pd
import numpy as np
import seaborn as sns


df=pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\per.csv")
df
summary_statistics = df.groupby('age')['test_score'].agg(['mean', 'median', 'min', 'max', 'std'])
print(summary_statistics)

category_values = df['age'].unique().tolist()
print(category_values)
