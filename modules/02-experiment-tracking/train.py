import os
import pickle
import click
import mlflow
import mlflow.sklearn  # for autologging

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):
    # tracking server, comes handy for remote server
    mlflow.set_tracking_uri("http://127.0.0.1:5000")

    mlflow.sklearn.autolog()  # automates the following:
    # logging model inputs/outputs
    # saving the model
    # tracking hyperparameters
    # logging training metrics

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    with mlflow.start_run():  # track experiments, everything is logged within this block
        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)

        y_pred = rf.predict(X_val)
        rmse = root_mean_squared_error(y_val, y_pred)
        print(f"RMSE: {rmse:.4f}")


if __name__ == '__main__':
    run_train()
