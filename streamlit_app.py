import requests
import streamlit as st

# ----Web/Tab config
st.set_page_config(page_title="WeatherApp", page_icon=":sun_behind_rain_cloud:", layout="wide")

# ----API Call/Config
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c8efac34cc3548754ca009222d24da49'.format(city)

res = requests.get(url)
data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
humidity = data['main']['humidity']
description = data['weather'][0]['description']

# ----WEB HEADER SECTION 1
st.title("The Minimalist Weather App")
city = st.text_input("Enter your city : ")

# ----WEB HEADER SECTION 2
st.note('Temperature: {}  degree celsius'.format(temp))
st.note('wind_speed: {}  m/s' .format(wind_speed))
st.note('Humidity: {} %' .format(humidity))
st.note('Clouds:', description)

if temp >= 149:
  st.write("You should wear a coat.")
else:
  st.write("It is safe to wear shorts.")

