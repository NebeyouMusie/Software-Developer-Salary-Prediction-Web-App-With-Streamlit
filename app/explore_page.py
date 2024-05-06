import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# function to the shorten the 'Country' column based on the unique values and count
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

# function to clean the 'YearsCodePro' column
def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


# function to clean the 'EdLevel' column
def clean_education(x):
    if "Bachelor’s degree" in x:
        return "Bachelor’s degree"
    if "Master’s degree" in x:
        return "Master’s degree"
    if "Professional degree" in x or 'Associate degree' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


st.cache_data
def load_data():
    df = pd.read_csv('./Software-Developer-Salary-Prediction-Web-App-With-Streamlit/app/cleaned_data.csv')
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2023
    """
    )

    data = df["Country"].value_counts()
    countries = [
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
    ]


    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=countries, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)