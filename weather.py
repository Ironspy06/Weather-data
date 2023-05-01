import requests
import streamlit as st
import plotly.graph_objects as go

st.title("Weather App")

city = st.text_input("Enter city name")

unit = st.radio("Select temperature unit:", ("Celsius", "Fahrenheit"))


url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {
    'appid': 'adbcdb7af4fd87ed1fa4ad02986cf2a1',
    'q': city,
    'units': 'metric' if unit == "Celsius" else "imperial",
    'cnt': 5 * 8 
}

# Make API request
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if 'list' in data:

        temp_data = []
        feels_like_data = []
        date_data = []

        
        for item in data['list']:
            temp_data.append(item['main']['temp'])
            feels_like_data.append(item['main']['feels_like'])
            date_data.append(item['dt_txt'])


        st.write(f"Weather in {data['city']['name']}:")
        if unit == "Celsius":
            st.write(f"Temperature Unit: Celsius")
        else:
            st.write(f"Temperature Unit: Fahrenheit")

        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=date_data, y=temp_data, name='Temperature'))
        fig.add_trace(go.Scatter(x=date_data, y=feels_like_data, name='Feels-like Temperature'))
        fig.update_layout(title='Temperature and Feels-like Temperature for the Last 5 Days', xaxis_title='Date', yaxis_title='Temperature')
        st.plotly_chart(fig)

    else:
        st.write("Sorry, could not retrieve weather data for the specified location.")
else:
    st.write("Sorry, could not retrieve weather data. Please try again later.")
