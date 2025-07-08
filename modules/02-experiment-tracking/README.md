# Experiment Tracking & Model Management

Background info: **Saving model**

Saving a model means serializing the trained model to disk so it can be reused without retraining.

_How and why saving models differs from traditional machine learning (ML) and deep learning (DL)?_

1. ML: Common frameworks used are `scikit-learn`, `XGBoost`, `LightGBM`. Usually saved as pickled Python objects that are of small file size (KB-MB).
2. DL: Frameworks include `TensorFlow`, `PyTorch`, `Keras`. Models are saved as custom binary formats which are framework natives like like `.pt`, `SavedModel`, `.h5` and are of large file size (MB-GB).

In short: when saving models think from a **workflow and deployment perspective**.

## Experiment Tracking

## Model Registry

**Introduction**: Why is there a need for a model registry?

- Challenge: Communication gaps between data scientists and engineers complicate deployment.
- Solution: Model registry streamlines the process by centralizing model info i.e. model changes, hyperparameters, and required preprocessing.

**Model Registration**: How are models documented and controlled before deployment?

- Process: Data scientists register models based on performance and readiness (metrics: training duration, model size, and error rates).
- Access: Deployment engineers view and manage models through the registry.

**Promotion of Models**: How do models transition through various stages in their lifecycle?

- Stages: Models can be moved to production, staging, or archived.
- Evaluation: Used performance metrics to determine model suitability for production.

**Transitioning Stages**: How to promote or archive models based on evaluation?

- Testing: Models are tested against new data to validate performance.
- Decisions: Engineers decide on promotions based on test results and metrics.

**Model Lineage**: Focuses on maintaining relationships between model versions and training data.

- History: Automatic versioning keeps track of changes and updates.
- Retrieval: Models can be traced back to their training experiments for verification.

**MLflow**: Practical use of MLflow for model tracking and registration.

- Logging: MLflow tracks experiments, models, and parameters effectively.
- Registration: Demonstrates how to register and transition model versions smoothly.
- Other commands: Retrieving performance metrics, and transitioning models between stages.
