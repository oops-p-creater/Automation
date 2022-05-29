import requests
from bs4 import BeautifulSoup
import pandas as pd
df=pd.read_excel(r"F:\AFO\alpinoimages.xlsx")
for i,row in df.iterrows():
    image1="https://www."+row['image1'][i]
    try:
        pageurl=image1
        source=requests.get(pageurl).text
        soup=BeautifulSoup(source,'lxml')
        imagelist=(soup.find_all('img'))
        imagelink=imagelist[0]['src']     #this [0] is because find_all() retrive a list contains all img tag
        downloaded_file = requests.get(imagelink)
        dest_file = open(fr"C:\Users\sdhak\Desktop\try\Alpino{i}_a.jpeg",'wb')
        dest_file.write(downloaded_file.content)
    except:
        pass





# pageurl='https://www.dropbox.com/s/ofzqtxrjigv3vrm/SM%20%281%29'
# # source=requests.get(pageurl).text
# soup=BeautifulSoup(source,'lxml')
# imagelist=(soup.find_all('img'))
# imagelink=imagelist[0]['src']     #this [0] is because find_all() retrive a list contains all img tag
# downloaded_file = requests.get(imagelink)
# dest_file = open(r"C:\Users\sdhak\Desktop\try\test5.jpeg",'wb')
# dest_file.write(downloaded_file.content)