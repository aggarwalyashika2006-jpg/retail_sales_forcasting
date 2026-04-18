import pandas as pd
import numpy as np

def train_model(df):
    # dummy model (for beginner level)
    return {"status": "trained"}

def create_future_dates(df, days=7):
    last_date = df["Date"].max()

    future_dates = pd.date_range(
        start=last_date,
        periods=days+1,
        freq="D"
    )[1:]

    products = df["Product"].unique()

    data = []

    for p in products:
        for d in future_dates:
            data.append([d, p])

    return pd.DataFrame(data, columns=["Date", "Product"])


def predict(model, future_df):
    if len(future_df) == 0:
        return future_df

    future_df["Predicted"] = np.random.randint(60, 150, len(future_df))
    return future_df