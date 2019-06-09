# Fun with weather data
This is just a fun vanity project where I'm messing around with data from my personal weather station.

## First experiment: Neighborhood comparison
The goal is to compare temperature between various neighborhoods in Scottsdale at differing elevations over a one 
year period (2018).

Questions to answer:
- Temperature:
    - what is the average temp difference over various intervals?
    - assuming that there are times when a different location is the warmest, track when the crossover points occur
- Precipitation: 
    - (how can we compare rainfall between locations? - identifying days when one location got rain?)
- Wind
    - TBD
- Data engineering
    - Are there gaps in the data?
    
The raw data: 
- Weather station reports from the WUnderground history service are timed based on reporting station. 
- Typical interval seems to be around 6 minutes
- Would like to have the closest temperature report in time that matches a regular interval. Closest but not after?
Examine one record at a time, placing its value to the nearest interval we care about - this normalizes across stations
we could attempt to do some interpolation, this would require more sophistication which would possibly be bettern
based on time of previous report, current report and difference between times?
could we do curve fitting

Other questions
- streaming updates?


Initial data gathering approach was based on [Weather Underground API][wunderground-api], but since they are 
[discontinuing][wunderground-discontinuation] it as of 12/31/2018, I'm looking for other options

https://www.aerisweather.com/
https://www.pwsweather.com/faqs.php
https://www.pwsweather.com/


Other research:
Time series: https://content.pivotal.io/blog/time-series-analysis-part-3-resampling-and-interpolation

Running weather station software on Raspberry Pi instead of full computer: 
https://github.com/acuparse/acuparse/wiki/Installation-on-Raspberry-Pi


[wunderground-api]: https://www.wunderground.com/weather/api/d/docs
[wunderground-discontinuation]: https://apicommunity.wunderground.com/weatherapi/topics/weather-underground-api-changes


