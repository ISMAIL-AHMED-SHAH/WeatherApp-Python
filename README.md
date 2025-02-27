# Real-Time Weather App 🌤️

## Live Demo 🚀
Check out the deployed app here: [IQ Weather App](https://iq-weather-app.streamlit.app/)

## Overview
The **Real-Time Weather App** is a simple and elegant web application built with **Streamlit** and the **OpenWeather API**. It allows users to fetch real-time weather information for any city worldwide, displaying key weather metrics such as temperature, humidity, wind speed, and conditions with an intuitive UI.

## Features ✨
- 🌎 **Real-time Weather Data**: Fetch live weather details for any city.
- 📊 **Key Weather Metrics**: Displays temperature, humidity, wind speed, and weather conditions.
- 🌤️ **Weather Icons**: Dynamically loads weather condition icons.
- 🔄 **Auto-Refresh Feature**: Refreshes data every 5 minutes for up-to-date weather information.
- 🎨 **Beautiful UI**: Gradient styling and a clean layout for better user experience.
- 🖥️ **Responsive Design**: Works across different devices and screen sizes.

## Technologies Used 🛠️
- **Python** 🐍
- **Streamlit** 🎈
- **OpenWeather API** 🌍
- **Requests (HTTP Requests Library)** 🔗
- **Datetime** ⏳

## Installation & Setup 🏗️
To run the project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/weather-app.git
   cd weather-app
   ```
2. Install dependencies:
   ```sh
   pip install streamlit requests
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## API Configuration 🌍
This app uses the **OpenWeather API** to fetch weather data. Replace `API_KEY` in the script with your own OpenWeather API key:
```python
API_KEY = "your_openweather_api_key"
```

## Usage 🏙️
1. Enter the name of the city in the input field.
2. Click the "Refresh Data" button to update the weather details.
3. View temperature, humidity, wind speed, and weather conditions.
4. The data automatically refreshes every 5 minutes.

## Author ✍️
👨‍💻 **Ismail Ahmed Shah**  
Built with ❤️ and passion for learning!

## License 📜
This project is licensed under the MIT License.

