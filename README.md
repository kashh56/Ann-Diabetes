ANN-Diabetes
============

**ANN-Diabetes** is a machine learning project that implements an Artificial Neural Network (ANN) model to predict diabetes risk based on patient data. The project uses a publicly available diabetes dataset and incorporates _hyperparameter tuning_ to optimize the model's performance. Additionally, the model is deployed on Streamlit, allowing users to interact with it through a user-friendly web interface.

Table of Contents
-----------------

*   [About](#about)
*   [Dataset](#dataset)
*   [Model](#model)
*   [Hyperparameter Tuning](#hyperparameter-tuning)
*   [Streamlit Deployment](#streamlit-deployment)
*   [Contributing](#contributing)
*   [License](#license)

About
-----

The **ANN-Diabetes** model is trained to predict whether a patient has diabetes based on factors like age, BMI, glucose levels, and insulin levels. The project involves cleaning the dataset, preparing the data, training an ANN model, and tuning hyperparameters for optimal performance. The trained model is then deployed on Streamlit, providing a simple interface for users to input their own data and get predictions.

Dataset
-------

The dataset used in this project is the Pima Indians Diabetes Database, which contains 768 instances with 8 features. These features include:

*   Pregnancies
*   Glucose
*   Blood Pressure
*   Skin Thickness
*   Insulin
*   BMI (Body Mass Index)
*   Diabetes Pedigree Function
*   Age

The target variable is whether or not the patient has diabetes (1: Positive, 0: Negative).

Model
-----

The model is an Artificial Neural Network (ANN) built using the **Keras** library, with **TensorFlow** as the backend. 
The model architecture consists of:

*   Input layer
*   Hidden layers with ReLU activation functions
*   Output layer with a single neuron (for binary classification)

Hyperparameter Tuning
---------------------

To improve the performance of the model, we performed hyperparameter tuning using techniques such as:

*   Grid Search
*   Random Search

The following hyperparameters were tuned:

*   Number of hidden layers
*   Number of neurons in each layer
*   activation function


Streamlit Deployment
--------------------

Once the model was trained and optimized, we deployed it using **Streamlit**. Streamlit provides a fast and interactive way to build web apps for machine learning projects. The app allows users to input their own data (such as age, BMI, glucose levels, etc.) and get a prediction of whether they have diabetes.

To interact with the model on Streamlit, visit the deployed app:

[Live Streamlit App](https://ann-diabetes-akash.streamlit.app/)

We are open to feedback.
Contributing
------------

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Please make sure to follow the guidelines below:

*   Ensure your code follows the existing style guide
*   Write unit tests for any new features
*   Update the documentation if needed

License
-------

This project is licensed under the MIT License - 
