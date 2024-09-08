# Country and City-wise AQI Visualization

This project provides an interactive web-based tool to visualize Air Quality Index (AQI) data by country and city. Users can select a country and then filter by city to view AQI values and categories. The app is built using **Streamlit** and allows easy interaction with large datasets.

## Features

- **Country and City Selection**: Users can select a country and then choose a city to view its AQI value and category.
- **Dynamic Data Display**: Based on the selected country and city, the app shows the AQI value and category.
- **User-Friendly Interface**: The application is designed using Streamlit for ease of use.

## AQI Categories

The AQI categories are based on the AQI value and are classified as follows:

- **Good**: Air quality is satisfactory.
- **Moderate**: Air quality is acceptable, but may pose a risk for sensitive individuals.
- **Unhealthy for Sensitive Groups**: Sensitive groups may experience health effects.
- **Unhealthy**: Everyone may experience health effects.
- **Very Unhealthy**: Health alert for everyone.
- **Hazardous**: Emergency conditions; everyone may be affected.

## Technologies Used

- **Python**: Backend language for data processing.
- **Streamlit**: Frontend framework for building the interactive web app.
- **Pandas**: Data manipulation and processing.
- **Scikit-learn**: For possible machine learning extensions (e.g., AQI prediction).

## Data Sources

- **KAGGLE API**:
    ```bash
    kaggle datasets download -d hasibalmuzdadid/global-air-pollution-dataset   
    ```

## Installation

### Prerequisites
- Python 3.x
- Pip package manager

### Steps to Install
1. Clone the repository:
    ```bash
    git clone https://github.com/shaivi04/Global-AQI-analysis.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Global-AQI-analysis
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Live Demo
- You can access the live demo of the application here: [Global AQI Analysis](https://global-aqi-analysis-gxgxq8pujn2y6wp2ngpotn.streamlit.app/)

