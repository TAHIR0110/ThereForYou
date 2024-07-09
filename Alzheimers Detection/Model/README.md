# Alzheimers Detection

## 🎯 Goal
The goal of this project is to develop a deep learning model capable of detecting Alzheimer's disease from brain MRI images. The model aims to accurately classify images into different stages of Alzheimer's: Non-Demented, Very Mild Demented, Mild Demented, and Moderate Demented.

## 🧵 Dataset
Link: https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images/data

## 🧾 Description
Alzheimer's disease is a progressive neurological disorder that leads to the degeneration of brain cells, causing memory loss and cognitive decline. Early detection is crucial for managing and potentially slowing the progression of the disease. The dataset contains brain MRI images classified into four categories:
- Non-Demented
- Very Mild Demented
- Mild Demented
- Moderate Demented
The dataset is pre-processed and divided into training and validation sets. Each image is labeled according to the stage of Alzheimer's it represents.

## 🧮 What I had done!
1. Data Preprocessing:
    - Resized images to a uniform size suitable for input into a deep learning model.
    - Normalized pixel values to ensure faster convergence during training.
    - Split data into training, validation, and test sets.

2. Model Architecture:
    - Used a pre-trained ResNet50 model as the base for transfer learning.
    - Added custom top layers to adapt the model to the specific classification task.
    - Fine-tuned the model by unfreezing the top layers and training them on the dataset.

3. Training:
    - Trained the model with an initial learning rate and used early stopping to prevent overfitting.
    - Fine-tuned the model by lowering the learning rate and unfreezing some layers of the base model.
    - Used data augmentation techniques to improve the robustness of the model.

## 📚 Libraries Needed
1. numpy
2. pandas
3. seaborn 
4. matplotlib.pyplot
5. plotly.graph_objects
6. sklearn

## Results:
1. Validation Accuracy: 53.09%
2. Validation Loss: 0.95

## 📢 Conclusion
The project successfully demonstrates the use of transfer learning with a pre-trained ResNet50 model to detect Alzheimer's disease from brain MRI images. By leveraging fine-tuning and data augmentation, the model achieved significant accuracy in classifying different stages of Alzheimer's. This approach can potentially aid in early detection and better management of the disease.

## ✒️ Your Signature
Name- Khushi Kalra
Github- https://github.com/abckhush
Role- GSSoC'24 Contributor
