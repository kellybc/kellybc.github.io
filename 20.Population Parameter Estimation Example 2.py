#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = [1250, 1320, 1542, 1464, 1275, 1383]


# In[2]:


import statistics as stats
import scipy.stats as sp


# In[3]:


CL = 0.95


# In[4]:


n = len(data)
print(n)


# In[5]:


Tbar = stats.mean(data)
print(Tbar)


# In[6]:


S_Tbar = stats.stdev(data)
print(S_Tbar)


# In[7]:


v = n - 1
print(v)


# In[8]:


a = 1 - CL
print(a)


# In[9]:


a2 = a / 2
print(a2)


# In[10]:


t_dist = sp.t(v)


# In[11]:


t_a2 = t_dist.ppf(1 - a2)
print(t_a2)


# In[12]:


print('The population mean lies between ', end='')
print(str(round(Tbar - t_a2 * S_Tbar / n**0.5, 1)), end='')
print(' and ', end='')
print(str(round(Tbar + t_a2 * S_Tbar / n**0.5, 1)), end='')
print(' hrs.')


# In[13]:


print('The population mean is ', end='')
print(str(round(Tbar, 2)) + ' +/- ', end='')
print(str(round(t_a2 * S_Tbar / n**0.5, 1)), end='')
print(' hours.')    # Answer

