# Fake Image Detection


## Getting Started

### Pre-requisites

Ensure you have Python 3.12 installed on your system. This project also requires a webcam for hand gesture recognition.

### Installation

1. Clone the repository to your local machine:

```bash
https://github.com/Jay-sanjay/Fake-Image-Detection
```
2. Create a conda environment after opening the repository

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```


3. install the requirements
```bash
pip install -r requirements.txt
```

4. install Dataset
For ease of the user I have uploaded the dataset on GoogleDrive, and to add it to your project just run
```bash
python main.py
```

5. Live Preview of the Web-App !!
```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## Improving the performance:
Once the app works fine on your local machine you can go added and tweak the model parameters [here](https://github.com/Jay-sanjay/Fraudulent-Image-Detection/blob/main/params.yaml) . 
This could possibly be increasing the number of Epochs and other changing other Hyper-Parameters.



## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

## Prediction Workflow
![image](https://github.com/Jay-sanjay/Fraudulent-Image-Detection/assets/134289328/e7561ce6-e083-4cf9-8367-8648040dabe4)


## Model Architecture
![image](https://github.com/Jay-sanjay/Fraudulent-Image-Detection/assets/134289328/e5bf9c1e-1c74-4303-83c6-46587309aafb)


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Jay-sanjay/Fake-Image-Detection.mlflow


Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Jay-sanjay/Fake-Image-Detection.mlflow

export MLFLOW_TRACKING_USERNAME=Jay-sanjay 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```
## Contributing to this Project:
#### We currently have following more tasks that can be add to the project to increase it's diversity:

### Add DVC and MLFlow integration

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)


## Currently we are using the python Application for CI/CD workflow , but for future we would like to have AWS-CICD workflows:
### AWS-CICD-Deployment-with-Github-Actions

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
### 4. Create EC2 machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

