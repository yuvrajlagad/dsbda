# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:40:33 2023

@author: YUVRAJ
"""

import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\Iris.csv")
species_data = df[df['Species'].isin(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])]
species_stats = species_data.groupby('Species').describe()

print(species_stats)
