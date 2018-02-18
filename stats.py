import numpy as np
import pandas as pd


data = pd.read_csv('data/labels_converted.csv')
print(data.columns)

df = data.groupby('Abnormality').nunique()
print(df)

df = data.groupby(['Abnormality','Type']).nunique()
print(df)