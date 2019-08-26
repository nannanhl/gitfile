# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 23:15:53 2019

@author: admin
"""
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import json
path = 'b:/python3/Data/example.txt'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
tz_counts = frame['tz'].value_counts() 
#tz_counts[:10]
clean_tz = frame['tz'].fillna('missing')
clean_tz[clean_tz == '' ] = 'unknow'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

import matplotlib.pyplot as plt
tz_counts[:10].plot(kind = 'barh', rot = 0)
"""
frame['a'][1]
frame['a'][50]
frame['a'][51]
"""

results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])



