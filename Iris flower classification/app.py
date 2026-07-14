import streamlit as st
import pandas as pd
import pickle
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("iris_model.pkl", "rb"))

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("IRIS.csv")

# -----------------------------
# Title
# -----------------------------
st.title("🌸 Iris Flower Classification")
st.markdown("### DecodeLabs AI Internship - Project 2")

st.markdown("---")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Enter Flower Details")

sepal_length = st.sidebar.slider(
    "Sepal Length (cm)",
    float(df.iloc[:,0].min()),
    float(df.iloc[:,0].max()),
    float(df.iloc[:,0].mean())
)

sepal_width = st.sidebar.slider(
    "Sepal Width (cm)",
    float(df.iloc[:,1].min()),
    float(df.iloc[:,1].max()),
    float(df.iloc[:,1].mean())
)

petal_length = st.sidebar.slider(
    "Petal Length (cm)",
    float(df.iloc[:,2].min()),
    float(df.iloc[:,2].max()),
    float(df.iloc[:,2].mean())
)

petal_width = st.sidebar.slider(
    "Petal Width (cm)",
    float(df.iloc[:,3].min()),
    float(df.iloc[:,3].max()),
    float(df.iloc[:,3].mean())
)

# -----------------------------
# Input Data
# -----------------------------
input_data = np.array([[

    sepal_length,
    sepal_width,
    petal_length,
    petal_width

]])

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(input_data)

probability = model.predict_proba(input_data)

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

    st.subheader("📊 Dataset Shape")

    st.write(df.shape)

    st.subheader("📋 Dataset Columns")

    st.write(df.columns)

with col2:

    st.subheader("🌼 Flower Measurements")

    st.write(f"Sepal Length : {sepal_length}")

    st.write(f"Sepal Width : {sepal_width}")

    st.write(f"Petal Length : {petal_length}")

    st.write(f"Petal Width : {petal_width}")

# -----------------------------
# Prediction Button
# -----------------------------
st.markdown("---")

if st.button("🔍 Predict Flower"):

    st.success("Prediction Completed Successfully")

    st.markdown("## 🌸 Prediction Result")

    st.info(prediction[0])

    st.markdown("## 📈 Prediction Probability")

    prob_df = pd.DataFrame({

        "Class": model.classes_,
        "Probability": probability[0]

    })

    st.dataframe(prob_df)

# -----------------------------
# Feature Information
# -----------------------------
st.markdown("---")

st.subheader("📖 Feature Description")

st.write("""
**Sepal Length** → Length of Sepal

**Sepal Width** → Width of Sepal

**Petal Length** → Length of Petal

**Petal Width** → Width of Petal
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
"""
<center>

Developed by ❤️ Ganesh Kumar

DecodeLabs AI Internship Project

</center>
""",
unsafe_allow_html=True
)