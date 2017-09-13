# -*- coding:utf-8 -*-
import os
import pandas as pd
import numpy as np 

#path = 'C:\\Users\\Administrator\\data\\'
path = 'D:/test/'
filenames = os.listdir(path)
print filenames

dataframes = []
for file in filenames:
    print file
    dataframes.append(pd.read_csv(path + file, header = None))
alldata = pd.concat(dataframes, ignore_index = True)
  
# print((alldata.max()).max())
td = np.transpose(alldata)  # 转置
tdn = td.max()  # 求每一行最大值

dictionary = dict(zip(filenames, tdn)) # 组成字典
dictionary

strmax = max(dictionary.items(), key=lambda x: x[1])
print strmax