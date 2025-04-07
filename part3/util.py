import pandas as pd

def get_unique_player_count(filepath="data/demographics.csv"):
    df = pd.read_csv(filepath)
    return df['pid'].nunique()
