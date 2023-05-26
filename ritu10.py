# -*- coding: utf-8 -*-
"""
Created on Sat May 27 00:40:51 2023

@author: YUVRAJ
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv(r"C:\Users\YUVRAJ\Desktop\DSBDAL\housing.csv")
X = data.drop('MEDV', axis=1)
y = data['MEDV']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)


accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
#weighted = precision_score(y_test, y_pred)
#micro = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


print("Confusion Matrix:")
print(cm)
print("\nAccuracy:", accuracy)
print("Error Rate:", error_rate)
#print("Precision:", preci1)
#print("Recall:", recall1)
print("F1 Score:", f1)
