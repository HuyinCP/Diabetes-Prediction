import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import title
from sklearn.impute import SimpleImputer
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Datasets/StudentScore.xls')
target = "writing score"

x = df.drop(target, axis = 1)
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

imputer = SimpleImputer(missing_values=-1.0, strategy='median')
x_train[["math score", "reading score"]] = imputer.fit_transform(x_train[["math score", "reading score"]])

