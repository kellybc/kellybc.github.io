#!/usr/bin/env python
# coding: utf-8

# In[1]:


def birthday_paradox(n, days_in_year = 365):
    pp = 1
    for i in range(1, n + 1):
        pp *= (1 - (n - i)/days_in_year)
    return 1 - pp


# In[2]:


birthday_paradox(16) # Answer


# In[3]:


birthday_paradox(23)


# In[4]:


birthday_paradox(47)


# In[5]:


filename = 'datasets/exam_grades.csv'


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


file = open(filename).read().strip()


# In[8]:


rows = file.split('\n')


# In[9]:


rows.pop(0)


# In[10]:


data = [int(r) for r in rows]


# In[11]:


n = len(data)
print(n)


# In[12]:


B = 20


# In[13]:


fig, ax = plt.subplots(1, 1)

ax.hist(data, bins = B)

ax.set_title('Exam Grade Occurance')
ax.set_xlabel('Exam Grade')
ax.set_ylabel('Number of students with grade')

plt.show()

