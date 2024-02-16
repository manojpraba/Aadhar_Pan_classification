# Aadhar_Pan_classification

## MLFLOW
```bash
MLFLOW_TRACKING_URI=https://dagshub.com/manojpraba/Aadhar_Pan_classification.mlflow \
MLFLOW_TRACKING_USERNAME=manojpraba \
MLFLOW_TRACKING_PASSWORD=04e8812a15298b038b8948da95e66bef3542a12f \
python script.py
```
Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/manojpraba/Aadhar_Pan_classification.mlflow
export MLFLOW_TRACKING_USERNAME=manojpraba 

export MLFLOW_TRACKING_PASSWORD=04e8812a15298b038b8948da95e66bef3542a12f
```
## DVC
```bash
dvc init
dvc repro