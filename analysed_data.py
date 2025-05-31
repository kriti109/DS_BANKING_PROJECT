# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from loading_dataset import load_dataset
from data_cleansing import preprocessing


def analyse_data(df):
    
    
    '-	What is the distribution of age among the clients?'
    
    
    age_value_count = df['age'].value_counts()
    print(age_value_count) 
    plt.hist(df['age'],color='skyblue',edgecolor='black')
    plt.xlabel('age')
    plt.ylabel('frequency')
    plt.title('Distribution of Age')
    plt.show()
    
    
    
    '-	How does the job type vary among the clients?'
    job_value_count = df['job'].value_counts()
    print(job_value_count) 
    plt.hist(df['job'],color='red',edgecolor='black')
    plt.xlabel('job')
    plt.ylabel('frequency')
    plt.title('Distribution of Job')
    plt.show()
    
    
    
    



if __name__ == '__main__':
    df = load_dataset()
    df = preprocessing(df)
    analyse_data(df)
    print(df.head(10))