import sys
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

print(sys.argv)

wind_data = pd.read_csv(sys.argv[1]);

#wind_data.info()
#print(wind_data[['time', 'h5_humidity_mean']])
#plt.figure()
#wind_data.plot(x='time', y=['a20_wind_speed_min', 'a20_wind_speed_mean', 'a20_wind_speed_max'], kind='line', linewidth=0.05)
#plt.show()

print(type(wind_data.index));
#wind_data.index = pd.to_datetime(wind_data.index, format='%Y-%m-%d %H:%M', exact=True)
wind_data.index = wind_data['time'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M'))
#print(wind_data)
#print(wind_data.index)
print(type(wind_data.index[1]))
#print(wind_data.index)
daily = wind_data.resample('D').mean()

daily.info()

plt.figure()
daily.plot( y=['a20_wind_speed_mean', 'a40_wind_speed_mean', 'a60_wind_speed_mean', 'a80T_wind_speed_mean'], kind='line', linewidth=0.5)
plt.show()
