# script to join the weather data and the taxi fare data

import pandas as pd

weather = pd.read_csv('centralParkWeather.csv')
taxi = pd.read_csv('train.csv')

# convert the timestamps in the taxi df to a date to merge with the weather df

def date(timestamp):
    return timestamp.split()[0]

taxi['DATE'] = taxi.apply(lambda x: date(x['key']), axis=1)

df_join = pd.merge(taxi, weather, how='left', on=None)