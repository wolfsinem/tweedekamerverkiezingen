import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt


df = pd.read_csv(("/Users/wolfsinem/downloads/Kopie van Verkiezingen 2021 - Blad1.csv"))
df.rename(columns={"Unnamed: 0": "Standpunten"}, inplace=True)

new_df = df
pd.options.mode.chained_assignment = None 
new_df['Mijn partij'] = ""

def histogram_intersection(a, b):
    v = np.minimum(a, b).sum().round(decimals=1)
    return v

standpunten = []
for i in df['Standpunten']:
    standpunten.append(i)

answers = []
for stelling in standpunten:
    answers.append(int(input(f"{stelling} (Ja=1, nee=0): ")))
    
for i in range(len(new_df.index)):
    new_df.at[i,'Mijn partij'] = answers[i]

new_df = new_df.astype({'Mijn partij': 'int64'})

corr = new_df.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)