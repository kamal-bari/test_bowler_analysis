#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import os
os.getcwd()


# In[3]:


os.chdir(r'H:\Training\EMK Center Data science with Python\Module 3- Data analysis with Python')


# In[4]:


os.getcwd()


# In[5]:


df = pd.read_excel("test_cricket.xlsx", sheet_name='wickets')

display(df.head(10))


# In[6]:


print(df.columns)


# In[ ]:


# {'Player'= 'Player_Name', 'Span'= 'Career_duration', 'Mat'= 'No_match_played', 'Inns' = 'No_innings', 'Balls':'No_balls_bowled',
# 'Runs': 'Runs_considered', 'Wkts' = 'Total_wickets_taken', 'BBI' = 'Best_Bowling_in_Innings', 'BBM' = 'Best_Bowling_in_Match',
# 'Ave' = 'Average_runs_per_wicket', 'Econ' = 'average_runs_conceded_per_over', 'SR'= 'Strike_rate', 
# 5 = 'No_times_5_wickets_taken', 10 = 'No_times_10_wickets_taken'} 


# In[7]:


# number of rows
print("number of rows = ", df.shape[0])

# number of columns
print("number of columns = ", df.shape[1])


# In[8]:


# checking data statistics
display(df.describe())


# In[9]:


print(df.dtype)


# In[10]:


# checking data types 
print(df.dtypes)


# In[11]:


# checking for missing values
print(df.info())


# In[12]:


# checking for missing values
print(df.info())


# In[13]:


print(d.isnull())


# In[14]:


# Checking missing values in the data frame
print(df.isnull())


# In[15]:


df = df.rename(columns = {'Player':'Player_Name',
                          'Span':'Career_duration',
                          'Mat':'No_match_played', 
                          'Inns':'No_innings', 
                          'Balls':'No_balls_bowled',
                          'Runs': 'Runs_considered', 
                          'Wkts':'Total_wickets_taken', 
                          'BBI': 'Best_Bowling_in_Innings', 
                          'BBM':'Best_Bowling_in_Match',
                          'Ave':'Average_runs_per_wicket',
                          'Econ':'average_runs_conceded_per_over', 
                          'SR':'Strike_rate',
                          5: 'No_times_5_wickets_taken', 
                          10:'No_times_10_wickets_taken'})
display(df.head())


# In[16]:


df_player = df['Player_Name'].str.split("(", expand=True)

display(df_player.head(10))


# In[17]:


df = pd.concat([df, df_player], axis=1)

display(df.head())


# In[18]:


# Removing first column
df = df.drop('Player_Name', axis=1)
display(df.head())


# In[19]:


# Renaming spliting columns
df = df.rename(columns={0: 'Player',
                        1: 'Country'})

display(df.head())


# In[20]:


# removing a value from a pandas column
df['Country'] = df['Country'].str.replace(")", "")

display(df.head())


# In[21]:


print(df.columns)


# In[22]:


new_col_sequence = ['Player','Country','Career_duration', 'No_match_played', 'No_innings', 'No_balls_bowled',
       'Runs_considered', 'Total_wickets_taken', 'Best_Bowling_in_Innings',
       'Best_Bowling_in_Match', 'Average_runs_per_wicket',
       'average_runs_conceded_per_over', 'Strike_rate',
       'No_times_5_wickets_taken', 'No_times_10_wickets_taken']
df = df[new_col_sequence]
display(df.head())


# In[ ]:




