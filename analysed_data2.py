# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 18:15:24 2025

@author: 7430
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from loading_dataset import load_dataset
from data_cleansing import preprocessing



def analyse_data2(df):
    
   #Bi Variable anaylyses
    #Catergorical - job, marital status, education, communication type, previous outcome, month
    #Numerical - age, balance, call duration, pdays, times contacted, previous
    #Binary - default, housing, loan
    
    # Categorical
    
    # 1. job vs y
    
    job_grouped_data = df.groupby(['job', 'y'])['y'].count()
    print(job_grouped_data)
    
    sns.countplot(x='job', hue='y', data=df)
    plt.xlabel("Job Types")
    plt.ylabel("Number of clients")
    plt.xticks(rotation=45)
    plt.title("Clients suscribed by job type")
    plt.show()
    
    # in terms of percentage
    job_y = pd.crosstab(df['job'], df['y'], normalize='index') * 100 #creating a new dataframe job_y
    print(job_y)
    job_y.plot(kind='bar', stacked=True, colormap='Set3')
    plt.title('Percentage of Subscription by Job Type')
    plt.ylabel('Percentage')
    plt.show()  #blue collar has the lowest subscription while students the highest. and this should reflect in age as well.
    
    
    # 2. marital status vs y
    
    mar_grouped_data = df.groupby(['marital_status', 'y'])['y'].count()
    print(mar_grouped_data)
    
    sns.countplot(x='marital_status', hue='y', data=df)
    plt.xlabel("Marital status")
    plt.ylabel("Number of clients")
    plt.xticks(rotation=45)
    plt.title("Clients suscribed by Marital Status")
    plt.show()
    
    # in terms of percentage
    mar_y = pd.crosstab(df['marital_status'], df['y'], normalize='index') * 100 #creating a new dataframe mar_y
    print(mar_y)
    mar_y.plot(kind='bar', stacked=True, colormap='Set3')
    plt.title('Percentage of Subscription by Marital Status')
    plt.ylabel('Percentage')
    plt.show() #married people has the lowest while the single people have the most.
    
    
    
    # 3. Education
    
    edu_grouped_data = df.groupby(['education', 'y'])['y'].count()
    print(edu_grouped_data)
    
    sns.countplot(x='education', hue='y', data=df)
    plt.xlabel("Education")
    plt.ylabel("Number of clients")
    plt.xticks(rotation=45)
    plt.title("Clients suscribed by education")
    plt.show()
    
    # in terms of percentage
    edu_y = pd.crosstab(df['education'], df['y'], normalize='index') * 100 #creating a new dataframe edu_y
    print(edu_y)
    edu_y.plot(kind='bar', stacked=True, colormap='Set3')
    plt.title('Percentage of Subscription by Education')
    plt.ylabel('Percentage')
    plt.show() #highest = tertiary, lowest = primary
    
    
    
    
    # 4. Communication Type
    
    
    com_grouped_data = df.groupby(['communication_type', 'y'])['y'].count()
    print(com_grouped_data)
    
    sns.countplot(x='communication_type', hue='y', data=df)
    plt.xlabel("communication type")
    plt.ylabel("Number of clients")
    plt.xticks(rotation=45)
    plt.title("Clients suscribed by communication type")
    plt.show()
    
    # in terms of percentage
    com_y = pd.crosstab(df['communication_type'], df['y'], normalize='index') * 100 #creating a new dataframe com_y
    print(com_y)
    com_y.plot(kind='bar', stacked=True, colormap='Set3')
    plt.title('Percentage of Subscription by communication type')
    plt.ylabel('Percentage')
    plt.show() #highest = cellular, lowest = unknown
    
    
    
    
    # 5. Previous Outcome
     
    pout_grouped_data = df.groupby(['poutcome', 'y'])['y'].count()
    print(pout_grouped_data)
    
    sns.countplot(x='poutcome', hue='y', data=df)
    plt.xlabel("Previous Outcome")
    plt.ylabel("Number of clients")
    plt.xticks(rotation=45)
    plt.title("Clients suscribed by previous outcome")
    plt.show()
    
    # in terms of percentage
    pout_y = pd.crosstab(df['poutcome'], df['y'], normalize='index') * 100 #creating a new dataframe pout_y
    print(pout_y)
    pout_y.plot(kind='bar', stacked=True, colormap='Set3')
    plt.title('Percentage of Subscription by previous outcome')
    plt.ylabel('Percentage')
    plt.show() #highest = cellular, lowest = unknown
    
    
    
    # 6. Month
    
    month_grouped_data = df.groupby(['month_num', 'y'])['y'].count()
    print(month_grouped_data)
    
    sns.countplot(x='month_num', hue='y', data=df)
    plt.xlabel("Month")
    plt.ylabel("Number of clients")
    plt.xticks(rotation=45)
    plt.title("Clients suscribed by Month")
    plt.show()
    
    # in terms of percentage
    month_y = pd.crosstab(df['month_num'], df['y'], normalize='index') * 100 #creating a new dataframe pout_y
    print(month_y)
    month_y.plot(kind='bar', stacked=True, colormap='Set3')
    plt.title('Percentage of Subscription by month')
    plt.ylabel('Percentage')
    plt.show() #highest = march, lowest = may
    
    
    
    
    # Numerical 
    
    # 1. Age
    
    #Boxplot for Age distribution to look at anomalies
    sns.boxplot(x='y', y='age', data=df)
    plt.title('Balance vs Term Deposit Subscription')
    plt.show()

    #Histogram for a general trend
    sns.histplot(data=df, x='age', hue='y', bins=30, kde=True)
    plt.title('Age Distribution by Subscription')
    plt.show()
    
    #Grouping age into 5-year bins and plotting the subscription rate (y) per age group
    a_bins = range(0, df['age'].max() + 5, 5)  # e.g., 10-15, 15-20, ...
    a_labels = [f"{i}-{i+4}" for i in a_bins[:-1]]  # labels like "10-14", "15-19", etc.
    df['age_group'] = pd.cut(df['age'], bins=a_bins, labels=a_labels, right=False)
    
    age_group_yes_rate = df.groupby('age_group')['y'].mean() * 100
    print(age_group_yes_rate)
    
    #Result as a bar plot
    age_group_yes_rate.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Subscription Rate by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Subscription Rate (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    df.drop(columns=['age_group'], inplace=True)
    
    
    
    
    # 2. Balance
    
    #Boxplot for Balance distribution to look at anomalies
    sns.boxplot(x='y', y='balance', data=df)
    plt.title('Balance vs Term Deposit Subscription')
    plt.show()

    #Histogram for a general trend
    sns.histplot(data=df, x='balance', hue='y', bins=30, kde=True)
    plt.title('Balance Distribution by Subscription')
    plt.show()
    
    #Quantile based grouping, every 10th quantile
    df['balance_group'] = pd.qcut(df['balance'], q=10, precision=0)
    balance_yes_rate = df.groupby('balance_group')['y'].mean() * 100
    print(balance_yes_rate)
    #Balance values at every 10th quantile
    b_quantile_cutoffs = df['balance'].quantile([i/10 for i in range(11)])
    print(b_quantile_cutoffs)
    
    #Bar plot of this analysis
    balance_yes_rate.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Subscription Rate by Balance Group')
    plt.ylabel('Subscription Rate (%)')
    plt.xlabel('Balance Group')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    df.drop(columns=['balance_group'], inplace=True)
    
    
    
    # 3. Call Duration
    
   
    #Boxplot for call duration distribution to look at anomalies
    sns.boxplot(x='y', y='call_duration', data=df)
    plt.title('call duration vs Term Deposit Subscription')
    plt.show()

    #Histogram for a general trend
    sns.histplot(data=df, x='call_duration', hue='y', bins=30, kde=True)
    plt.title('call duration Distribution by Subscription')
    plt.show()
    
    #Quantile based grouping, every 10th quantile
    df['call_duration_group'] = pd.qcut(df['call_duration'], q=10, precision=0)
    call_duration_yes_rate = df.groupby('call_duration_group')['y'].mean() * 100
    print(call_duration_yes_rate)
    #Balance values at every 10th quantile
    c_quantile_cutoffs = df['call_duration'].quantile([i/10 for i in range(11)])
    print(c_quantile_cutoffs)
    
    #Bar plot of this analysis
    call_duration_yes_rate.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Subscription Rate by call duration')
    plt.ylabel('Subscription Rate (%)')
    plt.xlabel('call duration')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    df.drop(columns=['call_duration_group'], inplace=True)
    
    
    
    # 4. previous days
    #a. vs poutcome
    #Boxplot for previous days distribution to look at anomalies
    sns.boxplot(x='poutcome', y='pdays', data=df)
    plt.title('pdays vs previous Term Deposit Subscription')
    plt.show()

    #Histogram for a general trend
    sns.histplot(data=df, x='pdays', hue='poutcome', bins=30, kde=True)
    plt.title('pdays Distribution by previous Subscription')
    plt.show()
    
    #b. vs y
    #Boxplot for previous days distribution to look at anomalies
    sns.boxplot(x='poutcome', y='y', data=df)
    plt.title('pdays vs Term Deposit Subscription')
    plt.show()

    #Histogram for a general trend
    sns.histplot(data=df, x='pdays', hue='y', bins=30, kde=True)
    plt.title('pdays Distribution Subscription')
    plt.show()
    
    
    
    #5. Times contacted
    
    #Boxplot for Times contacted distribution to look at anomalies
    sns.boxplot(x='y', y='times_contacted', data=df)
    plt.title('times contacted vs Term Deposit Subscription')
    plt.show()

    #Histogram for a general trend
    sns.histplot(data=df, x='times_contacted', hue='y', bins=40, kde=True)
    plt.title('times contacted Distribution by Subscription')
    plt.show()
    
    #Grouping age into 3-calls bins and plotting the subscription rate (y) 
    
    c_bins = range(0, df['times_contacted'].max() + 3, 3)  # e.g., 10-15, 15-20, ...
    c_labels = [f"{i}-{i+2}" for i in c_bins[:-1]]  # labels like "10-14", "15-19", etc.
    df['times_contacted_group'] = pd.cut(df['times_contacted'], bins=c_bins, labels=c_labels, right=False)
    
    times_contacted_group_yes_rate = df.groupby('times_contacted')['y'].mean() * 100
    print(times_contacted_group_yes_rate)
    
    #Result as a bar plot
    times_contacted_group_yes_rate.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Subscription Rate by times contacted Group')
    plt.xlabel('times contacted')
    plt.ylabel('Subscription Rate (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    df.drop(columns=['times_contacted_group'], inplace=True)
    

    
    
    # 6. Previous Times contacted
    
    #Boxplot for previous Times contacted distribution to look at anomalies
    sns.boxplot(x='y', y='previous', data=df)
    plt.title('Previou times contacted vs Term Deposit Subscription')
    plt.show()

    #Histogram for a general trend
    sns.histplot(data=df, x='previous', hue='y', bins=40, kde=True)
    plt.title('previous times contacted Distribution by Subscription')
    plt.show()
    
    #Grouping age into 3-calls bins and plotting the subscription rate (y) 
    
    p_bins = range(0, df['previous'].max() + 3, 3)  # e.g., 10-15, 15-20, ...
    p_labels = [f"{i}-{i+2}" for i in p_bins[:-1]]  # labels like "10-14", "15-19", etc.
    df['previous_group'] = pd.cut(df['previous'], bins=p_bins, labels=p_labels, right=False)
    
    previous_group_yes_rate = df.groupby('previous')['y'].mean() * 100
    print(previous_group_yes_rate)
    
    #Result as a bar plot
    previous_group_yes_rate.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Subscription Rate by previous times contacted Group')
    plt.xlabel('times contacted')
    plt.ylabel('Subscription Rate (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    df.drop(columns=['previous_group'], inplace=True)
    
    
    # Binary
    
    # 1. Default
    
    print(df['default'].value_counts())
    print(df['default'].value_counts(normalize=True) * 100)  # percentage of clients with default
    
    b_subscription_rate = df.groupby('default')['y'].mean() * 100
    print("Subscription rate by 'default':\n", b_subscription_rate) 
    
    sns.barplot(x='default', y='y', data=df)
    plt.title("Subscription Rate by 'Default'")
    plt.ylabel("Subscription Rate (%)")
    plt.tight_layout()
    plt.show()


    # 2. Housing loan
    
    print(df['housing'].value_counts())
    print(df['housing'].value_counts(normalize=True) * 100)  # percentage of clients with housing
    
    h_subscription_rate = df.groupby('housing')['y'].mean() * 100
    print("Subscription rate by 'Housing Loan':\n", h_subscription_rate) 
    
    sns.barplot(x='housing', y='y', data=df)
    plt.title("Subscription Rate by housing loan")
    plt.ylabel("Subscription Rate (%)")
    plt.tight_layout()
    plt.show()
    
    
    # 3. Personal loan
    
     
    print(df['loan'].value_counts())
    print(df['loan'].value_counts(normalize=True) * 100)  # percentage of clients with loan
    
    l_subscription_rate = df.groupby('loan')['y'].mean() * 100
    print("Subscription rate by 'Loan':\n", l_subscription_rate) 
    
    sns.barplot(x='loan', y='y', data=df)
    plt.title("Subscription Rate by loan")
    plt.ylabel("Subscription Rate (%)")
    plt.tight_layout()
    plt.show()
    
    
    
    
if __name__ == '__main__':
    df = load_dataset()
    df = preprocessing(df)
    analyse_data2(df)
    print(df.head(10))