CREATE KEYSPACE IF NOT EXISTS weather
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

CREATE TABLE IF NOT EXISTS weather.weather_observation (
    station_id text,
    observation_date date, // conversion required from observation_epoch, use for bucketing
    observation_time timestamp, // conversion required from observation_epoch
    latitude float static,
    longitude float static,
    elevation_ft uuid static, // conversion required
    weather_condition text, // "weather" in API
    temp_f float,
    relative_humidity float, // conversion required
    wind_dir text,
    wind_degrees float,
    wind_mph float,
    pressure_in float,
    pressure_trend text,
    feelslike_f float,
    visibility_mi float,
    precip_1hr_in float,
    precip_today_in float,
    PRIMARY KEY ((station_id, observation_date), observation_time)
);

		"latitude":"33.70", // SAVE
		"longitude":"-111.82", // SAVE
		"elevation":"2654 ft" // SAVE
		"station_id":"KAZSCOTT351",  // SAVE
		"observation_epoch":"1527128930",  // SAVE
		"weather":"Clear", // SAVE
		"temp_f":81.5, // SAVE
		"relative_humidity":"17%", // SAVE
		"wind_dir":"WSW", // SAVE
		"wind_degrees":247, // SAVE
		"wind_mph":1.4, // SAVE
		"pressure_in":"29.78", // SAVE
		"pressure_trend":"+", // SAVE
		"feelslike_f":"81.5", // SAVE
		"visibility_mi":"10.0", // SAVE
		"precip_1hr_in":"0.00", // SAVE
		"precip_today_in":"0.00", // SAVE
