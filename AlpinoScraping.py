#!/usr/bin/env python 
#coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import smtplib


# In[2]:


db=pd.read_excel(r"F:\AFO\alpino\Book 2.xlsx")


# In[3]:


links=db['Product Link on brand website']


# In[4]:


for x,link in enumerate(links):
    link=str(link)
    try:
        source=requests.get(link).text
        soup= BeautifulSoup(source,'lxml')
        try:
            price=soup.find('span',class_='ProductMeta__Price Price Price--compareAt Text--subdued u-h4').text
            db.loc[x,['MRP']]=price.split('. ')[1]
        except:
            db.loc[x,['MRP']]=0
        try:
            saleprice=soup.find('span',class_='ProductMeta__Price Price Price--highlight Text--subdued u-h4').text            
            db.loc[x,['SALEPRICE']]=saleprice.split('. ')[1]
        except:
            db.loc[x,['SALEPRICE']]=0
            
    except:
        pass


# In[5]:


db['SALEPRICE']=db['SALEPRICE'].astype('int64')


# In[6]:


for index, row in db.iterrows():
    a=row['OURPRICE']
    b=row['SALEPRICE']
    if b<a:
        
        EMAIL_ADRESS='pricealert.afo@gmail.com'
        EMAIL_PASSWORD='strongertogether'
    

        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
    
    
            smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
            subject='price alert'
            body=str(row['PRODUCT_ID'])+"link: " + row['Product Link on brand website']+'\n our price' +str(row['OURPRICE'])+'\n their price'+str(row['SALEPRICE'])
            msg = f'Subject:{subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADRESS,'pricealert.afo@gmail.com',msg)
    elif b==0 and a==0:
        EMAIL_ADRESS='pricealert.afo@gmail.com'
        EMAIL_PASSWORD='strongertogether'
    

        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
    
    
            smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
            subject='PRODUCT MISSING'
            body=str(row['PRODUCT_ID'])+"link: " + row['Product Link on brand website']
            msg = f'Subject:{subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADRESS,'pricealert.afo@gmail.com',msg)


# In[7]:


db.to_excel(r"F:\AFO\alpino\Book 2.xlsx",index=False)


# In[ ]:




