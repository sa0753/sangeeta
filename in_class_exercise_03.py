# -*- coding: utf-8 -*-
"""Copy of Copy of In_class_exercise_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19wsOfx6KOGI1iaRVYTYHHfMxrcnPjZAQ

# **The third in-class-exercise**

We want to extract information about the local weather from the National Weather Service website. Here is the link:

https://forecast.weather.gov/MapClick.php?textField1=33.22&textField2=-97.15#.XaXfI0ZKjb0

**Part one (locate the information we need):**

(1) Download the web page containing the forecast.

(2) Create a BeautifulSoup class to parse the page.

(3) Find the div with id seven-day-forecast, and assign to seven_day

(4) Inside seven_day, find each individual forecast item.

(5) Extract and print the first forecast item.


**Part two (Extracting information from the page):**

As you can see, inside the forecast item tonight is all the information we want. There are 4 pieces of information we can extract:

(1) The name of the forecast item.

(2) The description of the conditions.

(3) A short description of the conditions.

(4) The temperature High.

Write a python program to extract the required information and save it into a csv file with the format showing in the picture.
"""

from IPython.display import Image
Image('https://raw.githubusercontent.com/unt-iialab/INFO5731_Spring2020/master/In_class_exercise/data_output.PNG')

# Write your code here
import urllib.request
from bs4 import BeautifulSoup
weather = "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
page = urllib.request.urlopen(weather)
soup = BeautifulSoup(page)
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)
img = tonight.find("img")
desc = img['title']
print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
['Tonight',
 'Thursday',
 'ThursdayNight',
 'Friday',
 'FridayNight',
 'Saturday',
 'SaturdayNight',
 'Sunday',
 'SundayNight']
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)
import pandas as pd
weather = pd.DataFrame({
        "period": periods,
         "short_desc": short_descs,
         "temp": temps,
         "desc":descs
    })
weather
