#! /usr/bin/env python3.6

import sys

print(sys.version_info)
# major=3, minor=5, micro=2 means version 3.5.2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

na = np.array(a)
nb = np.array(b)

print ('na*nb: ', na*nb)

print ('mean: ', np.mean(a))
print ('std: ', np.std(a))



df = pd.DataFrame([['Paul', 'M', 18], ['Jean', 'F', 33], ['Tom', 'M', 35], ['Tony', 'M', 33], ['Amy', 'F', 21], ['Lisa', 'F', 20]])
df.columns=['Name', 'Gender', 'Age']
print(df)


x1 = np.random.uniform(0,1,size=10)
x2 = np.random.uniform(0,1,size=10)
print ('x1', x1)
print ('x2', x2)

plt.plot(x1)
plt.plot(x2)
plt.show()

print(mean_squared_error([1,2,3], [2,4,6]))
