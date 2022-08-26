#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pint # https://pint.readthedocs.io/en/0.10.1/
import numpy as np


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


N_L = Q_(12, 'in')
N_b = Q_(2, 'in')
N_Pcr = Q_(564, 'kip')


# In[4]:


u_L = N_L * (5 / 100)
u_b = N_b * (5 / 100)
u_Pcr = N_Pcr * (5 / 100)


# In[5]:


N_I = N_b**4 / 12
print(N_I)


# In[6]:


print(np.finfo(float).eps)


# In[7]:


def complexDiff(f, x, h = np.finfo(float).eps):
    df = []
    for i, e in enumerate(x):
        cx = x.copy()
        cx[i] = e + h * 1j
        df.append(f(cx).imag / h)
    return df


# In[8]:


def myFunction(x):
    a = x[0]
    b = x[1]
    c = x[2]
    return a**2 * b + c


# In[9]:


myVars = [5, 2, 1]


# In[10]:


print(complexDiff(myFunction, myVars))


# In[11]:


def I(x):
    b = x[0]
    return b**4 / 12


# In[12]:


dI = complexDiff(I, [N_b.to('in').magnitude])
print(dI)


# In[13]:


dIdb = Q_(dI[0], 'in**3')
print(dIdb)


# In[14]:


u_I = ((u_b * dIdb)**2)**0.5
print(u_I)


# In[15]:


def E(x):
    P_cr = x[0]
    L = x[1]
    I = x[2]
    return P_cr * L**2 / (4 * math.pi**2 * I)


# In[16]:


N_E = E([N_Pcr, N_L, N_I])
print('Answer, first part: The nominal value of the elastic modulus is '
      + str(round(N_E.to('ksi').magnitude, 1)) + ' ksi.') # Answer, first part


# In[17]:


dE = complexDiff(E, [N_Pcr.to('lbf').magnitude,
                     N_L.to('in').magnitude,
                     N_I.to('in**4').magnitude])
print(dE)


# In[18]:


dEdPcr = Q_(dE[0], '1/in**2')
dEdL = Q_(dE[1], 'lbf/in**3')
dEdI = Q_(dE[2], 'lbf/in**6')
print(dEdPcr)
print(dEdL)
print(dEdI)


# In[19]:


u_E = ((u_Pcr * dEdPcr)**2 + (u_L * dEdL)**2 + (u_I * dEdI)**2)**0.5
print('Answer, first part: The uncertainty of the elastic modulus is '
      + str(round(u_E.to('ksi').magnitude, 1)) + ' ksi.') # Answer, first part


# In[20]:


up_E = u_E / N_E
print('The percent uncertainty is ' + str(round(up_E.magnitude*100, 2)) + '%.')


# In[21]:


u_L = N_L * (1 / 100)
u_b = N_b * (1 / 100)
u_Pcr = N_Pcr * (1 / 100)


# In[22]:


u_I = ((u_b * dIdb)**2)**0.5
print(u_I)


# In[23]:


u_E = ((u_Pcr * dEdPcr)**2 + (u_L * dEdL)**2 + (u_I * dEdI)**2)**0.5
print('Answer, second part: The uncertainty of the elastic modulus is '
      +str(round(u_E.to('ksi').magnitude, 1)) + ' ksi.') # Answer, second part


# In[24]:


up_E = u_E / N_E
print('The percent uncertainty is ' + str(round(up_E.magnitude*100, 2)) + '%.')

