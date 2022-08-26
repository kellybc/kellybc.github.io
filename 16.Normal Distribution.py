#!/usr/bin/env python
# coding: utf-8

# In[1]:


m_a = [0, 5, 10]
s_a = [1, 2, 4]


# In[2]:


m_b = 100
s_b = 37
x_b = [50, 75, 140]


# In[3]:


m_c = 42
s_c = 7
P_c = [0.66, 0.75, 0.95]


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp


# In[5]:


x_a1 = np.linspace(-5, 5, 100)


# In[6]:


n_a1 = sp.norm(m_a[0], s_a[0])


# In[7]:


fig, ax = plt.subplots(1, 1)

ax.set_title('Normal distribution')
ax.set_xlabel('Random variable, x')
ax.set_ylabel('Probability')

# axhiline() and axvline() create a horizontal and vertical line at the origin
ax.axhline(color='k')
ax.axvline(color='k')

ax.plot(x_a1, n_a1.pdf(x_a1), 'b-', lw=2,
        label='$\mu$='+str(m_a[0])+', $\sigma$='+str(s_a[0]))

plt.show()


# In[8]:


x_a2 = np.linspace(-5, 15, 100)
x_a3 = np.linspace(0, 25, 100)


# In[9]:


n_a2 = sp.norm(m_a[1], s_a[1])
n_a3 = sp.norm(m_a[2], s_a[2])


# In[10]:


fig, ax = plt.subplots(1, 1)

ax.set_title('Normal distribution')
ax.set_xlabel('Random variable, x')
ax.set_ylabel('Probability')

# axhiline() and axvline() create a horizontal and vertical line at the origin
ax.axhline(color='k')
ax.axvline(color='k')

ax.plot(x_a1, n_a1.pdf(x_a1), 'b-', lw=2,
        label='$\mu$=' + str(m_a[0]) + ', $\sigma$=' + str(s_a[0]))
ax.plot(x_a2, n_a2.pdf(x_a2), 'g-', lw=2,
        label='$\mu$=' + str(m_a[1]) + ', $\sigma$=' + str(s_a[1]))
ax.plot(x_a3, n_a3.pdf(x_a3), 'r-', lw=2,
        label='$\mu$=' + str(m_a[2]) + ', $\sigma$=' + str(s_a[2]))

ax.legend(loc='best')
plt.show()    # Answer to part (a)


# In[11]:


n_b = sp.norm(m_b, s_b)


# In[12]:


P_b1=n_b.cdf(x_b[0])
P_b2=n_b.cdf(x_b[1])
P_b3=n_b.cdf(x_b[2])

print('The probability that the random variable value '+str(x_b[0])+' or '
      'anything less than the value will occur is '+str(round(P_b1, 4))+'.')
print('The probability that the random variable value '+str(x_b[1])+' or '
      'anything less than the value will occur is '+str(round(P_b2, 4))+'.')
print('The probability that the random variable value '+str(x_b[2])+' or '
      'anything less than the value will occur is '+str(round(P_b3, 4))+'.')
print('')    # Answer to part (b)


# In[13]:


n_c = sp.norm(m_c, s_c)


# In[14]:


x_c1 = n_c.ppf(P_c[0])
x_c2 = n_c.ppf(P_c[1])
x_c3 = n_c.ppf(P_c[2])

print('There is a '+str(P_c[0])+' chance that the value of '+str(round(x_c1, 2))
      +' or less will occur.')
print('There is a '+str(P_c[1])+' chance that the value of '+str(round(x_c2, 2))
      +' or less will occur.')
print('There is a '+str(P_c[2])+' chance that the value of '+str(round(x_c3, 2))
      +' or less will occur.')
print('') # Answers to part (c)

