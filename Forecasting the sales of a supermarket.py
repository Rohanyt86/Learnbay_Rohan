#!/usr/bin/env python
# coding: utf-8

# ## Name:- Rohan Suvarna
# 
# ## Domain:- Business Analyst
# 
# ## Bharat Intern
# 
# ## Task :- Forecasting the sales of a supermarket 

# #### Importing Libraries

# In[111]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.style.use('ggplot')
import statsmodels.api as sm
from scipy.stats import skew


# #### Load data

# In[4]:


df = pd.read_csv(r'C:\Users\ROHAN SUVARNA\OneDrive\Documents\Rohan Suvarna\Projects\Business_Analyst\train.csv',encoding = 'unicode_escape')
df


# In[5]:


#### head


# In[7]:


df.head()


# In[ ]:


### Tail


# In[8]:


df.tail()


# In[10]:


df.shape


# In[11]:


## information about the data

df.info()


# In[12]:


## null value contain

df.isnull().sum()


# In[23]:


## Postal code contain null values = 11
## Delete

df.dropna(inplace=True)


# In[24]:


df.info()


# In[26]:


df.shape


# In[27]:


## Descibe
df.describe()


# ### Exploratory Data analysis

# #### Highest product sales according to region

# In[160]:


# Group the data by 'Region' and 'Product Name' and calculate the counts
product_counts = df.groupby(['Region', 'Product Name']).size().reset_index(name='Count')

# Find the product that supplies the most in each region
idx = product_counts.groupby('Region')['Count'].idxmax()
most_supplied_products = product_counts.loc[idx]

# Create a bar plot using seaborn to visualize the most supplied products in each region
plt.figure(figsize=(10, 6))
sns.barplot(data=most_supplied_products, x='Region', y='Count', hue='Product Name')
plt.title('Most Supplied Product in Each Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.legend(title='Product Name', title_fontsize='large')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ##### here we can tell that East region consider most supply of product Staple envelope

# ### Which product has maximum sold

# In[129]:


# Group the data by 'Product Name' and calculate the total sales for each product
s = df.groupby('Product Name')['Sales'].sum().reset_index().sort_values(by = 'Sales',ascending = False).head(5)

# Find the highest product sales
highest_product_sold = s.loc[s['Sales'].idxmax()]

## Using barplot to visualize the highest sales
plt.figure(figsize=(25,10))
sns.barplot(x='Product Name', y='Sales', data=s)
plt.title('Product with Highest Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=360)
plt.tight_layout()
plt.show()


# #### Closely we can see thet Canon image CLASS 2200 Advanced copier has highest sales 

# ### Which product has minimum sold

# In[144]:


# Group the data by 'Product Name' and calculate the total sales for each product
s = df.groupby('Product Name')['Sales'].sum().reset_index().sort_values(by = 'Sales',ascending = True).head(5)

# Find the highest product sales
Lowest_product_sold = s.loc[s['Sales'].idxmin()]

## Using barplot to visualize the highest sales
plt.figure(figsize=(25,10))
sns.barplot(x='Product Name', y='Sales', data=s)
plt.title('Product with Highest Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=360)
plt.tight_layout()
plt.show()


# #### We can see that Eureka Disposable bags for sanitaire Vibra Groomer | Upright Vac has less sales

# ### Visualize sales distribution

# In[155]:


# Visualize sales distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], bins=30, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.show()


# ### Sales by Region

# In[143]:


# Group the data by 'Region' and calculate the total sales 
s = df.groupby('Region')['Sales'].sum().reset_index().sort_values(by = 'Sales',ascending = False)

# Find the highest product sales
highest_Region_sales = s.loc[s['Sales'].idxmax()]

## Using barplot to visualize the highest sales
plt.figure(figsize=(25,10))
sns.barplot(x='Region', y='Sales', data=s)
plt.title('Region with Highest Sales')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=360)
plt.tight_layout()
plt.show()


# West region contain highest sales 

# In[145]:


# Group the data by 'City' and calculate the total sales 
s = df.groupby('City')['Sales'].sum().reset_index().sort_values(by = 'Sales',ascending = False).head(5)

# Find the highest product sales
highest_City_sales = s.loc[s['Sales'].idxmax()]

## Using barplot to visualize the highest sales
plt.figure(figsize=(25,10))
sns.barplot(x='City', y='Sales', data=s)
plt.title('City with Highest Sales')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.xticks(rotation=360)
plt.tight_layout()
plt.show()


# New york city has highest sales

# In[146]:


# Group the data by 'Segment' and calculate the total sales 
s = df.groupby('Segment')['Sales'].sum().reset_index().sort_values(by = 'Sales',ascending = False).head(5)

# Find the highest Segment sales
highest_Segment_sales = s.loc[s['Sales'].idxmax()]

## Using barplot to visualize the highest sales
plt.figure(figsize=(25,10))
sns.barplot(x='Segment', y='Sales', data=s)
plt.title('Segment with Highest Sales')
plt.xlabel('Segment')
plt.ylabel('Total Sales')
plt.xticks(rotation=360)
plt.tight_layout()
plt.show()


# Highest sales made by consumer as compared to others House office and Corporate segment.

# In[100]:


df.corr()


# In[101]:


# Compute correlation matrix
correlation_matrix = df.corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[116]:


skewness_sales = df['Sales'].skew()
print("Skewness of Sales:", skewness_sales)


# - when value is not symmetric is called skeweed
# - here sales is highly Skeweed

# # Conclusion

# ##### Highest Stock to keep

# In[ ]:


- East Region has highest supply of product Staple envelope so we have to stock it up.
- Canon image CLASS 2200 Advanced copier product.


# ##### Lowest Stock to keep

# In[ ]:


- Eureka Disposable bags for sanitaire Vibra Groomer | Upright Vac porduct
- south region has less supply of Easy-staple paper


# ##### Highest Sales

# In[ ]:


- West region contain highest sales 
- New york city has highest sales
- consumer segment


# ##### Lowest sales

# In[ ]:


- East Saple Paper less sales in South region
- Hoouse office

