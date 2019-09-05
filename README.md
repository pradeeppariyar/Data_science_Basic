# Data_science_Basic
Basic Data science
Data Frame 

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

d = {'Quarters' : ['Quarter1','Quarter2','Quarter3','Quarter4'],
     'Revenue':[23400344.567,54363744.678,56789117.456,4132454.987]}
df=pd.DataFrame(d)
print(df)

pd.options.display.float_format = '{:.1f}'.format
print(df)

pd.options.display.float_format = '${:,.2f}'.format
print(df)

# Format with Scientific notation
pd.options.display.float_format = '{:.2E}'.format
print(df)

#Create a Dictionary of series
d = {'Name':pd.Series(['Raja','pradeep','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Siva','David','Daniel','akshay','Suraj']),
   'Age':pd.Series([26,27,25,24,31,27,25,33,42,32,51,47]),
   'Score':pd.Series([89,87,67,55,47,72,76,79,44,92,99,69])}
 
#Create a DataFrame
df = pd.DataFrame(d)
print (df)

print(df.describe())
