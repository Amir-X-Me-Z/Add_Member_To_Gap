# import platform
# from colorama import *
# system = platform.uname()
# prapertis = Fore.GREEN+f'''
# System Name >>> {Fore.RED+system[0]+Fore.GREEN}
# Node >>> {Fore.RED+system[1]+Fore.GREEN}
# Release >>> {Fore.RED+system[2]+Fore.GREEN}
# Version >>> {Fore.RED+system[3]+Fore.GREEN}
# Machine >>> {Fore.RED+system[4]+Fore.WHITE}
# '''
# print(prapertis)


# 
# from random import *
# a = range(10000, 10100)
# for x in a :
    # r = choice(['a','b','c','e','f','g'])
    # print(r + str(x) + r)


# from moviepy.video.io.VideoFileClip import VideoFileClip
from base64 import encode
from glob import escape
from msilib import sequence
from pickletools import pyfloat
from unicodedata import name
from moviepy.editor import *
from numpy import insert
import outcome
import os
from gtts import gTTS
from playsound import playsound
import os
import sqlite3
from pytube import *
from pyparsing import identchars
from PIL import Image
import pytesseract
import random 
from colorama import *
from pyfiglet import Figlet
init()
# if not os.path.isfile('users.txt'):
# 	open('users.py','a')
	

# with open('users.txt','a+') as file:
# 	for i in range(10):
# 		file.write(f'{i}\n')
# with open('users.txt','r+') as file:
# 	for x in file:
# 		print(x)

#   python 3 escape sequences

#  استخراج متن انگلیسی از عکس
# img = Image.open('photo.png')
# pytesseract.pytesseract.tesseract_cmd = r"D:\\photo to text\\Tesseract-OCR\\tesseract.exe"
# result = pytesseract.image_to_string(img,lang='eng+fas')
# with open('photo to text.txt',mode='w' , encoding='utf-8') as file :
# 	file.write(result)
# 	print(result)








#  ساخت پسورد لیست 

# lengths = int(input('enter number 1 >>> '.title()))
# counts = int(input('enter number 2 >>> '.title()))
# def password(length:int = 8, count:int = 100):
#     s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789'
#     generated_password = ""
#     for i in range(count):
#         generated_password += "".join(random.choices(s , k=length)) + "\n"
#     return generated_password
# f = password(lengths ,counts)
# with open('pass.txt','a+') as file:
# 	file.write(f'{f}\n')



# digital 




figlett = Figlet(font='term')
textt = figlett.renderText('send [ run ] in telegram : '.title())
print(Fore.GREEN + textt)



#  تبدیل متن به صدا
# music ='Amir.mp3'
# language = 'ar'
# spik = gTTS(text='felan shab bekheyr',lang = language , slow= True)
# spik.save(music)
# playsound(music)




