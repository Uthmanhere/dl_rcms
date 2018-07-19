import sys
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


wind_data = pd.read_csv(sys.argv[1]);


wind_data.index = wind_data['time'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M'))
daily = wind_data.resample('D').mean()

daily.info()

plt.figure()
daily.plot( y=['a20_wind_speed_mean', 'a40_wind_speed_mean', 'a60_wind_speed_mean', 'a80T_wind_speed_mean'], kind='line', linewidth=0.5)
plt.show()
