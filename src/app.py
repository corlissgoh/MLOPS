import streamlit as st
import pandas as pd
import pycaret.classification as pc
from hydra import initialize, compose
import os

# Hydra Configuration
def load_config():
    # Initialize Hydra
    config_path = os.path.join(os.path.dirname(__file__), 'conf')
    initialize(config_path=config_path)
    cfg = compose(config_name='config')
    return cfg

# Load Hydra config
config = load_config()

# Load the model using PyCaret
model_path = config.model.path
model = pc.load_model(model_path)

# Streamlit UI
st.title('Mushroom Species Prediction')
st.write("Enter the details to predict if the mushroom is edible or poisonous")

# Collect input data from the user
cap_shape = st.selectbox('Cap Shape', config.inputs.cap_shape)
cap_surface = st.selectbox('Cap Surface', config.inputs.cap_surface)
cap_color = st.selectbox('Cap Color', config.inputs.cap_color)
bruises = st.selectbox('Bruises', config.inputs.bruises)
odor = st.selectbox('Odor', config.inputs.odor)
gill_attachment = st.selectbox('Gill Attachment', config.inputs.gill_attachment)
gill_spacing = st.selectbox('Gill Spacing', config.inputs.gill_spacing)
gill_size = st.selectbox('Gill Size', config.inputs.gill_size)
gill_color = st.selectbox('Gill Color', config.inputs.gill_color)
stalk_shape = st.selectbox('Stalk Shape', config.inputs.stalk_shape)
stalk_root = st.selectbox('Stalk Root', config.inputs.stalk_root)
stalk_surface_above_ring = st.selectbox('Stalk Surface Above Ring', config.inputs.stalk_surface_above_ring)
stalk_surface_below_ring = st.selectbox('Stalk Surface Below Ring', config.inputs.stalk_surface_below_ring)
stalk_color_above_ring = st.selectbox('Stalk Color Above Ring', config.inputs.stalk_color_above_ring)
stalk_color_below_ring = st.selectbox('Stalk Color Below Ring', config.inputs.stalk_color_below_ring)
veil_type = st.selectbox('Veil Type', config.inputs.veil_type)
veil_color = st.selectbox('Veil Color', config.inputs.veil_color)
ring_number = st.selectbox('Ring Number', config.inputs.ring_number)
ring_type = st.selectbox('Ring Type', config.inputs.ring_type)
spore_print_color = st.selectbox('Spore Print Color', config.inputs.spore_print_color)
population = st.selectbox('Population', config.inputs.population)
habitat = st.selectbox('Habitat', config.inputs.habitat)

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'cap-shape': [cap_shape],
    'cap-surface': [cap_surface],
    'cap-color': [cap_color],
    'bruises': [bruises],
    'odor': [odor],
    'gill-attachment': [gill_attachment],
    'gill-spacing': [gill_spacing],
    'gill-size': [gill_size],
    'gill-color': [gill_color],
    'stalk-shape': [stalk_shape],
    'stalk-root': [stalk_root],
    'stalk-surface-above-ring': [stalk_surface_above_ring],
    'stalk-surface-below-ring': [stalk_surface_below_ring],
    'stalk-color-above-ring': [stalk_color_above_ring],
    'stalk-color-below-ring': [stalk_color_below_ring],
    'veil-type': [veil_type],
    'veil-color': [veil_color],
    'ring-number': [ring_number],
    'ring-type': [ring_type],
    'spore-print-color': [spore_print_color],
    'population': [population],
    'habitat': [habitat]
})

# Make predictions
prediction = model.predict(input_data)
st.write(f'The predicted class is: {prediction[0]}')
