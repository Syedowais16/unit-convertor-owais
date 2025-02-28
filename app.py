import streamlit as st
import pint

# Initialize the unit registry
ureg = pint.UnitRegistry()

# Streamlit App Title
st.title("🌍 Google-Like Unit Converter")

# Supported categories and units
categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter", "millimeter"],
    "Weight": ["kilogram", "gram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "quart", "pint", "cup"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot"],
}

# User selects category
category = st.selectbox("Select Category", list(categories.keys()))

# Dropdowns for selecting units
from_unit = st.selectbox("From Unit", categories[category])
to_unit = st.selectbox("To Unit", categories[category])

# Input field for user value
value = st.number_input("Enter Value", min_value=0.0, format="%.6f")

# Conversion logic
if st.button("Convert"):
    try:
        # Special case for temperature conversion
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value  # No conversion needed
        else:
            # Regular conversion using Pint
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        st.success(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")

    except Exception as e:
        st.error(f"Conversion error: {str(e)}")
