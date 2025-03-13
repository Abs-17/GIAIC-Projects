import streamlit as st
from collections import deque
import pandas as pd
import numpy as np
import plotly.express as px

# Factors for unit conversion
conversion_factors = {
    "Length": {
        "Meters": 1, "Centimeters": 100, "Feet": 3.28084, "Inches": 39.3701,
        "Kilometers": 0.001, "Millimeters": 1000, "Yards": 1.09361, "Miles": 0.000621371
    },
    "Weight": {
        "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274, "Stones": 0.157473
    },
    "Temperature": {
        "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15,
        "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9, "Kelvin to Celsius": lambda x: x - 273.15
    },
    "Time": {
        "Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800
    },
    "Speed": {
        "Meters per Second": 1, "Kilometers per Hour": 3.6, "Miles per Hour": 2.23694, "Feet per Second": 3.28084
    }
}

# Conversion history (persistent storage)
if "history" not in st.session_state:
    st.session_state.history = deque(maxlen=5)
if "from_unit" not in st.session_state:
    st.session_state.from_unit = None
if "to_unit" not in st.session_state:
    st.session_state.to_unit = None

# App Title & Layout
st.set_page_config(page_title="The Unit Converter", layout="centered")
st.title("🔢 The Unit Converter")

# Main Conversion UI
col1, col2, col3 = st.columns([3, 1, 3])

category_unit = st.selectbox("Select a category", list(conversion_factors.keys()))

# Ensure stored units exist in the current category
available_units = list(conversion_factors[category_unit].keys())
if st.session_state.from_unit not in available_units:
    st.session_state.from_unit = available_units[0]
if st.session_state.to_unit not in available_units:
    st.session_state.to_unit = available_units[1] if len(available_units) > 1 else available_units[0]

from_unit = col1.selectbox("From", available_units, index=available_units.index(st.session_state.from_unit))
to_unit = col3.selectbox("To", available_units, index=available_units.index(st.session_state.to_unit))
value = col1.number_input("Enter value", min_value=0.0, step=0.1, format="%.2f")

if col2.button("🔄 Swap"):
    st.session_state.from_unit, st.session_state.to_unit = st.session_state.to_unit, st.session_state.from_unit
    from_unit, to_unit = st.session_state.from_unit, st.session_state.to_unit

# Perform Conversion
if category_unit == "Temperature":
    if from_unit == "Celsius" and to_unit in conversion_factors[category_unit]:
        unit_converted = conversion_factors[category_unit][to_unit](value)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        unit_converted = conversion_factors[category_unit]["Fahrenheit to Celsius"](value)
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        unit_converted = conversion_factors[category_unit]["Kelvin to Celsius"](value)
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        unit_converted = conversion_factors[category_unit]["Kelvin"](conversion_factors[category_unit]["Fahrenheit to Celsius"](value))
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        unit_converted = conversion_factors[category_unit]["Fahrenheit"](conversion_factors[category_unit]["Kelvin to Celsius"](value))
    else:
        unit_converted = value
else:
    unit_converted = value * conversion_factors[category_unit][from_unit] / conversion_factors[category_unit][to_unit]

col3.metric(label=f"{value} {from_unit}", value=f"{unit_converted:.2f} {to_unit}")

# Save history
st.session_state.history.appendleft({
    "Input": value, "From": from_unit, "To": to_unit, "Output": round(unit_converted, 2)
})

# Conversion History Section
with st.expander("📜 Conversion History"):
    if st.session_state.history:
        df_history = pd.DataFrame(st.session_state.history)
        st.table(df_history)
        st.download_button("📥 Download History", df_history.to_csv(index=False), "conversion_history.csv", "text/csv")
    else:
        st.write("No conversions yet!")
