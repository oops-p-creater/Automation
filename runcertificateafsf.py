import requests
import io
from base64 import encodebytes
from PIL import Image,ImageDraw,ImageFont
import base64
import string
import random
def hello_world():
    
    a='cyclothon'
    b="marathon"
    text_color = (0,0,0)
    non="https://s3.amazonaws.com/appforest_uf/f1629714724389x802483215518820900/certi1.jpeg"
    run="https://s3.amazonaws.com/appforest_uf/f1629714762787x357958061278619260/certi2.jpeg"
    ride="https://s3.amazonaws.com/appforest_uf/f1629714825076x921700129227513100/certi3.jpeg"
    
    raw_certificate=Image.open(fr"C:\Users\sdhak\Desktop\AFSF2\certi2.jpeg")
    d = ImageDraw.Draw(raw_certificate)
    name="shivam dhakad"
    name=name.upper()
    n=len(name)
    n=n//2
    n=n*16
    activity="10"
    name_location = (512-n, 374)
    font = ImageFont.truetype("arial.ttf", 24)
    font_a = ImageFont.truetype("arial.ttf", 16)  
    
    duration_location = (1230, 2220)
    activity_location = (600,460)
    
    
    d.text(name_location, name, fill = (0,0,0), font = font,stroke_width=1,stroke_fill=(0,0,0))
    #d.text(duration_location, duration, fill = text_color, font = font_a,stroke_width=2,stroke_fill="black")
    d.text(activity_location, activity, fill = (0,0,0), font = font_a,stroke_width=1,stroke_fill=(0,0,0))
    
    raw_certificate.show()
    raw_certificate.save(fr"C:\Users\sdhak\Desktop\AFSF2\{name}.png")
    
hello_world()