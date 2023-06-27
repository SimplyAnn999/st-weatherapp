import requests
import streamlit as st

st.set_page_config(page_title="WeatherApp", page_icon=":sun_behind_rain_cloud:", layout="wide")
city = st.text_input("Enter your city : ")

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c8efac34cc3548754ca009222d24da49'.format(city)

res = requests.get(url)
data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
humidity = data['main']['humidity']
description = data['weather'][0]['description']


# HEADER SECTION
st.title("A Minimalist Weather App")
st.write('Temperature: {}  degree celsius'.format(temp))
st.write('wind_speed: {}  m/s' .format(wind_speed))
st.write('Humidity: {} %' .format(humidity))
st.write('Clouds:', description)


if temp >= 149:
  st.write("You should wear a coat.")
else:
  st.write("It is safe to wear shorts.")
