#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open("datasets/cfb_school_standings_2020.csv").read()


# In[2]:


print(f[:300]) # Note: The [:300] limits the print statement the first 300 characters of the string


# In[3]:


rows = f.strip().split('\n')


# In[4]:


print(rows[:5]) # Note: The [:5] limits the print statement the first 5 elements of the list


# In[5]:


cells = []

for row in rows:
    cells.append(row.split(','))


# In[6]:


print(cells[:2])


# In[7]:


print(cells[2])


# In[8]:


print(cells[2][1])


# In[9]:


cells.pop(0)
cells.pop(0)
print(cells[0])


# In[10]:


team_names = []
ppgs = []

for cell in cells:
    if cell[9].strip() != '' and cell[10].strip() != '':
        team_names.append(cell[1])
        ppgs.append(float(cell[9]) - float(cell[10]))


# In[11]:


max_value = ppgs[0]
index_of_max = 0

for i, ppg in enumerate(ppgs):
    if ppg > max_value:
        max_value = ppg
        index_of_max = i

print(max_value)
print(index_of_max)
print(team_names[index_of_max])


# In[12]:


L = ['a', 'b', 'c']
for e in enumerate(L):
    print(e)


# In[13]:


min_value = ppgs[0]
index_of_min = 0

for i, ppg in enumerate(ppgs):
    if ppg < min_value:
        min_value = ppg
        index_of_min = i

print(min_value)
print(index_of_min)
print(team_names[index_of_min])


# In[14]:


print(team_names[index_of_max], end = '')
print(' has the highest difference between the offense and defense', end = '')
print(' points per game with a value of ' + str(round(max_value, 1)) + '.')
print(team_names[index_of_min], end = '')
print(' has the lowest difference between the offense and defense', end = '')
print(' points per game with a value of ' + str(round(min_value, 1)) + '.')


# In[15]:


print("Max Difference: " + team_names[ppgs.index(max(ppgs))])
print("Min Difference: " + team_names[ppgs.index(min(ppgs))])

