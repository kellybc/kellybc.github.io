#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pint


# In[2]:


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


# In[3]:


N_T = Q_(25, 'degC')
u_T = Q_(2, 'delta_degC')
up_P = 1 / 100
N_P = Q_(250, 'kPa')


# In[4]:


u_P = N_P * up_P
print(u_P)


# In[5]:


N_R = Q_(287.05, 'J/(kg K)')


# In[6]:


N_rho=N_P / (N_R * N_T.to('K'))


# In[7]:


print('Answer, first part: The nominal value of the density is '+
      str(round(N_rho.to('kg/m**3').magnitude, 2))+' kg/m^3.') # Answer, first part


# In[8]:


drho_dP = 1 / (N_R * N_T.to('K'))
drho_dT = -N_P / (N_R * N_T.to('K')**2)


# In[9]:


u_rho = ((u_P * drho_dP)**2 + (u_T.to('K') * drho_dT)**2)**0.5


# In[10]:


print('Answer, second part: The uncertainty of the density is '+
      str(round(u_rho.to('kg/m**3').magnitude, 5))+' kg/m^3.') # Answer, second part

