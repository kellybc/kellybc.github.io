#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


x = [1, 2, 3]
y = [2, 4, 1]


# In[3]:


fig, ax = plt.subplots(1, 1)

ax.plot(x, y)

plt.show()


# In[4]:


fig, ax = plt.subplots(1, 1)

ax.plot(x, y)

ax.set_xlabel('x - axis')
ax.set_ylabel('y - axis')
ax.set_title('My first graph!')

plt.show()


# In[5]:


x1 = [1, 2, 3]
y1 = [2, 4, 1]

x2 = [1, 2, 3]
y2 = [4, 1, 3]


# In[6]:


fig, ax = plt.subplots(1, 1)

ax.plot(x1, y1, label='Series 1')
ax.plot(x2, y2, label='Series 2')

ax.set_xlabel('x - axis')
ax.set_ylabel('y - axis')
ax.set_title('Two series on the same graph!')

ax.legend()

plt.show()


# In[7]:


x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 5, 2, 6]


# In[8]:


fig, ax = plt.subplots(1, 1)

ax.plot(x, y, color='green', linestyle='dashed', linewidth=3, marker='o',
        markerfacecolor='blue', markersize=12)

ax.set_xlim(1, 8)
ax.set_ylim(1, 8)

ax.set_xlabel('x - axis')
ax.set_ylabel('y - axis')
ax.set_title('Some cool customizations!')

plt.show()


# In[9]:


x = [1, 2, 3, 4, 5]
height = [10, 24, 36, 40, 5] # i.e. the y values
bar_labels = ['dogs', 'cats', 'fishes', 'birds', 'lizards']


# In[10]:


fig, ax = plt.subplots(1, 1)

ax.bar(x, height, tick_label=bar_labels, width=0.8, color=['red', 'green'])

ax.set_xlabel('Pets')
ax.set_ylabel('Number of Pets')
ax.set_title('My bar chart!')

plt.show()


# In[11]:


ages = [2, 5, 70, 40, 30, 45, 50, 45, 43, 40, 44, 60, 7, 13, 57, 18, 90, 77,
        32, 21, 20, 40]


# In[12]:


r = [0, 100]
bins = 10


# In[13]:


fig, ax = plt.subplots(1, 1)

ax.hist(ages, bins, r, color='green', histtype='bar', rwidth=0.8)

ax.set_xlim(r)

ax.set_xlabel('Age')
ax.set_ylabel('Number of people')
ax.set_title('My histogram')

plt.show()


# In[14]:


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]


# In[15]:


fig, ax = plt.subplots(1, 1)

ax.scatter(x, y, color='green', marker='*', s=30)

ax.set_xlabel('x – axis')
ax.set_ylabel('y – axis')
ax.set_title('My scatter plot!')

plt.show()


# In[16]:


activities = ['eat', 'sleep', 'work', 'play']
time_spent = [3, 7, 8, 6]


# In[17]:


sector_colors = ['r', 'y', 'g', 'b']


# In[18]:


fig, ax = plt.subplots(1, 1)

ax.pie(time_spent, labels=activities, colors=sector_colors, startangle=90,
       shadow=True, explode=[0, 0, 0.1, 0], radius=1.2, autopct='%1.1f%%')

ax.legend()

plt.show()


# In[19]:


x = [0, 1, 2, 3, 4, 5]

y1 = [6, 3, 9, -3, 12, -6]
y2 = [0, 1, 4, 9, 16, 25]

plt.subplot(2, 1, 1)
plt.plot(x, y1, 'o-')
plt.ylabel('y1 data')

plt.subplot(2, 1, 2)
plt.plot(x, y2, 'o-')
plt.ylabel('y2 data')

plt.suptitle('A tale of 2 subplots')

plt.show()


# In[20]:


x = [0, 1, 2, 3, 4, 5]

y1 = [6, 3, 9, -3, 12, -6]
y2 = [0, 1, 4, 9, 16, 25]

fig, ax = plt.subplots(2, 1)

fig.suptitle('A tale of 2 subplots')

ax[0].plot(x, y1, 'o-')
ax[0].set_ylabel('y1 data')

ax[1].plot(x, y2, 'o-')
ax[1].set_ylabel('y2 data')

plt.show()


# In[21]:


x = [0, 1, 2, 3, 4, 5]
y = [6, 3, 9, -3, 12, -6]


# In[22]:


fig, ax = plt.subplots(2, 2)

fig.suptitle('Four plots on one figure', y=1.05)

ax[0, 0].plot(x, y, 'o-')
ax[0, 0].set_ylabel('Top Left y Axis Label')

ax[1, 0].bar(x, y)
ax[1, 0].set_xlabel('x data')
ax[1, 0].set_ylabel('Bottom Left y Axis Label')

ax[0, 1].scatter(x, y)
ax[0, 1].set_xlabel('Top Right x Axis Label')
ax[0, 1].set_ylabel('Top Right y Axis Label')

ax[1, 1].plot(y, x, 'o-')
ax[1, 1].set_xlabel('Bottom Right x Axis Label')
ax[1, 1].set_ylabel('Bottom Right y Axis Label')

plt.tight_layout()
plt.show()

