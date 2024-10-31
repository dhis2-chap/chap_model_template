import argparse

import joblib
import pandas as pd

def predict(model_fn, historic_data_fn, future_climatedata_fn, predictions_fn):
    df = pd.read_csv(future_climatedata_fn)

    # Here you use your trained model to predict disease cases on the data in df, and write them out to predictions.csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict using the trained model.')

    parser.add_argument('model_fn', type=str, help='Path to the trained model file.')
    parser.add_argument('historic_data_fn', type=str, help='Path to the CSV file historic data (here ignored).')
    parser.add_argument('future_climatedata_fn', type=str, help='Path to the CSV file containing future climate data.')
    parser.add_argument('predictions_fn', type=str, help='Path to save the predictions CSV file.')

    args = parser.parse_args()
    predict(args.model_fn, args.historic_data_fn, args.future_climatedata_fn, args.predictions_fn)
