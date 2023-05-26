# -*- coding: utf-8 -*-
"""
Created on Sat May 27 01:13:22 2023

@author: YUVRAJ
"""

import seaborn as sns
import matplotlib.pyplot as plt

titanic_data = sns.load_dataset('titanic')
titanic_data
sns.countplot(x='sex', data=titanic_data)
plt.show()

sns.histplot(data=titanic_data, x='fare')
plt.show()
