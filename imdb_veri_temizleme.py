# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:59:36 2020

@author: deniz
"""

import pandas as pd
import numpy as np

movies=pd.read_csv('IMDB.csv')

year=movies.year
year=year.str.replace('(','')
year=year.str.replace('I','')
year=year.str.replace(')','')
year=pd.to_numeric(year)
runtime=movies.runtime
runtime=runtime.str.replace(' min','')
runtime=pd.to_numeric(runtime)
movies['runtime']=runtime
movies['year']=year
movies.drop(columns=['Unnamed: 0','place'],inplace=True)

movies.to_csv('IMDB_clean_data.csv')