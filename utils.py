import pandas as pd

def load_data():
    """Load the Titanic dataset and filter"""
    df = pd.read_csv('data/titanic.csv')
    df = df[df["sex"] == "male"]
    return df

def clean_data(df):
    """
    Clean the data by dropping unnecessary columns and renaming others."""
    df = df.dropna()
    
    df['embarked'] = df["embarked"].str.lower()
    
    return df