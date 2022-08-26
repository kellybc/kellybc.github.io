#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd    # https://pandas.pydata.org/pandas-docs/stable/ #


# In[2]:


#pd.set_option('display.max_columns', 999) #
#pd.set_option('display.width', 1000) #


# In[3]:


birth_year = 1989
birth_state = 'Louisiana'


# In[4]:


df = pd.read_excel('datasets/1976-2016-president.xlsx', 
                   sheet_name = '1976-2016-president')


# In[5]:


df.head() # NOTE: if you are running this script in Thonny, you must write print(df.head()) #


# In[6]:


df.head(7) # NOTE: if you are running this script in Thonny, you must write print(df.head(7)) #


# In[7]:


df.tail() # NOTE: if you are running this script in Thonny, you must write print(df.tail()) #


# In[8]:


df.tail(6) # NOTE: if you are running this script in Thonny, you must write print(df.tail()) #


# In[9]:


election_year = birth_year - birth_year%4 
election_year # NOTE: if you are running this script in Thonny, you must write print(electionYear) #


# In[10]:


cond1 = df['year'] == election_year


# In[11]:


cond2 = df['state'] == birth_state


# In[12]:


results = df[cond1 & cond2]
results # NOTE: if you are running this script in Thonny, you must write print(results) #


# In[13]:


data = results.sort_values('candidatevotes', ascending = False).head(2)
data # NOTE: if you are running this script in Thonny, you must write print(data) #


# In[14]:


winner_name = data.iloc[0]['candidate']
winner_party = data.iloc[0]['party']
winner_vote = data.iloc[0]['candidatevotes']
runner_vote = data.iloc[1]['candidatevotes']


# In[15]:


print('In the ' + str(election_year) + ' U.S. Presidential election,', end='')
print(' the presidential candidate ' + winner_name + ' (', end='')
print(winner_party + ') won by ' + str(winner_vote - runner_vote) + ' ', end='')
print('votes with ' + str(winner_vote) + ' total votes in ' + birth_state + '.')

