from datetime import datetime

date = '2009-01-05'

df = '1'

# 0 - Monday, 1 - Tuesday, etc. 

def day_of_week(date):
    return datetime.strptime(date, '%Y-%m-%d').weekday()

df[''] = df.apply(lambda x: day_of_week(x['pickup_datetime']), axis=1)

print(day_of_week(date))