# this script obtains weather records for the specified station for the date specified


#https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
#https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722
#https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/


import urllib2
from datetime import datetime, timedelta
import yaml
import sys

with open('config.yaml', 'r') as yamlfile:
    config = yaml.load(yamlfile)

wunderground_api_key = config['wUndergroundApiKey']

# Uses WUnderground History API
# https://www.wunderground.com/weather/api/d/docs?d=data/history
# example request: http://api.wunderground.com/api/<KEY>/history_20180511/q/pws:KAZSCOTT351.json
# possible alternative method for local storage at least: http://www.getware.net/faq
# ~/Library/Containers/net.getware.weather/Data/Documents/UnderTheWX


def archive_weather_history(station, history_date):
    url = 'http://api.wunderground.com/api/' + wunderground_api_key + '/history_' + history_date + '/q/pws:' + station + '.json'
    print('Gathering input: ' + url)
    history_response = urllib2.urlopen(url).read()
    filename = 'data/history_' + history_date + '_' + station + '.json'
    f = open(filename, 'w')
    f.write(history_response)
    f.close()

if __name__ == '__main__':
    station = 'KAZSCOTT351'
    start_date = '20171220'
    end_date = '20171221'
    date_to_process = datetime.strptime(start_date, '%Y%m%d')
    end = datetime.strptime(end_date, '%Y%m%d')
    step = timedelta(days=1)

    while date_to_process <= end:
        archive_weather_history(station, date_to_process.strftime('%Y%m%d'))
        date_to_process += step




