#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


car =pd.read_csv(r"C:\Users\Chaitanya\Downloads\Cars Data1.csv")


# In[16]:


#  Always Analyze data first
# .head() command shows first N rows of data (by default t shows 5) 
car.head()


# In[17]:


#shape - It shows the total no. of rows and no. of columns of the dataframe
car.shape


# In[18]:


#Now check if there are any Null values in dataset (If there is any null value in any column,then fill it with mean of that column.)
car.isnull().sum()


# In[21]:


#fillna() - To fill the null values of a column with some particular value. For cylinders we will fill null valules wth mean
car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)


# In[22]:


car.isnull().sum()


# In[24]:


# Check what are the different types of Make are there in our dataset. And, what is the count of each Make in the data?
car['Make'].value_counts()


# In[27]:


#Show all the records where Origin is Asia or Europe.
car[car['Origin'].isin(['Asia','Europe'])]


# In[30]:


#Removing unwanted records - Remove all the records (rows) where Weight is above 4000.
car[~(car['Weight']> 4000)]


# In[31]:


#Instruction ( Applying function on a column ) - Increase all the values of 'MPG_City' column by 3.
car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)


# In[32]:


car


# In[ ]:




