#!/usr/bin/env python
# coding: utf-8

# In[1]:


V_t = 6.11 # in V


# In[2]:


data = [5.98, 6.05, 6.15, 6.06, 5.99, 6.00, 6.08, 6.03, 6.11] # in V


# In[3]:


import numpy as np


# In[4]:


V_avg = np.mean(data)
print(V_avg)


# In[5]:


B = abs(V_avg - V_t)
print(B)


# In[6]:


print(round(B, 2)) # answer to part (a)


# In[7]:


E = [abs(min(data)-V_avg), abs(max(data)-V_avg)]
print(E)


# In[8]:


P = max(E)
print(P)


# In[9]:


print(round(P, 2))


# In[10]:


R = [0, 5000] # in rpm


# In[11]:


Ap = 5 # as a percentage


# In[12]:


Z = 200 # in rpm


# In[13]:


S = 3500 # in rpm


# In[14]:


A_e = (Ap/100)*(R[1]-R[0])
print(A_e)


# In[15]:


M = A_e + Z
print(M)

