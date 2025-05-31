# -*- coding: utf-8 -*-
"""
Created on Wed May 28 16:59:38 2025

@author: 7430
"""

'Loading the dataset and starting the work on it.'
'importing the libraries'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_dataset():
    file_path = r'banking_data1.csv'
    df = pd.read_csv(file_path)

    'makes sure none of the rows or columns are cut out.'
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    return df


if __name__ == "__main__":
    df = load_dataset()

    'displaying dataset info'
    print(df.info())
    'displaying the first 10 rows of dataset'
    print(df.head(10))

    print(df.shape) #(rows, columns)

    print(df.columns)  #mentions all the columns 





