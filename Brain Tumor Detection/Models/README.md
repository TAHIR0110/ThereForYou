# Brain Tumor Detection

## 🎯 Goal
The main purpose of this project is to **identify brain tumor using MRI images and classify between different types of it such as maningioma , glioma , pituatary tumor** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/denizkavi1/brain-tumor**

## 🧾 Description

This project involves the comparative analysis of **Five** Keras image detection models, namely **ResNet101V2** , **ResNet50V2** , **InceptionV3** , **DenseNet121** and **Xception**  applied to a specific dataset. The dataset consists of annotated images related to a particular domain, and the objectives include training and evaluating these models to compare their accuracy scores and performance metrics. Additionally, exploratory data analysis (EDA) techniques are employed to understand the dataset's characteristics, explore class distributions, detect imbalances, and identify areas for potential improvement. The methodology encompasses data preparation, model training, evaluation, comparative analysis of accuracy and performance metrics, and visualization of EDA insights. 

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

![alt text](../Images/Xception_predictions/34f1e7e1-b284-412f-8f39-e275b51ab1da.png)</br>

![alt text](../Images/Xception_predictions/5d2e80b8-a395-455f-9fd9-8abd5b066c87.png)</br>

![alt text](../Images/Xception_predictions/cff8b585-8231-46b5-beb4-e21fae88a673.png)</br>

![alt text](../Images/Xception_predictions/fd604494-b52f-4f9e-a6b0-b7756c65c18d.png)


### ResNet101V2

Incorporating the ResNet101V2 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained ResNet101V2 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting ResNet101V2:**
- Deep Architecture (ResNet101V2's deeper network allows for learning complex patterns and features in images.)
- Proven Accuracy (ResNet101V2 consistently ranks high in various image recognition benchmarks.)
- Extensive Parameters (44.5M)
- Robust Efficiency (CPU - 50, GPU - 15)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/ResNet101V2_predictions/03a977fd-9400-46c8-9233-c9a4097fac07.png)</br>

![alt text](../Images/ResNet101V2_predictions/12114c34-012f-40d9-980f-4152ef2fbf60.png)</br>

![alt text](../Images/ResNet101V2_predictions/33a24aa6-b8b5-40d7-9903-77faaee5276a.png)</br>

![alt text](../Images/ResNet101V2_predictions/b1962cdd-9012-4b82-93f5-21a6a3a4188f.png)


### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/Resnet50V2_predictions/3b7cb05f-555b-4b83-ab6e-c9c66f04ebab.png)</br>

![alt text](../Images/Resnet50V2_predictions/4095f7df-54e0-4bda-9e82-647ba9e52d06.png)</br>

![alt text](../Images/Resnet50V2_predictions/b35aec0b-f342-4954-8aa0-be87dfdd1956.png)</br>

![alt text](../Images/Resnet50V2_predictions/b7b638ba-f76d-4f9a-9c75-136451a8964d.png)






### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/InceptionV3_predictions/04794cc7-d5b7-4ecc-b0a9-35f18c1ebf15.png)</br>

![alt text](../Images/InceptionV3_predictions/13462d45-4027-4207-be4e-a483cee5bb51.png)</br>

![alt text](../Images/InceptionV3_predictions/6f28d911-f7b4-4e11-a86a-f7fe372600ae.png)</br>

![alt text](../Images/InceptionV3_predictions/bb460701-375f-4050-ac83-9b85836db058.png)</br>

### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121/34527189-008a-4db2-96ee-ddcbe8994926.png)</br>

![alt text](../Images/DenseNet121/5fd59feb-d114-4aa6-b81b-71ac541bb884.png)</br>

![alt text](../Images/DenseNet121/81b76804-a42a-47fb-8a37-b743664af234.png)</br>

![alt text](../Images/DenseNet121/f4e50ab1-3c2d-426a-b11b-b2d6c2e0e1a3.png)


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

![alt text](../Images/bar.png)


### Pie Chart :-
A pie chart illustrating the distribution of labels in the training dataset. The percentage value displayed on each segment indicates the relative frequency of each label category.

![alt text](../Images/pie.png)

### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.

![alt text](../Images/image_path_distribution.png)



## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |97% ( Validation Accuracy: 0.9674)|
|InceptionV3  | 96% (Validation Accuracy: 0.9601) |
|DenseNet121     | 96% (Validation Accuracy:0.9601) |
|ResNet50V2  | 82% (Validation Accuracy: 0.8225) |
|ResNet101V2     | 96% (Validation Accuracy:  0.9638) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that Xception , ResNet101V2 and DenseNet121 were able to perform good on this dataset.**

Even though most of  the models implemented above are giving above 90% accuracy which is great when it comes to image recognition and that too of an MRI dataset after modifying the models a litle bit.

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024