#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:57:50 2019

@author: pradeep
"""

import pandas as pd
import numpy as np

d= pd.MultiIndex.from_product([['semester1','semester2'],['Math','Science']])
d=([[12,34,40,38] ,[50,56,54,60] ,[60 ,65,63 ,67],[70,74,78,80]])

df = pd.DataFrame(d ,
                  index=['Alisha' ,'Lina' ,'Bobby' ,'Pradeep'], 
                  columns=header)
df

# Stack() Function in dataframe stacks the column to rows at level 1 (default).
stack_df=df.stack()
stack_df

# unstack the datagram
unstacked_df = stack_df.unstack()
unstacked_df

unstack_df =stack_df.unstack()
unstack_df

stacked_df_lvl=df.stack(level=1)
stacked_df_lvl

#Create Pivot table in Pandas python

import pandas as pd
import numpy as np
 
#Create a DataFrame
d = {
    'Name':['Pradeep','Raja','Akshay','Pradeep','Raja','Akshay',
            'Pradeep','Raja','Akshay','Pradeep','Raja','Akshay'],
    'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
            'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
     
    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
 
df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

pd.pivot_table(df ,index=['Exam' ,'Subject'], aggfunc='sum' )



