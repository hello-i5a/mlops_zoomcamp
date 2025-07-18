@echo off
REM Launch the MLflow tracking server with SQLite and local artifact store

python -m mlflow server ^
  --backend-store-uri sqlite:///mlflow.db ^
  --default-artifact-root ./artifacts ^
  --host 127.0.0.1 ^
  --port 5000
