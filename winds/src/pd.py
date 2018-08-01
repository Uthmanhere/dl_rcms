import sys
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


wind_data = pd.read_csv(sys.argv[1]);

wind_data.index = wind_data['time'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M'))
daily = wind_data.resample('D').mean()
print(daily.info)
daily_month = wind_data.resample('m').mean()
print(daily_month)

#daily.sort_values( by='t5_temperature_mean' )
#print(daily['t5_temperature_mean'])
plt.figure()
daily.plot(y='a20_wind_speed_mean', kind='line', linewidth=0.5)
plt.show()
plt.figure()
daily_month.plot(y='a20_wind_speed_mean', kind='line', linewidth=0.5)
plt.show()
