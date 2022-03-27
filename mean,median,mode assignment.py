#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.DataFrame(np.random.rand(1000,5),columns = ('col_1','col_2','col_3','col_4','col_5'))
df.head()


# In[4]:


df.mean()


# In[5]:


df.mode()


# In[6]:


df.round(2).mode


# In[7]:


df['col_1'].mean()


# In[8]:


df['col_1'].median()


# In[9]:


df['col_1'].round(2).mode()


# In[ ]:




