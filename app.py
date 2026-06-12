import streamlit as st
import pickle
import matplotlib.pyplot as plt
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Load Model
model = pickle.load(open('house_model.pkl', 'rb'))

# Title
st.title("🏠 House Price Prediction Dashboard")
st.markdown("### Predict the estimated price of a house")

# Image
st.image(
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200",
    use_container_width=True
)

st.markdown("---")

# Input Section
st.subheader("📋 Enter House Details")

area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=5000,
    value=1500
)

bedrooms = st.slider("🛏 Bedrooms", 1, 10, 3)

bathrooms = st.slider("🚿 Bathrooms", 1, 10, 2)

parking = st.slider("🚗 Parking Spaces", 0, 5, 1)

st.markdown("---")

# Prediction Button
if st.button("🔍 Predict House Price"):

    prediction = model.predict(
        [[area, bedrooms, bathrooms, parking]]
    )

    st.success(
        f"🏡 Estimated House Price: ₹ {prediction[0]:.2f} Lakhs"
    )

    st.balloons()
    import matplotlib.pyplot as plt

st.subheader("Area vs House Price")

area_data = [1000,1200,1500,1800,2000,2200,2500,2800,3000,3500]
price_data = [25,30,40,45,55,60,70,80,90,100]

fig, ax = plt.subplots()

ax.plot(area_data, price_data)

ax.set_xlabel("Area")

ax.set_ylabel("Price")

st.pyplot(fig)