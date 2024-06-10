# Wound Classification uisng DL

## 🎯 Goal
The main purpose of this project is to **do wound classification using deep learning (DL) which leverages convolutional neural networks (CNNs) to accurately analyze and classify wound images based on type, severity, and healing stage.** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/yasinpratomo/wound-dataset**

## 🧾 Description

This project involves the comparative analysis of **Five** Keras image detection models, namely **MobileNetV2** , **ResNet50V2** , **InceptionV3** , **DenseNet121** and **Xception**  applied to a specific dataset. The dataset consists of annotated images related to a particular domain, and the objectives include training and evaluating these models to compare their accuracy scores and performance metrics. Additionally, exploratory data analysis (EDA) techniques are employed to understand the dataset's characteristics, explore class distributions, detect imbalances, and identify areas for potential improvement. The methodology encompasses data preparation, model training, evaluation, comparative analysis of accuracy and performance metrics, and visualization of EDA insights. 

## 🧮 What I had done!

### 1. Data Loading and Preparation:
    Loaded the dataset containing image paths and corresponding labels into a pandas DataFrame for easy manipulation and analysis.

### 2. Exploratory Data Analysis (EDA):
    Bar Chart for Label Distribution: Created a bar chart to visualize the frequency distribution of different labels in the dataset.

    Pie Chart for Label Distribution: Generated a pie chart to represent the proportion of each label in the dataset.

### 3. Data Analysis:
    Counted the number of unique image paths to ensure data uniqueness and quality.
        Analyzed the distribution of image paths by label for the top 20 most frequent paths.
        Displayed the number of unique values for each categorical column to understand data variety.
        Visualized missing values in the dataset using a heatmap to identify and address potential data quality issues.
        Summarized and printed the counts of each label.

### 4. Image Preprocessing and Model Training:
    Loaded and preprocessed the test images, ensuring normalization of pixel values for consistency.
        Iterated through multiple models (VGG16, ResNet50 , Xception) saved in a directory and made predictions on the test dataset.
        Saved the predictions to CSV files for further analysis and comparison.

### 5. Model Prediction Visualization:
    Loaded models and visualized their predictions on a sample set of test images to qualitatively assess model performance.
        Adjusted image preprocessing for models requiring specific input sizes (e.g., 299x299 for Xception).

## 🚀 Models Implemented

Trained the dataset on various models , each of their summary is as follows :-

### Xception

When implementing the Xception model in code, we leverage its sophisticated architecture to bolster our image classification tasks. By loading the pre-trained Xception model with weights from the ImageNet dataset, we harness its comprehensive knowledge.

**Reasons for choosing Xception:** :  Lightweight (88 MB) , 
**Excellent Accuracy** (Xception achieves high accuracy in image classification tasks .) , 
Reduced Parameters (22.9M) ,
Faster Inference Speed (CPU - 39.4, GPU - 5.2)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/Xception_predictions/7dbb1cbd-16bb-4942-baaa-2b19880adaf0.png)</br>

![alt text](../Images/Xception_predictions/a92b3820-877c-48a5-a746-b4b077d94b44.png)</br>

![alt text](../Images/Xception_predictions/d352d053-b127-4458-a927-b26163768853.png)</br>

![alt text](../Images/Xception_predictions/f0ea0e45-c2e2-465d-a226-3d61be821f84.png)</br>




### MobileNetV2

Incorporating the MobileNetV2 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained MobileNetV2 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting MobileNetV2:**

- Lightweight Architecture (MobileNetV2's efficient design allows for quick processing with minimal computational resources.)
- Proven Accuracy (MobileNetV2 consistently performs well in various image recognition benchmarks, balancing accuracy and speed.)
- Reduced Parameters (3.4M, significantly fewer than many other models, enabling faster inference and reduced memory usage.)
- High Efficiency (CPU - 5, GPU - 1.4, making it highly suitable for deployment on resource-constrained devices.)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/MobileNetV2_predictions/34d7125f-47d0-41ec-850b-ad0a08ead6af.png)</br>

![alt text](../Images/MobileNetV2_predictions/653017d6-df31-4263-b4b9-34975feb1760.png)</br>

![alt text](../Images/MobileNetV2_predictions/9aaf4c99-d14f-4f52-b4d8-9845de26b466.png)</br>

![alt text](../Images/MobileNetV2_predictions/b6cc4c7c-0a36-4d2b-8d74-dce9938b5fed.png)


### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/Resnet50V2_predictions/34d97a0f-aa8f-4404-8bbb-6a86bb40d465.png)</br>

![alt text](../Images/Resnet50V2_predictions/3848c8aa-758c-43c3-b282-7b478ace9496.png)</br>

![alt text](../Images/Resnet50V2_predictions/7004d6fc-418a-4e73-92a2-90425a1605f9.png)</br>

![alt text](../Images/Resnet50V2_predictions/9b4a7662-ad14-439f-8f73-e4226aac3b3a.png)




### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/InceptionV3_predictions/104b158d-ca3c-4aba-81c6-e2854858a8aa.png)</br>

![alt text](../Images/InceptionV3_predictions/17538d03-ce5c-4b83-8198-6955a96df46c.png)</br>


![alt text](../Images/InceptionV3_predictions/2f372cfb-f260-4842-8b0a-98fe0d4a3529.png)</br>

![alt text](../Images/InceptionV3_predictions/b63de5e6-37d4-425c-badd-19755e76ecf3.png)



### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121/369215e3-1d49-4e5e-a29e-bb1cbe1b4f98.png)</br>

![alt text](../Images/DenseNet121/6a97d94a-eb2c-4cd3-9eeb-49081e5b0208.png)</br>

![alt text](../Images/DenseNet121/bc5a3d49-ee60-4aa7-aacb-a430130d5c56.png)</br>

![alt text](../Images/DenseNet121/ed2f3fb2-6193-4f6e-babd-3f30361e307b.png)


## 📚 Libraries Needed

1. **NumPy:** Fundamental package for numerical computing.
2. **pandas:** Data analysis and manipulation library.
3. **scikit-learn:** Machine learning library for classification, regression, and clustering.
4.  **Matplotlib:** Plotting library for creating visualizations.
5.  **Keras:** High-level neural networks API, typically used with TensorFlow backend.
6. **tqdm:** Progress bar utility for tracking iterations.
7. **seaborn:** Statistical data visualization library based on Matplotlib.

## 📊 Exploratory Data Analysis Results

### Bar Chart :-
 A bar chart showing the distribution of labels in the training dataset. It visually represents the frequency of each label category, providing an overview of how the labels are distributed across the dataset.

![alt text](../Images/bar_chart.png)


### Pie Chart :-
A pie chart illustrating the distribution of labels in the training dataset. The percentage value displayed on each segment indicates the relative frequency of each label category.


![alt text](../Images/pie_chart.png)


### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.


![alt text](../Images/image_path_distribution.png)


## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |95% ( Validation Accuracy: 0.9545)|
|InceptionV3  | 91% (Validation Accuracy:0.9091) |
|DenseNet121     | 91% (Validation Accuracy:0.9091) |
|ResNet50V2  | 82% (Validation Accuracy:0.8182) |
|MobileNetV2   | 64% (Validation Accuracy: 0.6364) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that  Xception , DenseNet121 and InceptionV3 were able to perform good on this dataset.**

Even though all of  the models implemented above are giving above 80% accuracy which is great when it comes to image recognition.

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/aaradhyasinghgaur </br>
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024