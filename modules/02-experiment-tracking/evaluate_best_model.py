import os
import pickle
import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np


def load_pickle(filename):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


mlflow.set_tracking_uri("http://127.0.0.1:5000")
client = mlflow.tracking.MlflowClient()
experiment = client.get_experiment_by_name("random-forest-hyperopt")

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.rmse ASC"],
    max_results=1
)

best_run = runs[0]
print("Best Run ID:", best_run.info.run_id)
print("Validation RMSE:", best_run.data.metrics['rmse'])

X_train, y_train = load_pickle(os.path.join("output", "train.pkl"))
X_val, y_val = load_pickle(os.path.join("output", "val.pkl"))
X_test, y_test = load_pickle(os.path.join("output", "test.pkl"))

best_params = best_run.data.params

best_params = {
    'max_depth': int(best_params['max_depth']),
    'n_estimators': int(best_params['n_estimators']),
    'min_samples_split': int(best_params['min_samples_split']),
    'min_samples_leaf': int(best_params['min_samples_leaf']),
    'random_state': int(best_params['random_state'])
}

rf = RandomForestRegressor(**best_params)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

rmse_test = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Test RMSE of best model: {rmse_test:.3f}")
