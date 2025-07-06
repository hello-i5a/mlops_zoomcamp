# Introduction to MLOps

MLOps is needed to operationalize machine learning models in reliable, scalable and repeatable way. To be specific:

- To bridge the gap between development and production.
- To automate the integration and deployment of new data and models.
- To monitor and track model performance as it degrades over time due to data drift, concept drift and seasonality.
- To ensure reproducibility and compliance.

Foobar is a Python library for dealing with word pluralization.

## MLOps Maturity Model

MLOps maturity model is similar to Agile maturity model in software. In essence, it helps teams to understand their current MLOps standing and provides a roadmap for improvement.

Access Microsoft's MLOps maturity model [here](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model).

**MLOps Maturity Model Summary**

| Level | Name                   | Focus                                | Characteristics                                                 |
| ----- | ---------------------- | ------------------------------------ | --------------------------------------------------------------- |
| 0     | No MLOps               | Manual, isolated workflows           | Ad hoc experimentation, no reproducibility or collaboration     |
| 1     | DevOps for ML          | Model deployment only                | Manual training and deployment, limited automation              |
| 2     | Automated ML Pipelines | Reproducible and automated workflows | Feature/data pipelines, automated training, model registry      |
| 3     | CI/CD for ML           | Continuous training and validation   | Automated testing, monitoring, drift detection, rollback        |
| 4     | Scalable MLOps         | Scalable, governed, and compliant    | Multi-model governance, reuse, team collaboration, auditability |
