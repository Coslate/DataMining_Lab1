#! /usr/bin/env python3.6

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pm25_data = pd.read_csv('data/PM2.5/PM2.5_20160911_small.csv')
#pm25_data.head(5)#讀前十筆資料


pm25_lon_lat_data_group = pm25_data.groupby(['gps_lon','gps_lat'])[['s_d0', 's_d1']]
pm25_lon_lat_data_mean = pm25_lon_lat_data_group.mean()
group_keys = pm25_lon_lat_data_group.groups.keys()

lon = []
lan = []
for items in group_keys :
    (lon_val, lat_val) = items
    lon.append(lon_val)
    lan.append(lat_val)

#print(lon)
#print(lan)

plt.figure(1)
threedee = plt.figure().gca(projection='3d')
threedee.scatter(lon, lan, pm25_lon_lat_data_mean['s_d0'])

threedee.set_xlabel('gps_lon')
threedee.set_ylabel('gps_lat')
threedee.set_zlabel('s_d0')
plt.show()

#pm25_temperature_humidity_data['s_d0']
#print(pm25_lon_lat_data_group.count())
print(pm25_data.groupby(['gps_lon','gps_lat'])[['s_d0', 's_d1']].count())
#print(pm25_lon_lat_data_mean['s_d0'])

plt.figure(2)
threedee = plt.figure().gca(projection='3d')
threedee.scatter(lon, lan, pm25_lon_lat_data_mean['s_d1'], c = 'b')

threedee.set_xlabel('gps_lon')
threedee.set_ylabel('gps_lat')
threedee.set_zlabel('s_d1')
plt.show()
#print(pm25_lon_lat_data_mean['s_d1'])

