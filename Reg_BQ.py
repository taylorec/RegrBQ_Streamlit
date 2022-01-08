# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:49:35 2021

@author: evan
"""

import streamlit as st
import joblib

st.title('Prediction of Trip Duration in Minutes')
st.write("This application predicts the duration of a bike trip. Original data comes from Google BigQuery new_york_citibike.citibike_trips database.")
 
loaded_GBr = joblib.load('GBr.joblib')

start_station_id = st.number_input('Start station ID', min_value=1)
end_station_id = st.number_input('End station ID', min_value=1)
usertype = st.selectbox('User type', options=['Customer', 'Subscriber'])
birth_year = st.number_input('Birth year', min_value=1920)
gender = st.selectbox('Gender', options=['Male', 'Female', 'Unknown'])
hour = st.selectbox('Closest hour of trip start', ['12am', '1am', '2am', '3am',
                                                    '4am', '5am', '6am', '7am',
                                                    '8am', '9am', '10am', '11am',
                                                    '12pm', '1pm', '2pm', '3pm',
                                                    '4pm', '5pm', '6pm', '7pm',
                                                    '8pm', '9pm', '10pm', '11pm'])
month = st.selectbox('Month of trip', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
                                        'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
day = st.selectbox('Day of trip', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

if usertype == 'Customer':
    usertype = 0
elif usertype == 'Subscriber':
    usertype = 1

if gender == 'Male':
    gender = 0
elif gender == 'Female':
    gender = 1
elif gender == 'Unknown':
    gender = 2

if hour == '12am':
    hour = 0
elif hour == '1am':
    hour = 1
elif hour == '2am':
    hour = 2
elif hour == '3am':
    hour = 3
elif hour == '4am':
    hour = 4
elif hour == '5am':
    hour = 5
elif hour == '6am':
    hour = 6
elif hour == '7am':
    hour = 7    
elif hour == '8am':
    hour = 8
elif hour == '9am':
    hour = 9
elif hour == '10am':
    hour = 10
elif hour == '11am':
    hour = 11
elif hour == '12pm':
    hour = 12
elif hour == '1pm':
    hour = 13
elif hour == '2pm':
    hour = 14
elif hour == '3pm':
    hour = 15
elif hour == '4pm':
    hour = 16
elif hour == '5pm':
    hour = 17
elif hour == '6pm':
    hour = 18
elif hour == '7pm':
    hour = 19
elif hour == '8pm':
    hour = 20
elif hour == '9pm':
    hour = 21
elif hour == '10pm':
    hour = 22
elif hour == '11pm':
    hour = 23

if month == 'Jan':
    month = 1
if month == 'Feb':
    month = 2
if month == 'Mar':
    month = 3
if month == 'Apr':
    month = 4
if month == 'May':
    month = 5
if month == 'June':
    month = 6
if month == 'July':
    month = 7
if month == 'Aug':
    month = 8
if month == 'Sep':
    month = 9
if month == 'Oct':
    month = 10
if month == 'Nov':
    month = 11
if month == 'Dec':
    month = 12

if day == 'Mon':
    day = 0
if day == 'Tue':
    day = 1
if day == 'Wed':
    day = 2
if day == 'Thu':
    day = 3
if day == 'Fri':
    day = 4
if day == 'Sat':
    day = 5
if day == 'Sun':
    day = 6

prediction = loaded_GBr.predict([[start_station_id, end_station_id, usertype,
                                      birth_year, gender, hour, month,day]])
st.write('The predicted trip duration in minutes is: {}'.format(prediction))

       
