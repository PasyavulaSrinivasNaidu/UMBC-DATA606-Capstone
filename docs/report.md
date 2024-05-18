# 1. Title and Author

## Title: Malaria Detection - Deep Learning for Malaria Image Classification with TensorFlow

**UMBC Data Science Master Degree Capstone - DATA606**

#### Guided by:

Dr. Chaojie (Jay) Wang

#### Author Information:
  - **Name** - Srinivas Naidu Pasyavula
  - **University ID** - QC61851
  - **Github** - [Srinivas Naidu Pasyavula - Github](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/)
  - **LinkedIn** - [Srinivas Naidu Pasyavula - LinkedIn](https://www.linkedin.com/in/srinivas-naidu-pasyavula/)
  - **Powerpoint Presentation** - [Project Presentation File](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/blob/main/docs/Malaria%20Detection%20Presentation%20QC61851.pptx)
  - **Youtube Video** - [Project Presentation Video]()

# 2. Background
Malaria, a life-threatening disease caused by Plasmodium parasites transmitted through the bite of infected mosquitoes, remains a significant global health challenge. Accurate and timely diagnosis is crucial for effective treatment and prevention of the spread of the disease. Traditional methods of malaria diagnosis, such as microscopic examination of blood smears, can be labor-intensive and require expertise, leading to delays in diagnosis and treatment.

### What is it about?
The advancement of machine learning techniques, particularly convolutional neural networks (CNNs), offers promising opportunities for automated malaria diagnosis through image analysis. By leveraging CNNs, we can develop robust and efficient systems capable of detecting malaria parasites in blood smears with high accuracy and speed.

### Why does it matter?
Automated malaria diagnosis using CNNs can revolutionize the way malaria is detected, particularly in resource-constrained regions where access to skilled healthcare professionals may be limited. By providing a rapid and reliable diagnostic tool, we can improve patient outcomes, reduce healthcare costs, and contribute to the global efforts to control and eliminate malaria.

### What are your research questions?
1. How effective are CNNs in accurately classifying blood smear images as Parasitized (infected) or uninfected with malaria parasites?
2. What is the impact of various CNN architectures and hyperparameters on the performance of malaria detection models?
3. Can CNN-based malaria detection systems be deployed in real-world healthcare settings to enhance diagnosis and treatment outcomes?
4. What are the potential benefits of using CNNs for malaria diagnosis in resource-constrained regions?

# 3. Data:
### Data Source: [TensorFlow Datasets - Malaria Cell Images](https://www.tensorflow.org/datasets/catalog/malaria)
The dataset "Cell Images for Detecting Malaria" contains a collection of images representing blood smears of individuals infected with malaria and uninfected individuals.

### Data Size: 337MB
### Data Shape:
The dataset comprises two main categories:

**Parasitized(0):** This category contains images of blood smears showing red blood cells Parasitized(infected) with malaria parasites (Plasmodium).

**Uninfected(1):** This category contains images of blood smears showing healthy red blood cells without malaria parasites.

Each category contains a large number of images captured under different magnifications and lighting conditions. The dataset is organized into subdirectories, with each subdirectory corresponding to a specific category. The images are in JPEG format and vary in dimensions.

### Time Period - NA

### Dataset Information:

| Column               | Values/ Description |
| --------------------| --------------------|
| Total Images         | 27,558              |
| Parasitized Samples  | 13,779              |
| Uninfected Samples   | 13,779              |
| Image Dimensions     | Varying dimensions  |
| Image Format         | JPEG                |

### For the target variable (label):
**Category 1:** Parasitized(0) (malaria-positive)

**Category 2:** Uninfected(1) (malaria-negative)

**Note:** The target variable (label) will be the "Parasitized" and "Uninfected", which indicates whether the blood smear is infected with malaria parasites (Category 1: Parasitized) or not (Category 2: Uninfected). Based on the Image data, Features derived from the image pixels, such as intensity, texture, and shape features.

# 4. Exploratory Data Analysis (EDA)

The dataset does not contain any duplicate images and both labels are equally distributed

## 4.1. Data Distribution
The Malaria dataset contains a total of 27,558 cell images with equal instances of parasitized and uninfected cells from the thin blood smear slide images of segmented cells.

  ![image1](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/assets/127466900/f3124607-10c0-4368-93f9-a89ed387b79c)

## 4.2. Dataset Samples
- Label 0: parasitized (13,779 images)
- Label 1: uninfected (13,779 images)

  ![image2](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/assets/127466900/3622fef2-52d2-40f0-a70b-aa33f78280a5)

## 4.3. Data Preprocessing
Dataset of Images has been preprocessed with three steps -
- Image Resizing (224* 224 *3)
- Image Rescaling (resized_image/255)
- Image Augmentation (rot90, adjust_saturation, flip_left_right)

**Sample of Images for each label before and after preprocessing -**
### Parasitized Sample

![image](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/assets/127466900/e0c5f2e3-e463-4ed2-82bf-72c740c21d43)

### Uninfected Sample
![image](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/assets/127466900/a3caf415-deab-4e28-b381-f68983e211e5)

# 5. Model Training

## 5.1. Data Preparation

**Data Splitting :**
- Training Data: 80%
- Validation Data: 10%
- Testing Data: 10%

## 5.2. Steps for CNN Machine Learning Model Creation Using TensorFlow

- **Binary Classification:** The model distinguishes between malaria-infected and uninfected blood smear images.
- **Sequential API:** Utilized for building the neural network architecture in a linear stack of layers.
- **LeNet Model:** Employed as the backbone architecture for feature extraction and classification.
- **TensorFlow:** Framework used for implementing and training the deep learning model.
- **Key Components:** Input layer, convolutional layers, max-pooling layers, fully connected layers, and output layer for prediction.


## 5.3. Model Architecture Design

| Parameter                                        | Values/ Description |
| -------------------------------------------------| --------------------|
| Learning Rate                                    | 0.001               |
| Number of Epochs                                 | 10                  |
| Batch Size                                       | 128                 |
| Image Size                                       | 224                 |
| Number of Filters                                | 6                   |
| Kernel Size                                      | 3                   |
| Number of Strides                                | 1                   |
| Pooling Size                                     | 2                   |
| Number of Neurons in the First Dense Layer       | 100                 |
| Number of Neurons in the Second Dense Layer      | 10                  |



## 5.3. Model Compilation and Training

- Compiling the model by specifying the loss function (Binary cross-entropy), optimizer (Adam), and evaluation metrics.
- Training the compiled model using the training dataset.
- Specifing the number of epochs and batch size for training.
- Monitoring the training process to ensure the model is learning effectively.
- Validating the model performance using the validation dataset.

| Metric           | Description           |
| -----------------| ----------------------|
| True Positives   | tp                    |
| False Positives  | fp                    |
| True Negatives   | tn                    |
| False Negatives  | fn                    |
| Binary Accuracy  | accuracy              |
| Precision        | precision             |
| Recall           | recall                |
| AUC              | auc                   |


## 5.4. Model Evaluation
- Achieved accuracy of 97% on test data.
- The threshold considered is 0.5.

### 5.4.1. Model Loss
![image](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/assets/127466900/3b0679a5-7138-415b-9ab3-f8fd3e9236bf)

### 5.4.2. Model Accuracy
![image](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/assets/127466900/bde7b9a6-4cc5-491c-b21f-c298016d504d)

### 5.4.3. Evaluate the trained model using the test dataset
![image](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/assets/127466900/4fe855a1-c1b8-42d5-86f5-778838400e7c)



## 5.5. Model Saving and Deployment
- Saved the trained model for future deployment.
- Deploy the model in production environments for real-world applications.
- Integrate the model into a web application.(used Streamlit)

# 6. Application of the Trained Models

STreamlit

# 7. Conclusion
Achieved 97% accuracy on test data, demonstrating robust model performance.
Leveraged optimized hyperparameters for efficient training and accurate predictions.

## 7.1. Limitations

## 7.2. Lessons Learned

## 7.3. Future Scope:
- Boost efficiency by integrating advanced architectures like ResNet, DenseNet, or EfficientNet.
- Enhance the user experience by filtering out irrelevant images interactively.
- Developing a batch prediction model capable of processing entire datasets efficiently.

# 8. References

- [WHO](https://www.who.int/teams/global-malaria-programme/reports/world-malaria-report-2023)
- [Neuralearn](https://github.com/Neuralearn/deep-learning-with-tensorflow-2/blob/main/deep%20learning%20for%20computer%20vision/2-Malaria%20Detection%20by%20Neuralearn.ai-.ipynb)
- [TensorFlow](https://www.tensorflow.org/datasets/catalog/malaria)
- [National Library of Madecine](https://lhncbc.nlm.nih.gov/LHC-downloads/downloads.html#malaria-datasets)
- Ye, J., Si, R., & Wei, T. (2021). Classification of images by using TensorFlow. In 2021 6th International Conference on Intelligent Computing and Signal Processing (ICSP) (pp. 1-5). IEEE. DOI: 10.1109/ICSP51882.2021.9408796 
- Fuhad, K. M. Faizullah, Tuba, Jannat Ferdousey, Sarker, Md. Rabiul Ali, Momen, Sifat, Mohammed, Nabeel, & Rahman, Tanzilur. (2020). Deep Learning Based Automatic Malaria Parasite Detection from Blood Smear and Its Smartphone Based Application. Diagnostics (Basel), 10(5), 329. doi: 10.3390/diagnostics10050329
- Zhou, L., & Yu, W. (2022). Improved Convolutional Neural Image Recognition Algorithm based on LeNet-5. Journal of Computer Networks and Communications, 2022(2), 1-5. DOI: 10.1155/2022/1636203. Published by Hindawi under the CC BY 4.0 license.
