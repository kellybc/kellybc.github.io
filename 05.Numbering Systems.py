#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = 1*2**0 + 0*2**1 + 1*2**2 + 1*2**3 + 0*2**4 + 0*2**5 + 1*2**6
print(N) # Answer to part a


# In[2]:


N = 14*16**0 + 4*16**1 + 10*16**2 + 3*16**3
print(N) # Answer to part b


# In[3]:


N = 3*4**0 + 2*4**1
print(N) # Answer to part c


# In[4]:


N = 74754 # the decimal number
b = 16 # the desired base system
Q = [] # an empty list that will contain the quotients
R = [] # an empty list that will contain the remainders

i = 0
Q.append(N//b)
R.append(N%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)

i += 1
Q.append(Q[i-1]//b)
R.append(Q[i-1]%b)


# In[5]:


print(Q)
print(R)


# In[6]:


R.reverse()
print(R)


# In[7]:


S = str(R[0]) + str(R[1]) + str(R[2]) + str(R[3]) + str(R[4])
print(S) # answer to part b


# In[8]:


N = 563 # the decimal number
b = 7 # the desired base system
Q = [] # an empty list that will contain the quotients
R = [] # an empty list that will contain the remainders

Q.append(N//b)
R.append(N%b)

i = 0
while Q[i]!=0 or i>100:
    i += 1
    Q.append(Q[i-1]//b)
    R.append(Q[i-1]%b)


# In[9]:


print(Q)
print(R)


# In[10]:


R.reverse()
print(R)


# In[11]:


S = str(R[0]) + str(R[1]) + str(R[2]) + str(R[3])
print(S) # answer to part c

