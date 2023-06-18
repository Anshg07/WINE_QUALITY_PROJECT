import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('wine_quality_model.pkl')

# Define the Streamlit app
def main():
    # Set app title and description
    st.markdown(color_change_style, unsafe_allow_html=True)
    st.markdown("""<h2 align = 'center' > Designed By <b class='color-change'>ANSH GUPTA</b></h2>""", unsafe_allow_html=True)
    st.markdown("""<h1 align = 'center' > " WINE QUALITY PREDICTION " </h1>""", unsafe_allow_html=True)
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
        predictions = model.predict(input_df)
        
        # Display the predicted quality
        st.subheader("Predicted Wine Quality")
        
        if predictions[0]==0 :
            st.write("THIS IS A BAD QUALITY WINE")
        else:
            st.write('THIS IS A GOOD QUALITY WINE!! ENJOYYYY!')

# CSS style to animate the color-changing text
color_change_style = """
    <style>
    .color-change {
        animation: color_change_animation 3s infinite;
    }

    @keyframes color_change_animation {
        0% { color: #f2a4a8; }   /* Soft Pink */
        25% { color: #a6c8d2; }  /* Soft Blue */
        50% { color: #bdd4e7; }  /* Soft Lavender */
        75% { color: #e7c3a4; }  /* Soft Peach */
        100% { color: #d8ccd8; } /* Soft Gray */
        
    </style>
"""


# Run the app
if __name__ == '__main__':
    main()
