#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis on Automobile Dataset

# ### Import relevant libraries and define settings for plotting.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


#Importing Data

data=pd.read_csv(r"C:\Users\chila\OneDrive - Lovely Professional University\Documents\Gowtham\Finger tips\Python\Pandas\Pandas Live Project\Source Files\EDA Automobile Project16938333210.csv")

data.head()


# In[3]:


data.info()


# # Data Cleaning

# In[4]:


data["normalized-losses"]=data["normalized-losses"].replace("?",np.nan)


# In[5]:


data["normalized-losses"].value_counts().head()


# In[6]:


data["normalized-losses"].isnull().sum()


# In[7]:


mean=data[data["normalized-losses"]!=np.nan]["normalized-losses"].astype("float").mean()


# In[8]:


data["normalized-losses"]=data["normalized-losses"].fillna(mean)


# In[9]:


data.head()


# In[10]:


data["normalized-losses"]=data["normalized-losses"].astype(int)
data["normalized-losses"].info()


# In[11]:


pd.set_option("display.max_columns",None)
data.head()


# In[12]:


np.round(data[data["bore"]!="?"]["bore"].astype(float).mean(),2)


# In[13]:


data["bore"]=data["bore"].replace("?",3.33)
data[data["bore"]==3.33]


# In[14]:


data["bore"]=data["bore"].astype(float)
data["bore"].dtype


# In[15]:


data["horsepower"].unique()
data["stroke"].unique()


# In[16]:


a=np.round(data[data["horsepower"]!="?"]
           ['horsepower'].astype(int).mean())
b=round(data[data["stroke"]!="?"]
        ["stroke"].astype(float).mean(),2)


# In[17]:


data[["horsepower","stroke"]]=data[["horsepower","stroke"]].replace("?",{"horsepower":a,"stroke":b})


# In[18]:


data=data.astype({"horsepower":int,"stroke":float})
data[["horsepower","stroke"]].info()


# In[19]:


data["peak-rpm"]=data["peak-rpm"].replace("?",round(data[data["peak-rpm"]!="?"]
                      ['peak-rpm'].astype(int).mean()))
data["peak-rpm"]=data["peak-rpm"].astype(int)


# In[20]:


data["peak-rpm"].dtype 


# In[21]:


data["price"]=pd.to_numeric(data["price"],errors='coerce')
data["price"].unique()


# In[22]:


data["price"]=data["price"].replace(np.nan,round(data[data["price"]!=np.nan]["price"].mean()))


# In[23]:


data["price"]=data["price"].astype(int)
data["price"].info()


# In[24]:


data["drive-wheels"].unique()


# In[ ]:





# # Univariate Analysis

# Univariate analysis is the simplest form of analyzing data. “Uni” means “one”, so in other words your data has only one variable. It doesn't deal with causes or relationships (unlike regression ) and it's major purpose is to describe; It takes data, summarizes that data and finds patterns in the data.

# # Vehicle by make frequency diagram

# In[25]:


plt.figure(figsize=[15,5])
data["make"].value_counts().nlargest(5).plot(kind="bar")
plt.xlabel("Company",color="blue",fontsize=19)
plt.xticks(rotation=360,fontsize=15)
plt.ylabel("No.of Cars",color="green",fontsize=19)
plt.yticks(fontsize=15)
plt.title("Vehicle by make frequency diagram",fontsize=20)
plt.show()


# # Pricing Histogram

# In[26]:


data.hist(column="price",bins=6,color="m")


# In[27]:


data.hist(column="horsepower",bins=5)


# In[28]:


data.hist(column="normalized-losses",bins=5,color="g")


# # histogram for all columns

# In[29]:


data.hist(figsize=[25,30])


# # Bar plot for Fuel type

# In[30]:


sns.countplot(x="fuel-type",data=data)


# # Drive wheels count plot

# In[31]:


sns.countplot(x="drive-wheels",data=data)


# In[32]:


sns.countplot(x="engine-type",data=data)


# # find the correlation of columns with each other

# In[33]:


data.info()


# In[34]:


acorr=data[["symboling","normalized-losses","curb-weight","engine-size","horsepower","peak-rpm","city-mpg","highway-mpg","wheel-base","length","width","height","bore","stroke","compression-ratio","price"]].corr()


# In[35]:


sns.heatmap(acorr)


# # Bivariate Analysis

# Bivariate analysis is one of the simplest forms of quantitative (statistical) analysis. It involves the analysis of two variables (often denoted as X, Y), for the purpose of determining the empirical relationship between them.

# # Make a boxplot for make and price

# In[36]:


plt.figure(figsize=[30,20])
sns.boxplot(x="make",y="price",data=data)


# # make a boxplot for horsepower and price

# In[37]:


plt.figure(figsize=[30,20])
sns.boxplot(x="horsepower",y="price",data=data)


# # display a distrubation of price

# In[38]:


sns.distplot(data["price"])

print('This distribution has skew', data['price'].skew())
print('This distribution has kurtosis', data['price'].kurt())


# # Distrubation of curb-weight

# In[39]:


sns.distplot(data["curb-weight"])

print('This distribution has skew', data["curb-weight"].skew())
print('This distribution has kurtosis', data["curb-weight"].kurt())


# # Scatter plot of price and engine size

# In[42]:


sns.lmplot(x='price',y="engine-size",data=data);


# # Scatter plot of price and highway-mpg

# In[44]:


sns.lmplot(x="price",y="highway-mpg",data=data)


# # Scatter plot of City and Highway MPG, Curb weight based on Make of the car

# In[48]:


sns.relplot(x= "highway-mpg" ,y="curb-weight",hue="make",data=data)


# In[50]:


sns.lmplot(x='city-mpg',y="curb-weight", data=data, hue="make", fit_reg=False)


# # Drive wheels and City MPG bar chart

# In[51]:


data.groupby('drive-wheels')['city-mpg'].mean().plot(kind='barh', color = 'blue')
plt.title("Drive wheels City MPG")
plt.ylabel('City MPG')
plt.xlabel('Drive wheels');


# # Drive wheels and Highway MPG bar chart

# In[52]:


data.groupby('drive-wheels')['city-mpg'].mean().plot(kind='bar', color = 'g')
plt.title("Drive wheels City MPG")
plt.ylabel('City MPG')
plt.xlabel('Drive wheels');


# # Normalized losses based on body style and no. of doors

# In[53]:


pd.pivot_table(data,index=['body-style','num-of-doors'], values='normalized-losses').plot(kind='bar',color='orange')
plt.title("Normalized losses based on body style and no. of doors")
plt.ylabel('Normalized losses')
plt.xlabel('Body style and No. of doors');


# # Profits based on body style and no. of doors

# In[55]:


pd.pivot_table(data,index=['body-style','num-of-doors'], values='price').plot(kind='barh',color='m')
plt.title("Profits based on body style and no. of doors")
plt.ylabel('Body style and No. of doors')
plt.xlabel('Price');

