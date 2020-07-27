# script to join the weather data and the taxi fare data and clean some of it up

import pandas as pd
from sklearn.metrics.pairwise import haversine_distances
from datetime import datetime

weather = pd.read_csv('centralParkWeather.csv')
taxi = pd.read_csv('train.csv', nrows = 1_000_000)

# convert the timestamps in the taxi df to a date to merge with the weather df

def date(timestamp):
    return timestamp.split()[0]

taxi['DATE'] = taxi.apply(lambda x: date(x['key']), axis=1)

df = pd.merge(taxi, weather, how='left', on=None)

# add a new feature, hav_distance that will calculate distance between points
def hav_distance(lon1, lat1, lon2, lat2):
    # use sklearn's haversine function and multiply by Earth's radius to get distance in km
    return haversine_distances([[lon1, lat1], [lon2, lat2]])[0][1] * 6371000/1000

# create new feature using this function, distance in km
df['distance_traveled_km'] = df.apply(lambda x: hav_distance(x['pickup_longitude'], x['pickup_latitude'], x['dropoff_longitude'], x['dropoff_latitude']), axis=1)


def day_of_week(date):
    return datetime.strptime(date, '%Y-%m-%d').weekday()

# create a feature for day of the week, 0 - Monday, 1 - Tuesday, etc. 
df['week_day'] = df.apply(lambda x: day_of_week(x['DATE']), axis=1)


# drop some useless features
drop_elements = ['key', 'STATION', 'NAME']
df = df.drop(drop_elements, axis = 1)

#df.to_csv('taxi_weather.csv', index=False)

df.to_csv('taxi_weather.gz', index=False, compression='gzip')
