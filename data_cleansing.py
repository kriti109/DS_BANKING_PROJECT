# -*- coding: utf-8 -*-
"""
Created on Sat May 31 11:51:39 2025

@author: 7430
"""

'Cleaning pre processing the data.'
'importing the libraries'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from loading_dataset import load_dataset



def preprocessing(df):
    unique_counts = df.nunique() #displays the number of unique entries in each column
    print(unique_counts)
    
    #getting rid of redundant columns.
    
    print(df['marital'].value_counts())
    print(df['marital_status'].value_counts()) #same counts, these two are same.
    
    df.drop(columns=['marital'], inplace = True)
    df.drop(columns=['day', 'month'], inplace = True)
    
    
    #taking care of the missing values.
    print(df.isnull().sum()) #displays the total number of missing values in each column.
    # three missing values each in marital_status and education. 
    #dropping the three rows with missing values as our sample set is quite large and wont be affected much
    df.dropna(subset = ['marital_status', 'education'], inplace = True)
    #checking again
    print(df.isnull().sum())
    
    
    
    #converting datatypes to 0 and 1.
    df['y'].replace({'yes':1,'no':0}, inplace=True)
    df['default'].replace({'yes':1,'no':0}, inplace=True)
    df['housing'].replace({'yes':1,'no':0}, inplace=True)
    df['loan'].replace({'yes':1,'no':0}, inplace=True)
    
    
    
    #Working with unknown data
    age_value_count = df['age'].value_counts()
    print(age_value_count) #no unknown
    
    job_value_count = df['job'].value_counts()
    print(job_value_count) #288 unknowns, checking if unknowns has a pattern
    df['job_unknown'] = df['job'] == 'unknown'
    #print(df['job_unknown'].value_counts())
    
    return df
    
    
    
    
if __name__ == "__main__":
    df = load_dataset()
    df = preprocessing(df)
    print(df.dtypes)
    print(df.head(10))
    
    



