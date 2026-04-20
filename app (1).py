
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the pre-trained model and scaler
try:
    xgb_model = joblib.load('best_salary_predictor.pkl')
    scaler = joblib.load('scaler.pkl')
except FileNotFoundError:
    st.error("Model or scaler file not found. Please ensure 'best_salary_predictor.pkl' and 'scaler.pkl' are in the same directory.")
    st.stop()

# --- Streamlit Application --- 

st.set_page_config(page_title="Salary Predictor", layout="centered")

st.title("💼 Data Science Salary Predictor")
st.write("Enter the details below to get an estimated salary prediction.")
st.markdown("--- ")

# Hardcoded mappings for categorical features (simplified for demonstration)
# In a real application, you would save and load the LabelEncoder objects or a comprehensive mapping dictionary.
company_name_mapping = {
    "Tata Consultancy Services": 9160,
    "Unacademy": 9777,
    "Sasken": 8129,
    "Advanced Millennium Technologies": 417,
    "Appoids Tech Solutions": 884,
    "Other": 0 # Default/placeholder for companies not explicitly listed
}

job_title_mapping = {
    "Software Development Engineer": 933,
    "Android Developer": 28,
    "Data Scientist": 167,
    "Machine Learning Engineer": 566,
    "Data Analyst": 160,
    "Other": 0 # Default/placeholder for job titles not explicitly listed
}

location_mapping = {
    "Bangalore": 0,
    "Hyderabad": 4,
    "Pune": 8,
    "New Delhi": 7,
    "Mumbai": 6,
    "Other": 0 # Default/placeholder for locations not explicitly listed
}

employment_status_mapping = {
    "Full Time": 0,
    "Part Time": 1,
    "Internship": 2
}

job_roles_mapping = {
    "SDE": 10,
    "Android": 1,
    "Data Scientist": 3,
    "Machine Learning Engineer": 6,
    "Data Analyst": 2,
    "Other": 0 # Default/placeholder for job roles not explicitly listed
}

# --- Input Features --- 

st.header("Feature Input")

col1, col2 = st.columns(2)

with col1:
    rating = st.slider("Rating (out of 5)", min_value=1.0, max_value=5.0, value=3.8, step=0.1)
    company_name = st.selectbox("Company Name", list(company_name_mapping.keys()), index=0)
    job_title = st.selectbox("Job Title", list(job_title_mapping.keys()), index=0)
    salaries_reported = st.number_input("Salaries Reported (count)", min_value=1, max_value=100, value=1, step=1)

with col2:
    location = st.selectbox("Location", list(location_mapping.keys()), index=0)
    employment_status = st.selectbox("Employment Status", list(employment_status_mapping.keys()), index=0)
    job_roles = st.selectbox("Job Roles", list(job_roles_mapping.keys()), index=0)

# --- Prediction Logic --- 

if st.button("Predict Salary"): # Make sure the button is within the form context if using st.form
    # Map categorical inputs to their encoded integer values
    encoded_company_name = company_name_mapping[company_name]
    encoded_job_title = job_title_mapping[job_title]
    encoded_location = location_mapping[location]
    encoded_employment_status = employment_status_mapping[employment_status]
    encoded_job_roles = job_roles_mapping[job_roles]

    # Create a DataFrame for the input features
    input_data = pd.DataFrame([[rating, encoded_company_name, encoded_job_title, 
                                  salaries_reported, encoded_location, 
                                  encoded_employment_status, encoded_job_roles]],
                               columns=['Rating', 'Company Name', 'Job Title', 
                                        'Salaries Reported', 'Location', 
                                        'Employment Status', 'Job Roles'])
    
    # Ensure column order is correct if `scaler` was fitted on a specific order.
    # The columns match the order of X used during training based on the notebook.

    # Scale the input features
    scaled_input = scaler.transform(input_data)

    # Make prediction (log-transformed salary)
    log_prediction = xgb_model.predict(scaled_input)[0]

    # Inverse transform the prediction to get original salary scale
    predicted_salary = np.expm1(log_prediction)

    st.success(f"Predicted Salary: ₹{predicted_salary:,.2f}")
    st.write("\n\n*Note: This is an estimated salary based on the trained model.*")
