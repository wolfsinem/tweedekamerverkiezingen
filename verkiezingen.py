import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt

def load_dataset(filepath="/Users/wolfsinem/downloads/Kopie van Verkiezingen 2021 - Blad1.csv"):
    """Load the dataset 

    Returns:
        [type]: [description]
    """
    df = pd.read_csv((filepath))
    df.rename(columns={"Unnamed: 0": "Standpunten"}, inplace=True)
    return df


def modify_df():
    """Return the modified version of the dataframe with a new column.
    """
    new_df = load_dataset()
    pd.options.mode.chained_assignment = None 
    new_df['Mijn partij'] = ""
    return new_df

def histogram_intersection(a, b):
    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]

    Returns:
        [type]: [description]
    """
    v = np.minimum(a, b).sum().round(decimals=1)
    return v


def questions(new_df):
    """[summary]

    Returns:
        [type]: [description]
    """
    standpunten = []
    for i in new_df['Standpunten']:
        standpunten.append(i)
    return standpunten


def answer_questions(new_df):
    """[summary]
    """
    questions_ = questions(new_df)
    answers = []
    for stelling in questions_:
        answers.append(int(input(f"{stelling} (Ja=1, nee=0): ")))
    
    for i in range(len(new_df.index)):
        new_df.at[i,'Mijn partij'] = answers[i]


new_df = modify_df()

a = answer_questions(new_df)
corr = new_df.corr()
print(corr.style.background_gradient(cmap='coolwarm').set_precision(2))