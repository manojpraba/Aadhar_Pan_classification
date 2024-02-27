# Aadhar_Pan_classification
The objective is to differentiate between Aadhar cards and PAN cards using a classification model. The model is based on a pre-trained VGG16 architecture, initially trained on the ImageNet dataset. Subsequently, a custom artificial neural network (ANN) layer is added to the VGG16 model for classification. This custom model is trained using a dataset comprising 250 Aadhar cards and 220 PAN cards, over 100 epochs. After training, the model achieves an accuracy of 96% in distinguishing between Aadhar cards and PAN cards.

## input and output
![alt tag](https://github.com/manojpraba/Aadhar_Pan_classification/blob/main/sceenshots/aadhar.png)
![alt tag](https://github.com/manojpraba/Aadhar_Pan_classification/blob/main/sceenshots/pan.png)

## Workflow
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/manojpraba/Aadhar_Pan_classification.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
localhost:8080
```


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
