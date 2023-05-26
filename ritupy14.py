# -*- coding: utf-8 -*-
"""
Created on Sat May 27 01:34:13 2023

@author: YUVRAJ
"""
import pandas as pd

# Load the dataset into a DataFrame
iris_data = pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\Iris.csv")

# Display the column names and data types
print(iris_data.dtypes)

import matplotlib.pyplot as plt

# Create histograms for each feature
for feature in iris_data.columns:
    plt.hist(iris_data[feature])
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {feature}')
    plt.show()

import seaborn as sns

# Create box plots for each feature
for feature in iris_data.columns:
    sns.boxplot(x=feature, data=iris_data)
    plt.xlabel(feature)
    plt.title(f'Box Plot of {feature}')
    plt.show()
