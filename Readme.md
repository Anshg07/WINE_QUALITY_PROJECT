# Wine Quality Prediction with Streamlit App

This project aims to predict the quality of wine using a Random Forest Machine Learning model deployed with Streamlit.

## Overview
This Streamlit app utilizes a Random Forest model trained on a dataset of various attributes of wine to predict the quality of wine. Users can input different features of the wine, such as acidity, pH level, alcohol content, etc., and the app will provide a prediction of the wine's quality.

## Installation
To run this Streamlit app locally, follow these steps:

1. Clone this repository:

```
git clone https://github.com/Anshg07/WINE_QUALITY_PROJECT.git
```

2. Navigate to the project directory:

```
cd WINE_QUALITY_PROJECT
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the Streamlit app:

```
streamlit run app.py
```

5. Open your web browser and go to `localhost:8501` to access the app.

## Usage
Once the Streamlit app is running, users can interact with it through their web browser. They can input various features of the wine, such as acidity, pH level, alcohol content, etc., and the app will provide a prediction of the wine's quality.

## Dataset
The dataset used for training the Random Forest model is the Wine Quality Dataset, which is publicly available on the UCI Machine Learning Repository. It contains various attributes of wine, such as fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, and quality.

## Model
The Random Forest model used in this app is trained on the Wine Quality Dataset to predict the quality of wine based on its features. Random Forest is an ensemble learning method that operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.

## About
This project is created and maintained by Ansh Gupta. Feel free to reach out with any questions or suggestions.