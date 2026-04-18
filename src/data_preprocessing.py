import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"])
    return df