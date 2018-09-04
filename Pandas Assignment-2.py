
# coding: utf-8

# In[1]:


import pandas as pd

Baby_Names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
Baby_Names.info()


# In[2]:


# Delete Unnamed columns.

del Baby_Names['Unnamed: 0']
del Baby_Names['Id']

Baby_Names.head()


# In[27]:


# Show the distribution of male and female

Baby_Names['Gender'].value_counts()


# In[12]:


# What is the median name occurence in the dataset

names[names.Count == names.Count.median()]


# In[23]:


# 5. Distribution of male and female born count by states

counts = Baby_Names.groupby(['Gender', 'State', 'Year']).count()
counts

