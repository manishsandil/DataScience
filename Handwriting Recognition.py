#!/usr/bin/env python
# coding: utf-8

# # Import libraries and data sets

# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.datasets import load_digits

digits = load_digits()


# # Analyze sample image

# In[10]:


import pylab as pl
pl.gray()
# pl.matshow(digits.images[6])
# pl.show()
# digits.images[6]


# In[ ]:




