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

# Define conversion functions
def convert_distance(value, from_unit, to_unit):
    # Conversion rates based on 1 meter
    units_in_meters = {
        "Kilometers": 1000,
        "Meters": 1,
        "Miles": 1609.34,
        "Yards": 0.9144,
        "Feet": 0.3048
    }
    
    value_in_meters = value * units_in_meters[from_unit]
    conversion_rate = units_in_meters[to_unit]
    
    return value_in_meters / conversion_rate

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Celsius to other units
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    
    # Fahrenheit to other units
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    
    # Kelvin to other units
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

def convert_weight(value, from_unit, to_unit):
    # Conversion rates based on 1 kilogram
    units_in_kg = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    
    value_in_kg = value * units_in_kg[from_unit]
    conversion_rate = units_in_kg[to_unit]
    
    return value_in_kg / conversion_rate

def convert_pressure(value, from_unit, to_unit):
    # Conversion rates based on Pascal (Pa)
    units_in_pa = {
        "Pascal": 1,
        "Bar": 100000,
        "PSI": 6894.76,
        "Atmosphere": 101325
    }
    
    value_in_pa = value * units_in_pa[from_unit]
    conversion_rate = units_in_pa[to_unit]
    
    return value_in_pa / conversion_rate

# Select units based on the category
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
    # Proceed with the conversion logic when the button is pressed
    if st.button("Convert"):
        if category == "Distance":
            result = convert_distance(value, from_unit, to_unit)
        elif category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif category == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        elif category == "Pressure":
            result = convert_pressure(value, from_unit, to_unit)
        
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit} 🎉")
