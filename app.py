import streamlit as st
import pandas as pd
import numpy as np
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

date = st.date_input(
    "write the today's date",
    value = None)
st.write('Today is:', date)

time = st.time_input(
    'what time is it?',
    value = None)
st.write("It's:", time)

date_time = datetime.datetime.combine(date, time)

latitude= st.number_input('Enter a latitude:', format='%0.6f')
longitude= st.number_input('Enter a longitude:', format='%0.6f')
latitude_dropoff= st.number_input('Enter a latitude drop off:', format='%0.6f')
longitude_dropoff= st.number_input('Enter a longitude drop off:', format='%0.6f')
passenger_count = st.number_input('How many passenger:', key='pass_count', min_value = int(0))

params_ = {
    'pickup_datetime' : date_time,
    'pickup_latitude' :latitude,
    'pickup_longitude' : longitude,
    'dropoff_latitude' : latitude_dropoff,
    'dropoff_longitude' : longitude_dropoff,
    'passenger_count': passenger_count
    }


url_ = 'https://taxifare.lewagon.ai/predict'
response = requests.get(url = url_, params = params_)
fare_amount = response.json()['fare']*passenger_count* -1

map_df = pd.DataFrame({
    'latitude': [latitude, latitude_dropoff],
    'longitude': [longitude, longitude_dropoff]
})
st.map(map_df, size=12)

if st.button('Click me to get the fare'):
    st.write("You'll pay:", f'{fare_amount}', format='%0.2f')




'''
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
