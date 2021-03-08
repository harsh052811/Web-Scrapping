#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[114]:


import bs4, requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[115]:


webpage = "https://www.flipkart.com/search?q=phones&otracker=search&marketplace-FLIPKART&as-show-Don&as-off"


# In[116]:


fetch_url =urlopen(webpage)


# In[118]:


page_html = fetch_url.read()


# In[117]:


soup = BeautifulSoup(page_html,"html.parser")


# In[119]:


print(soup.prettify())


# In[120]:


phones= soup.findAll("div",{'class':'_4rR01T'})


# In[121]:


phones
len(phones)


# In[122]:


phone_list=[]


# In[123]:


for i in range(0,len(phones)):
    phone_list.append(phones[i].text.strip())


# In[124]:


phone_list


# In[125]:


prices=soup.findAll('div',{'class':'_30jeq3 _1_WHN1'})


# In[133]:


prices


# In[134]:


prices_list=[]


# In[136]:


for i in range(0,len(prices)):
    prices_list.append(prices[i].text.strip())


# In[137]:


prices_list



# In[141]:


print(len(prices_list))


# In[142]:


print(len(phone_list))


# In[145]:



for i in range(0,20):
    print(prices_list[i],'-',phone_list[i])


# In[150]:


data=pd.DataFrame(list(zip(prices_list,phone_list)),columns=['Prices','Phone_Name'])


# In[151]:


data


# In[152]:


file_name='Price.xlsx'
data.to_excel(file_name)


# In[ ]:




