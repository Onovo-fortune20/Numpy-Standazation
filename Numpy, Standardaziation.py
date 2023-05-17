#!/usr/bin/env python
# coding: utf-8

# Number1
# 

# In[1]:


import  numpy as np
arr = np.random.randn(6, 7)

arr
arr.mean()
np.std(arr)


# In[2]:


import  numpy as np
arr = np.random.randn(6, 7)

arr

np.std(arr)


# In[3]:


import numpy as np
nwalks = 3*1000

nsteps = 3*1000

draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1

steps = np.where(draws > 0, 1, -1)

walks = steps.cumsum(1)

walks


# In[4]:


import numpy as np
nwalks = 3*1000

nsteps = 3*1000

draws = np.random.randint(0, 2, size=(nwalks, nsteps)) 

steps = np.where(draws > 0, 1, -1)

walks = steps.cumsum(1)

walks
    
hits20 = (np.abs(walks) >= 20).any(1)

hits20.sum() # Number that hit 20 or -20


# In[ ]:




