import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('./Software-Developer-Salary-Prediction-Web-App-With-Streamlit/app/model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title('Software Developer Salary Prediction')

    st.write('''### We need some information to predict the salary ''')

    countries = (
        'United States of America',                              
        'Germany',                                                 
        'United Kingdom of Great Britain and Northern Ireland',     
        'Canada',                                                   
        'India',                                                    
        'France',                                                   
        'Netherlands',                                              
        'Australia',                                                 
        'Brazil',                                                    
        'Spain',                                                     
        'Sweden',                                                    
        'Italy',                                                     
        'Poland',                                                    
        'Switzerland',                                               
        'Denmark',                                                   
        'Norway',                                                    
        'Israel',
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox('Country', countries)
    education = st.selectbox('Education Level', education)

    experience = st.slider('Years of Experience', 0, 50, 3)

    ok = st.button('Calculate Salary')
    
    if ok:
    # Ensure that the country and education variables are correctly transformed
    # into numerical values before they are passed to the model.
        X = np.array([[country, education, experience ]])
        X[:, 0] = le_country.transform([X[:,0]])
        X[:, 1] = le_education.transform([X[:,1]])
        X = X.astype(float)

        try:
            salary = model.predict(X)
            st.subheader(f'The estimated salary is ${salary[0]:.2f}')
        except Exception as e:
            st.error(f"An error occurred: {e}")