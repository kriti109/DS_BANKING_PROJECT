# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 14:16:48 2025

@author: 7430
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from loading_dataset import load_dataset
from data_cleansing import preprocessing



def analyse_data3(df):
    
    
    
    
    
    
   
if __name__ == '__main__':
    df = load_dataset()
    df = preprocessing(df)
    analyse_data3(df)
    print(df.head(10))