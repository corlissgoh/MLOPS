import streamlit as st
import pandas as pd
import mlflow
import mlflow.sklearn
from datetime import datetime
import pycaret.regression as pr

# Load the MLflow model using the file path

model = pr.load_model('models/hdb_resale_pipeline')
# Streamlit app
st.title('HDB Resale Price Prediction')

st.write('Enter the details of the HDB flat to predict its resale price.')

# User inputs for features
block = st.number_input('Block Number', value=1)
street_name = st.text_input('Street Name', value='E.g Bishan Street 1')
town = st.text_input('Town', value='E.g Bishan')
flat_type = st.selectbox('Flat Type', options=['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE'])
storey_range = st.selectbox('Storey Range', options=['1-3', '4-6', '7-9', '10-12', '13-15', '16-18', '19-21', '22-24', '25-27', '28-30', '31-33', '34-36', '37-39', '40-42', '43-45', '46-48', '49-50'])
floor_area_sqm = st.number_input('Floor Area (sqm)', value=50)
flat_model = st.selectbox('Flat Model', options=['New Generation', 'Model A','Model A2','Premium Apartment', 'Improved','Maisonette', 'Apartment', 'Type S1','Type S2'])
lease_commence_date = st.number_input('Lease Commence Year', min_value=1900, max_value=datetime.now().year, value=2000)
cbd_dist = st.number_input('Distance to CBD (m)', value=5.0)
min_dist_mrt = st.number_input('Distance to Nearest MRT (m)', value=5.0)

# Compute remaining years of lease
current_date = datetime.now()
remaining_year = 99 - (current_date.year - lease_commence_date)

# Create a DataFrame from user inputs
input_data = pd.DataFrame({
    'block': [block],
    'street_name': [street_name],
    'town': [town],
    'flat_type': [flat_type],
    'storey_range': [storey_range],
    'floor_area_sqm': [floor_area_sqm],
    'flat_model': [flat_model],
    'remaining_years': [remaining_year],
    'cbd_dist': [cbd_dist],
    'min_dist_mrt': [min_dist_mrt]
})

# Predict button
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted Resale Price: ${prediction[0]:,.2f}')
