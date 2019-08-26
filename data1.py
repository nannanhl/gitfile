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


results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])
cframe = frame[frame.a.notnull()]
cframe['a']

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts=by_tz_os.size().unstack().fillna(0)
agg_counts[:10]

indexer=agg_counts.sum(1).argsort()
count_subset=agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind='barh',stacked=True)
count_subset.plot(kind='barh',stacked=False)


normed_subset=count_subset.div(count_subset.sum(1),axis=0)  
normed_subset.plot(kind='barh',stacked=True)












