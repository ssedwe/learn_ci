

import streamlit as st
from utils import calculate_powers

st.title("Power Calculator")
st.write("Enter a number to calculate its powers")

n = st.number_input("Enter a number", value=1)

results = calculate_powers(n)

st.write(f"Square: {results['square']}")
st.write(f"Cube: {results['cube']}")
st.write(f"Fifth Power: {results['fifth_power']}")