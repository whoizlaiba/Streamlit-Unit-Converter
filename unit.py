import streamlit as st

# Inject custom CSS to style the app
st.markdown("""
    <style>
    .title {
        color: #4CAF50;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    .stSelectbox, .stNumberInput {
        font-size: 16px;
    }
    .stButton {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stButton:hover {
        background-color: #45a049;
    }
    .stWrite {
        font-size: 18px;
        color: #333;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app with custom class
st.markdown('<div class="title">Unit Converter</div>', unsafe_allow_html=True)

# Select category for conversion
category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

# Define the conversion for each category (Units only for simplicity)
if category == "Distance":
    units = ["Kilometers", "Meters", "Miles", "Yards", "Feet"]
elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
elif category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
elif category == "Pressure":
    units = ["Pascal", "Bar", "PSI", "Atmosphere"]

# Select from and to unit
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

# Input value to convert
value = st.number_input("Enter value", min_value=0.0, step=0.1)

# Validate the input value
if value <= 0:
    st.error("Value must be greater than 0 to proceed with conversion!")
else:
    # Proceed with the conversion logic (currently a placeholder)
    if st.button("Convert"):
        # You can implement actual conversion logic here, for now, we'll just display the input
        st.success(f"Convert {value} {from_unit} to {to_unit}🎉")
        
       



