#! /usr/bin/env python3.6

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pm25_data = pd.read_csv('data/PM2.5/PM2.5_20160911_small.csv')
#pm25_data.head(5)#讀前十筆資料

pm25_temperature_humidity_data_group = pm25_data.groupby(['s_t0','s_h0'])[['s_d0', 's_d1']]
pm25_temperature_humidity_data_mean = pm25_temperature_humidity_data_group.mean()
group_keys = pm25_temperature_humidity_data_group.groups.keys()

temp = []
hum = []
for items in group_keys :
    (temp_val, hum_val) = items
    temp.append(temp_val)
    hum.append(hum_val)

plt.figure(1)
threedee = plt.figure().gca(projection='3d')
threedee.scatter(temp, hum, pm25_temperature_humidity_data_mean['s_d0'])

threedee.set_xlabel('s_t0')
threedee.set_ylabel('s_h0')
threedee.set_zlabel('s_d0')
plt.show()

#pm25_temperature_humidity_data['s_d0']
print(pm25_temperature_humidity_data_mean['s_d0'])

plt.figure(2)
threedee = plt.figure().gca(projection='3d')
threedee.scatter(temp, hum, pm25_temperature_humidity_data_mean['s_d1'], c = 'b')

threedee.set_xlabel('s_t0')
threedee.set_ylabel('s_h0')
threedee.set_zlabel('s_d1')
plt.show()
print(pm25_temperature_humidity_data_mean['s_d1'])

