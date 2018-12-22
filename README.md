Notes

https://www.wunderground.com/weather/api/d/docs

http://dark5un.github.io/blog/2017/02/18/wip-cassandra-query-language-cql-intellij-idea-plugin/

https://apicommunity.wunderground.com/weatherapi/topics/weather-underground-api-changes
https://www.aerisweather.com/
https://www.pwsweather.com/faqs.php
https://www.pwsweather.com/


Get the python driver
https://docs.datastax.com/en/developer/python-driver/3.14/installation/


Weather station reports from history service are timed based on reporting station. Interval seems to be around 6 minutes
would like to have the closest temperature report in time that matches a regular interval. Closest but not after?
examine one record at a time, placing its value to the nearest interval we care about - this normalizes across stations
we could attempt to do some interpolation, this would require more sophistication which would possibly be bettern
based on time of previous report, current report and difference between times?
could we do curve fitting
streaming values?
