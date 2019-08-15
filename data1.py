# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 23:15:53 2019

@author: admin
"""
#《利用python进行数据分析》
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import json
#8-15-2019修改
path = 'b:/python3/Data/example.txt'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
frame