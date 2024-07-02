# Fake Image Detection
The Project utilizes Convolutional Neural Net based Mesonet Model to Identify deep fakes.  The architecture focuses on mesoscopic properties of images. More information about the model architecture is provided below.

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

## TODO's: 
- [ ] Add support for Video Frogery detection.
- [ ] Dockerize the Codebase.
- [ ] Add comments for better code readibility.
- [ ] Host using Amazon-AWS.


