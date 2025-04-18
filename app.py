import streamlit as st
import requests
from datetime import datetime
import time

# Configure the app
st.set_page_config(
    page_title="Real-Time Weather App",
    page_icon="🌤️",
    layout="centered"
)

# Add gradient background (optional)
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #E0F6FF, #FFFFFF);
    }
    </style>
""", unsafe_allow_html=True)

# Gradient title
st.markdown("""
    <h1 style="background: linear-gradient(to right, #4ECDC4, #45B7D1, #96CEB4); 
               -webkit-background-clip: text; 
               color: transparent; 
               text-align: center;">
                Weather App
    </h1>
""", unsafe_allow_html=True)



# Constants
API_KEY = "314305dfb21d06325abea643a991f2eb"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather_data(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # For Celsius
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    except requests.RequestException as e:
        return None

# UI Elements
st.subheader("🌤️ Real-Time Weather Forecast App")
st.write("Get current weather information for any city!")

# City input
city = st.text_input("Enter City Name", "London")

# Add a placeholder for weather info
weather_placeholder = st.empty()

# Main app logic
def update_weather():
    if city:
        weather_data = get_weather_data(city)
        
        if weather_data is None:
            weather_placeholder.error("Error fetching weather data. Please try again.")
            return
        
        if weather_data.get("cod") != 200:
            weather_placeholder.error(f"Error: {weather_data.get('message', 'City not found')}")
            return
        
        # Extract weather information
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]
        icon_code = weather_data["weather"][0]["icon"]
        
        # Create columns for layout
        col1, col2 = weather_placeholder.columns(2)
        
        # Display weather information
        with col1:
            st.metric("Temperature", f"{temp:.1f}°C")
            st.metric("Humidity", f"{humidity}%")
        
        with col2:
            st.metric("Wind Speed", f"{wind_speed} m/s")
            st.image(f"http://openweathermap.org/img/wn/{icon_code}@2x.png", width=100)
            st.write(f"**Condition:** {description.capitalize()}")
        
        # Display last updated time
        st.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Auto-refresh logic
if st.button("Refresh Data") or 'last_refresh' not in st.session_state:
    update_weather()
    st.session_state.last_refresh = time.time()

# Auto-refresh every 5 minutes
if 'last_refresh' in st.session_state:
    if time.time() - st.session_state.last_refresh >= 300:  # 300 seconds = 5 minutes
        update_weather()
        st.session_state.last_refresh = time.time()

# Footer
st.markdown("---")
st.write("👨‍💻 Build with ❤️ by **Ismail Ahmed Shah**")



st.sidebar.image("weather.png", use_container_width=True)
st.sidebar.markdown("---")
# 📬 Contact Section
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
st.sidebar.markdown("---")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png", width=90, use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Build with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")