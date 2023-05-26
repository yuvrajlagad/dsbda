# -*- coding: utf-8 -*-
"""
Created on Sat May 27 01:21:42 2023

@author: YUVRAJ
"""

import seaborn as sns
import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt
titanic_data = sns.load_dataset('titanic')

sns.boxplot(x='sex', y='age', hue='survived', data=titanic_data)
plt.xlabel('Gender')
plt.ylabel('Age')
plt.title('Distribution of Age with respect to Gender and Survival')
plt.show()
