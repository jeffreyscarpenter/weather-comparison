from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

def init_cassandra_session():
    global session
    cluster = Cluster()
    session = cluster.connect('weather')

class Observation(Model):
    station_id = columns.Text(primary_key=True)
    observation_date columns.Date(primary_key=True)
    observation_time = columns.DateTime(primary_key=True, clustering_order="DESC")
    latitude = columns.Float(static=True) # not in history
    longitude = columns.Float(static=True) # not in history
    elevation_ft = columns.Float(static=True) # not in history
    weather_condition = columns.Text() # not in history
    temp_f = columns.Float() # tempi
    relative_humidity = columns.Float() # hum
    wind_dir = columns.Text() #wdire
    wind_degrees = columns.Float() #wdird
    wind_mph = columns.Float() # wspdi
    pressure_in = columns.Float() #pressurei
    pressure_trend = columns.Text() # not in history
    feelslike_f = columns.Float() # not in history
    visibility_mi = columns.Float() # not in history
    precip_1hr_in = columns.Float() #precip_ratei
    precip_today_in = columns.Float() #precip_totali

    #"tempm":"25.2", "tempi":"77.4","dewptm":"-0.8", "dewpti":"30.5","hum":"18","wspdm":"1.8",
    #"wspdi":"1.1","wgustm":"3.5", "wgusti":"2.2","wdird":"202","wdire":"SSW","pressurem":"916.6", "pressurei":"27.07",
    #"windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999",
    #"precip_ratem":"0.0", "precip_ratei":"0.00","precip_totalm":"0.0", "precip_totali":"0.00",
    #"solarradiation":"","UV":"","softwaretype":"UnderTheWXv1" },


def persist_observation(observation):
    init_cassandra_session()

    result = Observation.create(
        station_id=observation.station_id,



