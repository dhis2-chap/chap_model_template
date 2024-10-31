import argparse

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

def train(csv_fn, model_fn):
    df = pd.read_csv(csv_fn)

    # Here you train your model based on the data in df, and save it to model.bin


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a minimalist forecasting model.')

    parser.add_argument('csv_fn', type=str, help='Path to the CSV file containing input data.')
    parser.add_argument('model_fn', type=str, help='Path to save the trained model.')
    args = parser.parse_args()
    train(args.csv_fn, args.model_fn)


