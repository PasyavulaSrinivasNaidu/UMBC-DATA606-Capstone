## Title: MalariaNet - Deep Learning for Malaria Image Classification with TensorFlow

**UMBC Data Science Master Degree Capstone - DATA606**

#### Guided by:

Dr. Chaojie (Jay) Wang

#### Author Information:
  - Name - Srinivas Naidu Pasyavula
  - University ID - QC61851
  - Github - [Srinivas Naidu Pasyavula - Github](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/)
  - LinkedIn - [Srinivas Naidu Pasyavula - LinkedIn](https://www.linkedin.com/in/srinivas-naidu-pasyavula/)
  - Powerpoint Presentation - [Project Presentation File](https://github.com/PasyavulaSrinivasNaidu/UMBC-DATA606-Capstone/blob/main/docs/Malaria%20Detection%20Presentation%20QC61851.pptx)
  - Youtube Video - [Project Presentation Video]()

## Background:
### What is it about?
Malaria, a life-threatening disease caused by Plasmodium parasites transmitted through the bite of infected mosquitoes, remains a significant global health challenge. Accurate and timely diagnosis is crucial for effective treatment and prevention of the spread of the disease. Traditional methods of malaria diagnosis, such as microscopic examination of blood smears, can be labor-intensive and require expertise, leading to delays in diagnosis and treatment.

The advancement of machine learning techniques, particularly convolutional neural networks (CNNs), offers promising opportunities for automated malaria diagnosis through image analysis. By leveraging CNNs, we can develop robust and efficient systems capable of detecting malaria parasites in blood smears with high accuracy and speed.

### Why does it matter?
Automated malaria diagnosis using CNNs can revolutionize the way malaria is detected, particularly in resource-constrained regions where access to skilled healthcare professionals may be limited. By providing a rapid and reliable diagnostic tool, we can improve patient outcomes, reduce healthcare costs, and contribute to the global efforts to control and eliminate malaria.

### What are your research questions?
1. How effective are CNNs in accurately classifying blood smear images as Parasitized (infected) or uninfected with malaria parasites?
2. What is the impact of various CNN architectures and hyperparameters on the performance of malaria detection models?
3. Can CNN-based malaria detection systems be deployed in real-world healthcare settings to enhance diagnosis and treatment outcomes?
4. What are the potential benefits of using CNNs for malaria diagnosis in resource-constrained regions?

## Data:
### Data Source: [Kaggle - Malaria Cell Images Dataset](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/data)
The dataset "Cell Images for Detecting Malaria" contains a collection of images representing blood smears of individuals infected with malaria and uninfected individuals.

### Data Size: 708MB
### Data Shape:
The dataset comprises two main categories:

**Parasitized:** This category contains images of blood smears showing red blood cells Parasitized(infected) with malaria parasites (Plasmodium).

**Uninfected:** This category contains images of blood smears showing healthy red blood cells without malaria parasites.

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
**Category 1:** Parasitized (malaria-positive)

**Category 2:** Uninfected (malaria-negative)

**Note:** The target variable (label) will be the "Parasitized" and "Uninfected", which indicates whether the blood smear is infected with malaria parasites (Category 1: Parasitized) or not (Category 2: Uninfected). Based on the Image data, Features derived from the image pixels, such as intensity, texture, and shape features.

## Steps for CNN Machine Learning Model Creation Using TensorFlow

1. **Data Preparation**:
   - Download the dataset from the tensorflow datasets using tensorflow datasets api.
   - Preprocess the images (resize, normalize pixel values, etc.).
   - Split the dataset into training, validation, and test sets.

2. **Model Architecture Design**:
   - Define the architecture of the CNN model.
   - Choose the number of layers, type of layers (convolutional, pooling, fully connected), activation functions, etc.
   - Decide on the model parameters such as filter size, number of filters, dropout rates, etc.

3. **Model Compilation**:
   - Compile the model by specifying the loss function, optimizer, and evaluation metrics.
   - Choose appropriate loss function (e.g., categorical cross-entropy for multi-class classification), optimizer (e.g., Adam), and evaluation metric (e.g., accuracy).

4. **Model Training**:
   - Train the compiled model using the training dataset.
   - Specify the number of epochs and batch size for training.
   - Monitor the training process to ensure the model is learning effectively.
   - Validate the model performance using the validation dataset.

5. **Model Evaluation**:
   - Evaluate the trained model using the test dataset.
   - Calculate metrics such as accuracy, precision, recall, and F1-score to assess model performance.
   - Analyze any discrepancies between training and validation/test performance to identify potential issues (e.g., overfitting).

6. **Model Fine-Tuning**:
   - Fine-tune the model architecture and hyperparameters based on the evaluation results.
   - Experiment with different architectures, optimization techniques, learning rates, etc., to improve model performance.

7. **Model Deployment**:
   - Save the trained model for future deployment.
   - Deploy the model in production environments for real-world applications.
   - Integrate the model into a web application.

8. **Model Monitoring and Maintenance**:
   - Monitor the deployed model's performance over time.
   - Update the model periodically with new data or retrain it on a regular basis to maintain accuracy and relevance.
   - Handle any errors or issues that arise during deployment and usage.
