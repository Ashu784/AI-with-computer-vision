#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 


# In[10]:


data = pd.read_csv('lab1.csv')


# In[11]:


data


# In[12]:


concepts = np.array(data)[:,:-1]


# In[13]:


concepts


# In[14]:


target = np.array(data)[:,-1]


# In[15]:


target


# In[16]:


def train(con,tar):
    for i, val in enumerate(tar):
        if val == 'yes':
            specific_h = con[i].copy()
            break
            
    for i,val in enumerate(con):
        if tar[i] == 'yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
    return specific_h
        


# In[17]:


print(train(concepts,target))


# In[ ]:




