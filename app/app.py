import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Page Configurations
st.set_page_config(
    page_title="Malaria Infection Detection",
    page_icon="🦠",
    layout="centered"
)

# Load the pre-trained model
model = tf.keras.models.load_model('malaria_detection_lenet_model.h5')

# Function to predict whether the image is infected or not
def predict_image(image):
    image = Image.open(image)
    image = image.resize((224, 224))  # Resize the image
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Expand dimensions to match batch size
    prediction = model.predict(image)
    return prediction

# Function to determine the result based on the prediction
def parasite_or_not(prediction):
    if prediction < 0.5:
        return 'Parasite', prediction
    else:
        return 'Un-Infected', prediction

# Main Function
def main():
    # Set title and description
    st.title("Malaria Infection Detection")
    st.markdown("Upload an image to check if it's infected or not.")

    # File uploader section
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Predict button
        if st.button('Check for Infection'):
            with st.spinner('Analyzing...'):
                prediction, confidence = parasite_or_not(predict_image(uploaded_file))
                # Display prediction result with confidence
                if prediction == 'Parasite':
                    st.error(f"Prediction: {prediction} with confidence: {confidence[0][0]:.2f}")
                else:
                    st.success(f"Prediction: {prediction} with confidence: {confidence[0][0]:.2f}")
            # Disclaimer
            st.warning("Please note: This is a demonstration model and not for medical diagnosis.")

        # Reset button
        if st.button('Reset'):
            st.image("", caption='Uploaded Image', use_column_width=True)

# Run the main function
if __name__ == "__main__":
    main()
