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

# Constants
API_KEY = "314305dfb21d06325abea643a991f2eb"  # Replace with your OpenWeatherMap API key
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
st.title("🌤️ Real-Time Weather App")
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
st.markdown("Data provided by OpenWeatherMap")