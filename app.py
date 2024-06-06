import streamlit as st
from PIL import Image
from cnnClassifier.pipeline.prediction import PredictionPipeline
import os

def index():
    return "Project is running"

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

st.title("Fraudulent Image Detection")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image.save(clApp.filename)

    if st.button('Predict'):
        result = clApp.classifier.predict()
        st.write(result)