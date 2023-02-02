import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import datetime as dtt

from functions import coordinates, documentation_cloud_cover, documentation_ppt_amt, documentation_weather_type, documentation_wind_spd_10m, wiki_timezone

def main():
    
    #user_city = input()
    
    lat, long = coordinates("Kelowna")
    
    url ="http://www.7timer.info/bin/api.pl?lon={long}&lat={lat}&product=civil&output=json".format(long=long,lat=lat)
    course_requests = requests.get(url)

    course = BeautifulSoup(course_requests.text, features="lxml")
    course

    data = json.loads(course.text)
    flag = (data["dataseries"])

    # initialize time

    ml_ini = data["init"]
    dt = datetime.strptime(ml_ini, '%Y%m%d%H')
    ml_hr = dt.hour
    time_zone = wiki_timezone("Kelowna") ## user input
    act_hr = ml_hr+time_zone+3

    # loop

    given_date = dtt.datetime(dt.year, dt.month, dt.day, act_hr)
    ch =[]
    for i in range(64):
        try:
            interval = dtt.timedelta(hours=3)
            new_date = given_date + interval * i
            ch.append(new_date.strftime("%Y-%m-%d %H:%M"))
        except:
            print("Improper format of the mentioned date")

    civil =pd.DataFrame(flag)
    civil1 = pd.json_normalize(civil["wind10m"])
    civil = pd.concat([civil1, civil.drop("wind10m",axis=1)],axis=1)

    # timedate_columns
    civil["datetime"]= pd.DataFrame(ch)

    civil[["Date", "Time(24 hrs)"]] = civil.datetime.str.split(" ", expand=True)
    civil.drop("datetime", axis=1, inplace=True)
    civil.drop("timepoint", axis=1, inplace=True)

    cloudupdate = documentation_cloud_cover(civil)

    ppt_amt = documentation_ppt_amt(cloudupdate)

    wind_speed = documentation_wind_spd_10m(ppt_amt)

    weather_type = documentation_weather_type(wind_speed)

    return weather_type