import pandas as pd


data = pd.read_csv('data/labels_converted.csv')
print(data.columns)

df = data.groupby('Abnormality')[['Abnormality']].count()
print(df)

df = data.groupby(['Abnormality','Type'])[['Abnormality','Type']].count()
print(df)
