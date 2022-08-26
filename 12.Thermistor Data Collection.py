#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# define function that takes the resistance value of the thermistor and
# converts it to temperature in degC by using the manufacturer's theorectical
# expression.
# R2 - numeric in ohms
# B  - (optional) numeric in Kelvin that represents beta value of thermistor
# R1 - (optional) numeric in ohms that represents the thermistor calibration
#      resistance point
# T1 - (optional) numeric in Kelvin that represents the thermistor calibration
#      temperature point
# Kelvin - (optional) boolean that determines whether the returned temperature
#          value will be in Kelvin or degC
def therm_theo_exp(R2, B = 3470, R1 = 10000, T1 = 298.15, Kelvin = False):
    unitConversion = 273.15
    if Kelvin:
        unitConversion = 0
    T = B/math.log((R2/R1)*math.exp(B/T1)) - unitConversion
    return T


# In[2]:


R = 16640.63 # Resistance in ohms
print(therm_theo_exp(R)) # temperature in degC


# In[3]:


print(therm_theo_exp(R, T1 = 400, R1 = 20000))


# In[4]:


print(therm_theo_exp(R, Kelvin = True)) # temperature in K

