
import pandas as pd 
import collections
import pprint
SAW = [
['250','16','12','excellent'],
['200','16','8','average'],
['300','32','16','good'],
['275','32','8','good'],
['225','16','16','belowavg'],
]

df = pd.DataFrame(SAW,columns=['Price','Storage','Camera','Looks'])
all_columns = ['Price','Storage','Camera','Looks']

Looks_num = {
	'belowavg':2,
	'average':3,
	'good':4,
	'excellent':5
}
df.Looks = [Looks_num[item] for item in df.Looks] 

df = df.apply(pd.to_numeric)
#
min_price = df['Price'].min()
df['Price'] = min_price / df['Price']
#
df['Storage'] = df['Storage'] / df['Storage'].max()
#
df['Camera'] = df['Camera'] / df['Camera'].max()
#
df['Looks'] = df['Looks'] / df['Looks'].max()
#

print(df)

weightage = 0.25
df[all_columns]*=weightage

print(df)

total = df.sum(axis=1)
print("Total Sumation each Row\n",total)

best_mobile = {}
key = 0 
for x in total:
	best_mobile[key] = round(x,4)
	key+=1

print(best_mobile)
df['Performance Score'] = total
print(df)
from collections import OrderedDict

sorted_dict = collections.OrderedDict(best_mobile)
#print(sorted_dict)

best_mobile = sorted(best_mobile.items(), key=lambda t: t[1], reverse=True)

#print("Performance Score : ",best_mobile)
print("-"*50)
for i,j in best_mobile:
	print("Mobile",i,"\tPerformance Score",j,)
print("-"*50)

########################################
# students@s:~/Desktop$ python3 dmbi1.py 
#       Price  Storage  Camera  Looks
# 0  0.800000      0.5    0.75    1.0
# 1  1.000000      0.5    0.50    0.6
# 2  0.666667      1.0    1.00    0.8
# 3  0.727273      1.0    0.50    0.8
# 4  0.888889      0.5    1.00    0.4
#       Price  Storage  Camera  Looks
# 0  0.200000    0.125  0.1875   0.25
# 1  0.250000    0.125  0.1250   0.15
# 2  0.166667    0.250  0.2500   0.20
# 3  0.181818    0.250  0.1250   0.20
# 4  0.222222    0.125  0.2500   0.10
# Total Sumation each Row
#  0    0.762500
# 1    0.650000
# 2    0.866667
# 3    0.756818
# 4    0.697222
# dtype: float64
# {0: 0.7625, 1: 0.65, 2: 0.8667, 3: 0.7568, 4: 0.6972}
#       Price  Storage  Camera  Looks  Performance Score
# 0  0.200000    0.125  0.1875   0.25           0.762500
# 1  0.250000    0.125  0.1250   0.15           0.650000
# 2  0.166667    0.250  0.2500   0.20           0.866667
# 3  0.181818    0.250  0.1250   0.20           0.756818
# 4  0.222222    0.125  0.2500   0.10           0.697222
# --------------------------------------------------
# Mobile 2 	Performance Score 0.8667
# Mobile 0 	Performance Score 0.7625
# Mobile 3 	Performance Score 0.7568
# Mobile 4 	Performance Score 0.6972
# Mobile 1 	Performance Score 0.65
# --------------------------------------------------
