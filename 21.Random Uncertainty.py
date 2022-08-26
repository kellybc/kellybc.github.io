#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = [48530, 48980, 50210, 49860, 48560, 49540, 49270, 48850, 49320, 48680]


# In[2]:


a = 1.5


# In[3]:


R = [0, 100000]


# In[4]:


HV = 49500


# In[5]:


import scipy.stats as sp
import statistics as stats


# In[6]:


xbar = stats.mean(data)
print(xbar)


# In[7]:


S_xbar = stats.stdev(data)
print(S_xbar)


# In[8]:


n = len(data)
print(n)


# In[9]:


nu = n-1
print(nu)


# In[10]:


t_dist = sp.t(nu)


# In[11]:


t = t_dist.ppf(1-(1-0.95)/2)
print(t)


# In[12]:


P_x = t * S_xbar / 1**0.5
print('The random uncertainty for each measurement is ', end='')
print(format(P_x, '.1f'), end='')
print(' kJ/kg.')    # ANSWER (a)


# In[13]:


P_xbar = t * S_xbar / n**0.5
print('The random uncertainty for the mean of the measurements is ', end='')
print(format(P_xbar, '.1f'), end='')
print(' kJ/kg.') # ANSWER (b)


# In[14]:


P_large = 2 * S_xbar / n**0.5
print('The random uncertainty for the mean, assuming a large sample ', end='')
print('size with the same standard deviation, is ', end='')
print(format(P_large, '.1f'), end='')
print(' kJ/kg.') # ANSWER (c)


# In[15]:


B_x = (a / 100) * (R[1] - R[0])
print(B_x)


# In[16]:


u_xbar = (B_x**2 + P_xbar**2)**0.5
print('The total uncertainty in the mean value is ', end='')
print(format(u_xbar, '.1f'), end='')
print(' kJ/kg.') # ANSWER (d)


# In[17]:


up_xbar = 100 * u_xbar / HV
print(up_xbar)


# In[18]:


u_x = (B_x**2 + P_x**2)**0.5
print('The total uncertainty in a single measurement is ', end='')
print(format(u_x, '.1f'), end='')
print(' kJ/kg.') # ANSWER (e)


# In[19]:


up_x = 100 * u_x / HV
print(up_x)

