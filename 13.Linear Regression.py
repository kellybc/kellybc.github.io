#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def linear_coeffs(x, y):
    # create a NumPy vector #
    Y = np.array(y)
    
    # Build the X matrix #
    X = []
    for x_i in x:
        X.append([1, x_i])
    
    # create a true NumPy matrix instead of just a list of lists #
    X = np.array(X)
    
    # Calculate B, B = (X'X)^(-1) X' Y
    B = np.matmul(
            np.matmul(
                np.linalg.inv(
                    np.matmul(np.transpose(X), X)
                ), np.transpose(X)
            ), Y
        )
    
    return B


# In[3]:


x = [1, 2, 3, 4]
y = [6, 5, 7, 10]


# In[4]:


print(linear_coeffs(x, y))


# In[5]:


T = [12.2, 22.1, 57.4]
R = [16640.63, 11136.36, 3081.84]


# In[6]:


print(linear_coeffs(R, T))


# In[7]:


print(linear_coeffs(T, R))


# In[8]:


import statistics

def coeff_of_determination(xs, ys, f):
    num = 0
    denom = 0
    ybar = statistics.mean(ys)
    for i, x in enumerate(xs):
        num += (ys[i] - f(x))**2
        denom += (ys[i] - ybar)**2
    R2 = 1 - num/denom
    return R2


# In[9]:


def my_fit(x):
    B = linear_coeffs(R, T)
    y = B[0] + B[1]*x
    return y


# In[10]:


print(coeff_of_determination(R, T, my_fit))

