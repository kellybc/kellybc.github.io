#!/usr/bin/env python
# coding: utf-8

# In[1]:


Rbar = 25 # in ohms


# In[2]:


S_Rbar = 0.5 # in ohms


# In[3]:


import scipy.stats as sp


# In[4]:


n = 36


# In[5]:


CL = 0.9


# In[6]:


a = 1 - CL
print(a)


# In[7]:


a2 = a/2
print(a2)


# In[8]:


n_dist = sp.norm(0, 1)


# In[9]:


z_a2 = n_dist.ppf(1 - a2)
print(z_a2)


# In[10]:


print('The population mean lies between ', end='')
print(str(round(Rbar - z_a2 * S_Rbar / n**0.5, 3)), end='')
print(' and ', end='')
print(str(round(Rbar + z_a2 * S_Rbar / n**0.5, 3)), end='')
print(' ohms.')    # Answer


# In[11]:


print('The population mean is ', end='')
print(str(round(Rbar, 2)) + ' +/- ', end='')
print(str(round(z_a2 * S_Rbar / n**0.5, 3)), end='')
print(' ohms.')    # Answer

