"""ON BOARDING """
import pandas as pd
import requests
raw_sheet=pd.read_excel("Virtualthon5.0 master file.xlsx",sheet_name=None)
id_mapping=#SHEET PROVIDED BY EVENT ORGANISERS
#THESE ARE THE MULTIPLE SHEETS IN EXCEL FILE"""

Cycling_10k=raw_sheet['C10km']
category1=list(Cycling_10k['BiB no'])

Cycling_20k=raw_sheet['C20km']
category2=list(Cycling_20k['BiB no'])

Cycling_30k=raw_sheet['C30km']
category3=list(Cycling_30k['BiB no'])

Cycling_50k=raw_sheet['C50km']
category4=list(Cycling_50k['BiB no'])

Running_3k=raw_sheet['R3km']
category5=list(Running_3k['BiB no'])

Running_5k=raw_sheet['R5km']
category6=list(Running_5k['BiB no'])

Running_10k=raw_sheet['R10km']
category7=list(Running_10k['BiB no'])

Running_21k=raw_sheet['R21km']
category8=list(Running_21k['BiB no'])

#CATEGORY OF SQUADS"""

category1_s="1623734567074x842999054625669100"
category2_s="1623734611208x451137453131825150"
category3_s="1623734634733x491264190486413300"
category4_s="1623734651982x902013945816023000"
category5_s="1623734377310x522183617668448260"
category6_s="1623734463842x316824686075838460"
category7_s="1623734488039x980440836872077300"
category8_s="1623734514523x939376673736622100"

#CALL API AND CHANGE CATEGORY AND SQUAD AD PER AS NEED
#BELOW FUNCTION WILL ADD MEMBERS TO THEIR RESPECTIVE CATEGORY SQUADS

for j,i in enumerate(category1):
    try:
        print(i)
        id_mapping.loc[i]['unique id']
        id_mapping.at[i,'bool']="true"
        ID=id_mapping.loc[i]['unique id']    
        ID=str(ID)
        print(ID)
        #parentSquadMemberList.remove(ID)
        status=requests.post("https://us-central1-fitnet-dc799.cloudfunctions.net/requestActionSquad",data={'userID':'1618066353393x979895929116008300',
                                                                                                                'memberID':ID,
                                                                                                                'action':"ADD_MEMBER",
                                                                                                                'squadID':category1_s})
        
        print(status)
        print(ID)
        Cycling_10k.at[j,'bool']="True" 
    except:
        
        Cycling_10k.at[j,'bool']="False"
        
        
"""ADD MANUAL ACTIVITY"""


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
for i in df.iterrows():
    bib=str(i[1]['BIB '])
    
    if bib.startswith("C10"):
        distance=10000
        activityType="Cycling"
    if bib.startswith("C20"):
        distance=20000
        activityType="Cycling"
    if bib.startswith("C30"):
        distance=30000
        activityType="Cycling"
    if bib.startswith("C50"):
        distance=50000
        activityType="Cycling"
    if bib.startswith("R3"):
        distance=3000
        activityType="Running"
    if bib.startswith("R5"):
        distance=5000
        activityType="Running"
    if bib.startswith("R10"):
        distance=10000
        activityType="Running"
    if bib.startswith("R21"):
        distance=21000
        activityType="Running"
    
    duration=i[1]['Time']
    duration_in_sec=get_sec(str(duration))*1000
    
    userid=i[1]['id']
    
    if userid!=0:
        status=requests.post("https://us-central1-fitnet-dc799.cloudfunctions.net/addManualActivity",data={'userID':userid,
                                                                                                            "activityType":activityType,
                                                                                                            "activityStartDate":234567,
                                                                                                        "activityEndDate":123456,
                                                                                                     "duration":duration_in_sec,
                                                                                                   "distance":distance,
                                                                                                      "eventID":"1623734251296x340782449447665660"
                                                                                                          })
        print(status)
        
        
    
"""NOTIFICATION"""
for i in l:
    data={
    "userID":i,
    "title": "Your VIRTUALTHON 5.0 certificate is ready!",
    "body":"open event's page to view, save and share your certificate...",
    "action":"125468",
    "type":"message",
    "image":"https://beta.twidapp.com/pub/media/brand_images/Cult_Fit_1.png",
    "banner":"https://s3.amazonaws.com/appforest_uf/f1623735218388x279613265698298600/BRAND%20CIRCUS%20EVENT.jpeg"
    }

    status=requests.post("https://us-central1-fitnet-dc799.cloudfunctions.net/pushNotification",data)
    print(status)
    sleep(0.3)


""""EMAIL"""
import imghdr
import smtplib
from email.message import EmailMessage
import time
from time import sleep

