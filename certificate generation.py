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
    
hello_world()