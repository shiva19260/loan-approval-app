# Loan Approval Prediction Web App

This project is a machine learning-based web application that predicts whether a loan will be approved or denied based on certain features. It uses a trained machine learning model to make predictions and is deployed using Flask.

## Table of Contents:
- [Technologies Used](#technologies-used)
- [Input Features Required](#input-features-required)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Project Link](#project-link)

## Technologies Used:
- **Flask**: For building the web application.
- **Machine Learning Model**: Trained using scikit-learn.
- **Joblib**: For saving and loading the trained model and scaler.
- **AWS EC2**: Deployed on AWS EC2 for public access.
- **HTML**: For the web application's front-end interface.

## Input Features Required:
To get a loan approval prediction, provide the following information:

1. **Gender**: Applicant's gender (Male/Female)
2. **Marital Status**: Marital status (Married/Single)
3. **Dependents**: Number of dependents (0, 1, 2, etc.)
4. **Education**: Education status (Graduate/Not Graduate)
5. **Self-Employed**: Whether the applicant is self-employed or not (Yes/No)
6. **Applicant Income**: Monthly income of the applicant (numeric value)
7. **Coapplicant Income**: Monthly income of the coapplicant (numeric value)
8. **Loan Amount**: The loan amount requested (numeric value)
9. **Loan Amount Term**: The loan term in months (numeric value)
10. **Credit History**: Credit history (1 = good, 0 = poor)
11. **Property Area**: Type of property area (Urban/Semiurban/Rural)

## Setup Instructions:
To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/shiva19260/loan-approval-app.git

2. Navigate to the project directory:
     cd loan-approval-app
   
4. Install the required dependencies:
     pip install -r requirements.txt

5. Run the Flask application:
     python app.py

6. Open your browser and go to the following URL:
     http://13.61.146.96:5000/

How to Use:
1. Open the web application using the URL above.
2. Fill in the form with the required information.
3. Click Submit to get the loan approval prediction.
4. The prediction will be displayed as either "Loan Approved" or "Loan Denied".

Project Link:
Access the live project deployed on AWS EC2 here:
## Project Link:
Access the live project deployed on AWS EC2 here: [Loan Approval Prediction App](http://13.61.146.96:5000/)


   