for i in e:
    msg = EmailMessage()
    msg.set_content("""\
        
Hi,

Please find your Virtualthon 5.0 certificate attached.
    
Make your friends and close ones fit by inviting them on afo. 
    
https://afo.page.link/virtualthon
    
Best
Team afo
        """)
    name=d[i]
    print(i)
    name=name.upper()
    print(name)
    with open(fr'C:\Users\sdhak\Desktop\demo\{name}.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = "afoCertificate"
    msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    msg['Subject'] = 'Virtualthon 5.0 Certificate'
    msg['From'] = "SENDER@EMAIL"
    msg['To'] = i

    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("SENDER@EMAIL", "PASSWORD")
    server.send_message(msg)
    print("Success")
    sleep(0.3)
    server.quit()
    

"""CERTIFICATE"""

#CREATE AND ITER IN DATA FRAME AND CALL API
for i in a1.iterrows():
    duration=i[1][0]['Duration']
    name=i[1][6]
    types="Cycling"
    activity="10 KM IN"
    userid=i[0]
    status=requests.post(f"https://us-central1-afo-dev-53e39.cloudfunctions.net/certificateGenerator?name={name}&duration={duration}&type={types}&activity={activity}")
    print(status)
    res=requests.post("https://us-central1-fitnet-dc799.cloudfunctions.net/saveCertificate",data={"id":userid,
                                                                                               "certificate":status.json()['url']})
    print(res)
    
###CERTIFICATE FUNCTION###
import requests
import io
from base64 import encodebytes
from PIL import Image,ImageDraw,ImageFont
import base64
import string
import random
def CERTIFICATE():
    
    a='cyclothon'
    b="marathon"
    text_color = (0,0,0)
    raw_certificate=Image.open(fr"C:\Users\sdhak\Desktop\certificate\{b}.png")
    d = ImageDraw.Draw(raw_certificate)
    name="VENKATESH PRABHU DESAI"
    name=name.upper()
    n=len(name)
    n=n//2
    n=n*64
    
    name_location = (1241-n, 1924)
    activity="21 KM IN"
    duration="01:54:00"
    font = ImageFont.truetype("arial.ttf", 96)
    font_a = ImageFont.truetype("arial.ttf", 64)  
    
    duration_location = (1230, 2220)
    activity_location = (940,2220)
    
    
    d.text(name_location, name, fill = (202,38,62), font = font,stroke_width=2,stroke_fill=(202,38,62))
    d.text(duration_location, duration, fill = text_color, font = font_a,stroke_width=2,stroke_fill="black")
    d.text(activity_location, activity, fill = text_color, font = font_a,stroke_width=2,stroke_fill="black")
    
    
    raw_certificate.save(fr"C:\Users\sdhak\Desktop\demo\{name}.png")
    


"""ALPINO SCRAPPING"""
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



"""ALPINO IMAGES SCRAPPING"""
for i,row in df.iterrows():
    image1="https://www."+row['image1']
    try:
        path=fr"F:\AFO\alpino\Alpino{i+1}"
        os.mkdir(path)
        source=requests.get(image1).text
        soup=BeautifulSoup(source,'lxml')
        imagelist=(soup.find_all('img'))
        imagelink=imagelist[0]['src']    
        downloaded_file = requests.get(imagelink)
        dest_file = open(fr"F:\AFO\alpino\Alpino{i+1}\Alpino{i+1}_a.jpeg",'wb')
        dest_file.write(downloaded_file.content)
    except:
        pass
for i,row in df.iterrows():
    image2="https://www."+row['image2']
    try:
        source=requests.get(image2).text
        soup=BeautifulSoup(source,'lxml')
        imagelist=(soup.find_all('img'))
        imagelink=imagelist[0]['src']     #this [0] is because find_all() retrive a list contains all img tag
        downloaded_file = requests.get(imagelink)
        dest_file = open(fr"F:\AFO\alpino\Alpino{i+1}\Alpino{i+1}_b.jpeg",'wb')
        dest_file.write(downloaded_file.content)
    except:
        pass
    image3="https://www."+row['image3']
for i,row in df.iterrows():
    try:
        source=requests.get(image3).text
        soup=BeautifulSoup(source,'lxml')
        imagelist=(soup.find_all('img'))
        imagelink=imagelist[0]['src']     #this [0] is because find_all() retrive a list contains all img tag
        downloaded_file = requests.get(imagelink)
        dest_file = open(fr"F:\AFO\alpino\Alpino{i+1}\Alpino{i+1}_c.jpeg",'wb')
        dest_file.write(downloaded_file.content)
    except:
        pass


