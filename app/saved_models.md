# Malaria Detection Model

This repository contains a pre-trained model for detecting malaria infection in images.

## Model Description

The model is built using TensorFlow and is based on the LeNet architecture. It has been trained on a dataset of malaria-infected and uninfected cell images.

## Usage

You can download the pre-trained model from the following Google Drive link:

[Download Model](https://drive.google.com/drive/folders/1CzphNPkAhIBx5NpPW1RdezurYdTUIkMB?usp=sharing)

## Instructions

1. Download the model file from the provided Google Drive link.
2. Load the model in your TensorFlow application using `tf.keras.models.load_model`.
3. Use the loaded model to make predictions on new malaria cell images.

## Example Usage

```python
import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model('path/to/downloaded/model.h5')

# Use the model for inference
# (Add your code here)
