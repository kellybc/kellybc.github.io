#!/usr/bin/env python
# coding: utf-8

# In[1]:


n1 = 25
alpha1 = 0.05


# In[2]:


n2 = 15
t2 = 1.56


# In[3]:


nu = [2, 7, 16, 30]


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp


# In[5]:


nu1 = n1 - 1
print(nu1)


# In[6]:


alpha1_2 = alpha1/2
print(alpha1_2)


# In[7]:


tDist_a = sp.t(nu1)


# In[8]:


print(tDist_a.ppf(1 - alpha1_2)) # Answer to part (a)


# In[9]:


nu2 = n2 - 1
print(nu2)


# In[10]:


tDist_b = sp.t(nu2)


# In[11]:


alpha2 = 2*(1 - tDist_b.cdf(t2))
print(alpha2) # Answer to part (b)


# In[12]:


x = np.linspace(-5, 5, 100)
print(x)


# In[13]:


tDist1 = sp.t(nu[0])
tDist2 = sp.t(nu[1])
tDist3 = sp.t(nu[2])
tDist4 = sp.t(nu[3])


# In[14]:


nDist = sp.norm(0, 1)


# In[15]:


fig, ax = plt.subplots(1, 1)

ax.set_title('Student distribution')
ax.set_xlabel('Random variable, x')
ax.set_ylabel('Probability')
ax.axhline(color='k')
ax.axvline(color='k')

ax.plot(x, tDist1.pdf(x), 'b-', lw=2, label='$\\nu$='+str(nu[0]))
ax.plot(x, tDist2.pdf(x), 'g-', lw=2, label='$\\nu$='+str(nu[1]))
ax.plot(x, tDist3.pdf(x), 'r-', lw=2, label='$\\nu$='+str(nu[2]))
ax.plot(x, tDist4.pdf(x), 'y-', lw=2, label='$\\nu$='+str(nu[3]))

ax.plot(x, nDist.pdf(x), 'k-', lw=2, label='Normal')

ax.legend(loc='best')
plt.show()

