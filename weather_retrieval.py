# this script obtains weather records for the specified station for the date specified

import sys
import urllib2
import json
import dateutil.parser
from cassandra.cluster import Cluster
import yaml

# https://docs.datastax.com/en/developer/python-driver/3.10/getting_started/

def init_cassandra_session():
    global session
    cluster = Cluster()
    session = cluster.connect('weather')

with open("config.yaml", 'r') as yamlfile:
    config = yaml.load(yamlfile)

wunderground_api_key = config['wUndergroundApiKey']

#init_cassandra_session()

# Uses WUnderground History API
# https://www.wunderground.com/weather/api/d/docs?d=data/history
# example request: http://api.wunderground.com/api/<KEY>/history_20180511/q/pws:KAZSCOTT351.json
# possible alternative method for local storage at least: http://www.getware.net/faq
# ~/Library/Containers/net.getware.weather/Data/Documents/UnderTheWX


def get_weather_history(station, history_date, do_persist):
    url = "http://api.wunderground.com/api/" + wunderground_api_key + "/history_" + history_date + "/q/pws:" + station + ".json"
    history_response = urllib2.urlopen(url).read()
    history_dict = json.loads(history_response)
    observations = history_dict["history"]["observations"]
    for observation in observations:
        process_observation(station, observation, do_persist)


def process_observation(station, observation, do_persist):
    observation_temp = observation["tempi"]
    observation_date = dateutil.parser.parse(observation["date"]["pretty"] )
    print "Temperature at " + station + " on: " + str(observation_date) + " was: " + str(observation_temp)
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
            station,
            observation_date.date(),
            observation_date,
            observation_temp
        )
      )


# python weather_retrieval.py KAZSCOTT351
get_weather_history(sys.argv[1], sys.argv[2], False)


