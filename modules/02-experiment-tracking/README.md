# Experiment Tracking & Model Management

Background info: **Saving model**

_How and why saving models differs from traditional machine learning (ML) and deep learning (DL)?_

1. ML: Common frameworks used are `scikit-learn`, `XGBoost`, `LightGBM`. Usually saved as pickled Python objects that are of small file size (KB-MB).
2. DL: Frameworks include `TensorFlow`, `PyTorch`, `Keras`. Models are saved as custom binary formats which are framework natives like like `.pt`, `SavedModel`, `.h5` and are of large file size (MB-GB).

In short: when saving models think from a **workflow and deployment perspective**.
