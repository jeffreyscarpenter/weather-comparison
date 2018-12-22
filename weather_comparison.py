# this script obtains the current weather from two specified weather stations and compares them
# Uses WUnderground History API
# https://www.wunderground.com/weather/api/d/docs?d=data/history

import sys
import urllib2
import json
import dateutil.parser
import yaml


# https://docs.datastax.com/en/developer/python-driver/3.10/getting_started/


with open("config.yaml", 'r') as yamlfile:
    config = yaml.load(yamlfile)

wunderground_api_key = config['wUndergroundApiKey']


# init_cassandra_session()

def get_current_weather(station,do_persist):
    url = "http://api.wunderground.com/api/" + wunderground_api_key + "/conditions/q/pws:" + station + ".json"
    myWeather = urllib2.urlopen(url).read()
    myWeatherDict = json.loads(myWeather)
    myCurrentObservation = myWeatherDict["current_observation"]
    myCurrentTemp = myCurrentObservation["temp_f"]
    # myCurrentDatetime = datetime.fromtimestamp(float(myCurrentObservation["observation_epoch"]))
    myCurrentDatetime = dateutil.parser.parse(myCurrentObservation["observation_time_rfc822"])
    print "Current temperature at " + station + " is: " + str(myCurrentTemp) + " on: " + str(myCurrentDatetime)
    if do_persist:
        session.execute(
            """
        INSERT INTO weather_observation (
            station_id,
            observation_date, // conversion required from observation_epoch, use for bucketing
            observation_time, // conversion required from observation_epoch
            temp_f
        )
        VALUES (%s, %s, %s, %s)
        """,
            (
                myCurrentObservation["station_id"],
                myCurrentDatetime.date(),
                myCurrentDatetime,
                myCurrentTemp
            )
        )
    return myCurrentTemp


# python weather_comparison.py KAZSCOTT351 KAZSCOTT243
temp1 = get_current_weather(sys.argv[1],False)
temp2 = get_current_weather(sys.argv[2],False)

delta = temp2 - temp1
print "Difference : " + str(delta)

#         latitude,
#         longitude,
#         elevation_ft, // conversion required
#         weather_condition, // "weather" in API
#         temp_f,
#         relative_humidity, // conversion required
#         wind_dir,
#         wind_degrees,
#         wind_mph,
#         pressure_in,
#         pressure_trend,
#         feelslike_f,
#         visibility_mi,
#         precip_1hr_in,
#         precip_today_in,
