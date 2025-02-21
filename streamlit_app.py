# -----------------------------------
# Author: Aryan Mittal
# Program: AP Performance Task
# Version 1.0
# Development Date(s): 2/21/25
# -----------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load data
df = pd.read_csv("College Majors & Incomes.csv")
ranks = df["Rank"].tolist()
majors = df["Major"].tolist()
medianEarnings = df["Median"].tolist()

# Page configuration
st.set_page_config(page_title="College Major Helper")
st.title("College Major Helper")

# Header
st.header("Are you cooked?")

# Input field
major = st.text_input("Enter a major:")

# Quick Info section
st.subheader("Quick Info:")

# Function to show median earnings
def show_median_earnings():
    if major in majors:
        for x in range(len(majors)):
            if majors[x] == major:
                median = medianEarnings[x]
        st.info(f"The median earnings of an employed {major} graduate is ${median} annually.")
    else:
        st.error(f"{major} is not a major in the dataset")

# Three buttons with the same functionality as in your original code
if st.button("See Median Earnings"):
    show_median_earnings()

if st.button("See the Rank of Each Major by Median Earnings"):
    # This button exists in the original but has no functionality
    pass

if st.button("See Unemployment Rate"):
    # This button exists in the original but has no functionality
    pass