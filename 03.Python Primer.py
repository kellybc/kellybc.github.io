#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[2]:


print('Hello, World!')


# In[3]:


print(Hello, World!)


# In[4]:


a = 17
b = 7
print(a + b)


# In[5]:


x = 1
print(type(x))


# In[6]:


y = 2.8
print(type(y))


# In[7]:


z = 1.6 + 3.2j
print(type(z))


# In[8]:


print(a + b)


# In[9]:


print(a - b)


# In[10]:


print(a * b)


# In[11]:


print(a / b)


# In[12]:


print(a % b)


# In[13]:


print(a ** b)


# In[14]:


print(a // b)


# In[15]:


a = 16
b = 7
a += b # the same as a = a + b
print(a)


# In[16]:


a = 16
b = 7
a -= b # the same as a = a - b
print(a)


# In[17]:


a = 16
b = 7
a *= b # the same as a = a *b
print(a)


# In[18]:


a = 16
b = 7
a /= b # the same as a = a / b
print(a)


# In[19]:


a = 16
b = 7
a %= b # the same as a = a % b
print(a)


# In[20]:


a = 16
b = 7
a **= b # the same as a = a ** b
print(a)


# In[21]:


a = 16
b = 7
a //= b # the same as a = a // b
print(a)


# In[22]:


print(a == b)


# In[23]:


print(a != b)


# In[24]:


print(a > b)


# In[25]:


print(a >= b)


# In[26]:


print(a < b)


# In[27]:


print(a <= b)


# In[28]:


cars = ['Ford', 'Volvo', 'BMW']
print(cars)


# In[29]:


print(cars[2])


# In[30]:


fruits = ('apple', 'banana', 'cherry')
print(fruits)


# In[31]:


print(fruits[2])


# In[32]:


pets = {'dog', 'cat', 'fish', 'dog'}
print(pets)


# In[33]:


player1 = {'name': 'Babe Ruth', 'height': '6ft 2in', 'weight': 215}
print(player1)


# In[34]:


print(player1['name'])


# In[35]:


player2 = {
    'name': 'Mickey Mantle',
    'weight': 195,
    'height': '5ft 11in'
}
print(player2)


# In[36]:


a = 200
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('b is equal to a')
else:
    print('b is less than a')


# In[37]:


a = 200
b = 33
c = 5
# conditional statement 1
if b == 33 or c == 6:
    print('b equals 33 or c equals 6.')

# conditional statement 2
if b > a and c == 4:
    print('b is greater than a and c equals 4.')
elif a == b:
    print('b is equal to a.')
else:
    print('b is less than a')
    print('or b is greater than a and c does not equal 4.')


# In[38]:


a = 200
b = 33
if not a == b:
    print('a is not equal to b.')
else:
    print('a is equal to b.')


# In[39]:


i = 0
while i < 10:
    print(i)
    i += 1 # what happens if this line is not here?


# In[40]:


i = 0
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1


# In[41]:


# i = 0
# while i < 10:
#     print(i)
#     if i == 3:
#         continue
#     i += 1


# In[42]:


snacks = ['chips', 'apples', 'peanuts']
for snack in snacks:
    print(snack)


# In[43]:


for x in range(6): # same as range(0, 6, 1)
    print(x)


# In[44]:


for x in range(2, 7): # same as range(2, 7, 1)
    print(x)


# In[45]:


for x in range(0, 21, 3):
    print(x)


# In[46]:


def my_function1():
    print('What')


# In[47]:


def my_function2(a, b):
    return a + b ** 2


# In[48]:


def my_function3(a, b):
    if a > b:
        return a + b
    elif a < b:
        return b - a
    else:
        return a * b


# In[49]:


print(my_function1())


# In[50]:


print(my_function2(3, 4))


# In[51]:


print(my_function3(3, 3))


# In[52]:


print(my_function3(4, 2))


# In[53]:


print(my_function3(2, 3))


# In[54]:


greeting = 'Hello'
name = 'Will'
print(greeting + ' ' + name)


# In[55]:


greeting = 'Hello'
name = 'Will'
question = 'How\'s it going?'
print(greeting + ' ' + name + '. ' + question)


# In[56]:


greeting = 'Hello'
name = 5
print(greeting + ' ' + name)


# In[57]:


greeting = 'Hello'
name = '5'
print(greeting + ' ' + name)


# In[58]:


greeting = 'Hello'
name = 5
print(greeting + ' ' + str(name))


# In[ ]:




