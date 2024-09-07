import streamlit as st
import pandas as pd
import numpy as np
import joblib
import seaborn as sns
from sklearn.preprocessing import LabelEncoder



data = pd.read_csv('global air pollution dataset.csv')
# Load the model and label encoder
best_model = joblib.load('rf_model.pkl')
label_encoder = LabelEncoder()
classes = ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
label_encoder = LabelEncoder()
label_encoder.fit(classes)



# Aesthetic Title with Emojis
st.markdown("<h1 style='text-align: center; color: #808080;'>Global Air Pollution Analysis & Prediction 🌍🏙️</h1>", unsafe_allow_html=True)


# Sidebar Navigation with Icons
st.sidebar.title("🔍 **Explore the App**")
st.sidebar.markdown("<p style='font-size: 14px; color: #1E90FF;'>Navigate through the sections:</p>", unsafe_allow_html=True)

options = ["🏠 Introduction", "📊 AQI Analysis", "🔮 Custom Predictions"]
choice = st.sidebar.radio("", options)

# Additional Aesthetic Enhancements
st.sidebar.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; font-size: 12px; color: #808080;'>Powered by Streamlit</p>", unsafe_allow_html=True)


# Introduction Section
if choice == "🏠 Introduction":
    st.subheader('Introduction')
    st.write('This app analyzes global air pollution data of 175 countries and its major cities and predicts AQI categories based on CO AQI Value, Ozone AQI Value, NO2 AQI Value, and PM2.5 AQI Value.')

# AQI Analysis Section
if choice == "📊 AQI Analysis":

    st.title('Country-wise AQI Values')

    # Step 1: Create a select box for the countries
    country_list = data['Country'].unique()
    selected_country = st.selectbox("Choose a country to display its cities AQI data:", country_list)

  
    country_data = data[data['Country'] == selected_country]

   
    city_list = country_data['City'].unique()  # List of cities in the selected country
    selected_city = st.selectbox(f"Choose a city from {selected_country}:", city_list)

   
    city_aqi = country_data[country_data['City'] == selected_city][['City', 'AQI Value', 'AQI Category']]

    # Step 5: Display the AQI data for the selected city
    st.subheader(f"Air Quality Index (AQI) for {selected_city} in {selected_country}")
    st.write(city_aqi)

    city_aqi_chart = country_data[['City', 'AQI Value']].set_index('City').sort_values(by='AQI Value', ascending=False)


    st.subheader(f'Top 20 most polluted cities of {selected_country}')
    st.bar_chart(city_aqi_chart.head(20))
    other_countries = data[(data['AQI Category'] == 'Hazardous')]

# Select the top 50 cities with the highest AQI values
    top_50 = other_countries.nlargest(50, 'AQI Value')

    # Create a styled DataFrame with highlighted AQI values
    World_Top_polluted_cities = top_50[['Country', 'City', 'AQI Value', 'AQI Category', 'NO2 AQI Value', 'CO AQI Value', 'PM2.5 AQI Value', 'Ozone AQI Value']] \
        .style.background_gradient(cmap='PuRd', subset=['AQI Value', 'NO2 AQI Value', 'CO AQI Value', 'PM2.5 AQI Value', 'Ozone AQI Value'])

    # Display the styled DataFrame in Streamlit
    st.title('Worlds Top 50 Most Polluted Cities')
    st.dataframe(World_Top_polluted_cities)

    other_countries = data[(data['AQI Category'] == 'Good')]
    top_50 = other_countries.nsmallest(50, 'AQI Value')

    # Create a styled DataFrame with highlighted AQI values
    World_Top_least_polluted_cities = top_50[['Country', 'City', 'AQI Value', 'AQI Category', 'NO2 AQI Value', 'CO AQI Value', 'PM2.5 AQI Value', 'Ozone AQI Value']] \
        .style.background_gradient(cmap='Greens', subset=['AQI Value', 'NO2 AQI Value', 'CO AQI Value', 'PM2.5 AQI Value', 'Ozone AQI Value'])

    # Display the styled DataFrame in Streamlit
    st.title('Worlds Top 50 Least Polluted Cities')
    st.dataframe(World_Top_least_polluted_cities)
    # Count the number of occurrences in each AQI category
    category_counts = data['AQI Category'].value_counts().reset_index()
    category_counts.columns = ['AQI Category', 'Count']


# Custom Predictions Section
if choice == "🔮 Custom Predictions":
    st.subheader('Predict AQI Category')
    co = st.number_input('CO AQI Value', min_value=0, max_value=500)
    ozone = st.number_input('Ozone AQI Value', min_value=0, max_value=500)
    no2 = st.number_input('NO2 AQI Value', min_value=0, max_value=500)
    pm25 = st.number_input('PM2.5 AQI Value', min_value=0, max_value=500)
    
    if st.button('Predict'):
        # Prepare the input data
        input_data = pd.DataFrame([[co, ozone, no2, pm25]])

        # Find the maximum AQI value across the pollutants
        max_data_value = input_data.max(axis=1).values[0]

        # Reshape the data for the model (if needed)
        max_data_value_reshaped = np.array([[max_data_value]])

        # Predict using the trained model
        predicted_category = best_model.predict(max_data_value_reshaped)

        # Decode the predicted label (if necessary)
        predicted_category_label = label_encoder.inverse_transform(predicted_category)

        # Display the prediction result in Streamlit
        st.write("Predicted AQI Category:", predicted_category_label[0])







