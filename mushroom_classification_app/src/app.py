import streamlit as st
import pandas as pd
import pycaret.classification as pc
from hydra import initialize, compose
import os

# Hydra Configuration
#def load_config():
    # Initialize Hydra
    #config_path = os.path.join(os.path.dirname(__file__), '../conf')
    #initialize(config_path=config_path)
    #cfg = compose(config_name='config.yaml')
    #return cfg

# Load Hydra config
#config = load_config()

# Load the model using PyCaret
#model_path = config.model.path
#model = pc.load_model(model_path)
model = pc.load_model('models/mushroom-pipeline')

# Streamlit UI
st.title('Mushroom Species Prediction')
st.write("Enter the details to predict if the mushroom is edible or poisonous")

# Collect input data from the user
cap_shape = st.selectbox('Cap Shape', ['convex', 'bell', 'conical', 'flat', 'knobbed', 'sunken'])
cap_surface = st.selectbox('Cap Surface', ['smooth', 'scaly', 'fibrous', 'grooves'])
cap_color = st.selectbox('Cap Color', ['brown', 'buff', 'cinnamon', 'gray', 'green', 'pink', 'purple', 'red', 'white', 'yellow'])
bruises = st.selectbox('Bruises', ['bruises', 'no'])
odor = st.selectbox('Odor', ['almond', 'anise', 'creosote', 'fishy', 'foul', 'musty', 'none', 'pungent', 'spicy'])
gill_attachment = st.selectbox('Gill Attachment', ['attached', 'free'])
gill_spacing = st.selectbox('Gill Spacing', ['close', 'crowded', 'distant'])
gill_size = st.selectbox('Gill Size', ['broad', 'narrow'])
gill_color = st.selectbox('Gill Color', ['black', 'brown', 'buff', 'chocolate', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'])
stalk_shape = st.selectbox('Stalk Shape', ['enlarging', 'tapering'])
stalk_root = st.selectbox('Stalk Root', ['bulbous', 'club', 'equal', 'rhizomorph', 'rooted', 'missing'])
stalk_surface_above_ring = st.selectbox('Stalk Surface Above Ring', ['fibrous', 'scaly', 'smooth'])
stalk_surface_below_ring = st.selectbox('Stalk Surface Below Ring', ['fibrous', 'scaly', 'smooth'])
stalk_color_above_ring = st.selectbox('Stalk Color Above Ring', ['brown', 'buff', 'cinnamon', 'gray', 'orange', 'pink', 'red', 'white', 'yellow'])
stalk_color_below_ring = st.selectbox('Stalk Color Below Ring', ['brown', 'buff', 'cinnamon', 'gray', 'orange', 'pink', 'red', 'white', 'yellow'])
veil_type = st.selectbox('Veil Type', ['partial', 'universal'])
veil_color = st.selectbox('Veil Color', ['brown', 'orange', 'white', 'yellow'])
ring_number = st.selectbox('Ring Number', ['none', 'one', 'two'])
ring_type = st.selectbox('Ring Type', ['cobwebby', 'evanescent', 'flaring', 'large', 'none', 'pendant', 'sheathing'])
spore_print_color = st.selectbox('Spore Print Color', ['black', 'brown', 'buff', 'chocolate', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'])
population = st.selectbox('Population', ['abundant', 'clustered', 'numerous', 'scattered', 'several', 'solitary'])
habitat = st.selectbox('Habitat', ['grasses', 'leaves', 'meadows', 'paths', 'urban', 'waste', 'woods'])

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
