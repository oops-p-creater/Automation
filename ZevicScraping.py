#!/usr/bin/env python
# coding: utf-8

# In[33]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import smtplib


# In[34]:


db=pd.read_excel(r"F:\AFO\zevic\zevic.xlsx")


# In[36]:


links=db['Product Link on brand website']


# In[38]:


for x,link in enumerate(links):
    
    try:
        link=str(link)
        source=requests.get(link).text
        soup= BeautifulSoup(source,'lxml')
        try:
            price=soup.find('span',class_='ProductMeta__Price Price Text--subdued u-h4').text
            db.loc[x,['MRP']]=price.split('. ')[1]
        except:
            db.loc[x,['MRP']]=0
        try:
            saleprice=soup.find('span',class_='ProductMeta__Price Price Text--subdued u-h4').text            
            db.loc[x,['SALEPRICE']]=saleprice.split('. ')[1]
        except:
            db.loc[x,['SALEPRICE']]=0
            
    except:
        pass


# In[39]:


db['MRP']=db['MRP'].fillna(0)
db['SALEPRICE']=db['SALEPRICE'].fillna(0)
db['Product Link on brand website']=db['Product Link on brand website'].fillna('NA')
db['OURPRICE']=db['OURPRICE'].fillna(0)


# In[40]:


db['SALEPRICE']=db['SALEPRICE'].astype('int64')
db['MRP']=db['MRP'].astype('int64')


# In[41]:


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
            body=str(row['PRODUCT_ID'])+" link: " + row['Product Link on brand website']+'\n our price' +str(row['OURPRICE'])+'\n their price'+str(row['SALEPRICE'])
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
            body=str(row['PRODUCT_ID'])+" link: " + row['Product Link on brand website']
            msg = f'Subject:{subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADRESS,'pricealert.afo@gmail.com',msg)
        


# In[32]:


db.to_excel(r"F:\AFO\zevic\zevic.xlsx",index=False)


# In[ ]:




