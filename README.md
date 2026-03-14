# 📦 🎈 My First Streamlit App (Streamlit Crash Course)

Welcome to the **Streamlit Crash Course**! In this course, you'll learn how to create interactive web applications using Streamlit. Streamlit is a powerful and easy-to-use framework that allows you to build data-driven applications with minimal code.

---

## Course Outline

1. Introduction to Streamlit  
2. Setting up your environment  
3. Creating your first Streamlit app  
4. Adding interactivity with widgets  
5. Displaying data and visualizations  

---

## Introduction to Streamlit

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. With Streamlit, you can turn your Python scripts into interactive web applications in just a few lines of code.

---

## Setting up your environment

To get started with Streamlit, install the required packages:

```bash
pip install streamlit matplotlib pandas watchdog
```
---

## Features

- Display a sample DataFrame  
- Filter data interactively using a slider  
- Visualize data with a Matplotlib bar chart  

---

## Running the App

Create a Python file (e.g., `streamlit_app.py`) and add your code.  
Then run the app in your terminal:

```bash
streamlit run streamlit_app.py
```

## Example Usage

Here’s a minimal example showing the main functionality:
```
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("My First Streamlit App")
```

### Sample DataFrame
```
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.dataframe(df)
```
### Slider to filter by age
```
age_filter = st.slider("Select age range", 0, 100, (20, 40))
filtered_df = df[(df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1])]
st.dataframe(filtered_df)
```
### Simple bar chart
```
plt.bar(filtered_df['Name'], filtered_df['Age'])
st.pyplot(plt)
```

## Resources

Streamlit Documentation (https://docs.streamlit.io/)

Streamlit GitHub Repository (https://github.com/streamlit/streamlit)
