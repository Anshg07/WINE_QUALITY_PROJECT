import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('wine_quality_model.pkl')

# Function to preprocess the input data
def preprocess_input(data):
    # Perform any necessary data preprocessing steps
    # e.g., scaling, encoding categorical variables, etc.
    # Return the preprocessed data as a DataFrame or numpy array
    processed_data = data  # Placeholder for preprocessing steps
    return processed_data

# Function to make predictions
def predict_quality(data):
    # Preprocess the input data
    processed_data = preprocess_input(data)
    
    # Make predictions using the pre-trained model
    predictions = model.predict(processed_data)
    
    return predictions

# Define the Streamlit app
def main():
    # Set app title and description
    st.title("Wine Quality Prediction")
    st.write("This app predicts the quality of wine based on input features.")
    
    # Create input fields for the wine features
    fixed_acidity = st.number_input("Fixed Acidity")
    volatile_acidity = st.number_input("Volatile Acidity")
    citric_acid = st.number_input("Citric Acid")
    residual_sugar = st.number_input("Residual Sugar")
    chlorides = st.number_input("Chlorides")
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide")
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide")
    density = st.number_input("Density")
    pH = st.number_input("pH")
    sulphates = st.number_input("Sulphates")
    alcohol = st.number_input("Alcohol")
    
    # Create a dictionary with the input data
    input_data = {
        'fixed acidity': fixed_acidity,
        'volatile acidity': volatile_acidity,
        'citric acid': citric_acid,
        'residual sugar': residual_sugar,
        'chlorides': chlorides,
        'free sulfur dioxide': free_sulfur_dioxide,
        'total sulfur dioxide': total_sulfur_dioxide,
        'density': density,
        'pH': pH,
        'sulphates': sulphates,
        'alcohol': alcohol
    }
    
    # Display the prediction button
    if st.button("Predict"):
        # Convert the input data into a DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Make predictions
        predictions = predict_quality(input_df)
        
        # Display the predicted quality
        st.subheader("Predicted Wine Quality")
        
        if predictions[0]==0 :
            st.write("THIS IS A BAD QUALITY WINE")
        else:
            st.write('THIS IS A GOOD QUALITY WINE!! ENJOYYYY!')
        st.write(predictions[0])

# Run the app
if __name__ == '__main__':
    main()