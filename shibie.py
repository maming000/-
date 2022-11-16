
#encoding:utf-8
import requests
import base64
from tkinter import *
from PIL import ImageGrab
import pyperclip

import requests
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=wgEHks0l6MCpalbs3lPuFX1U&client_secret=Z4Rn4ghBx9k06fUYPmSEIRbCFvWFxLyQ'
response = requests.get(host)
if response:
    print(response.json()['access_token'])

window = Tk()
window.title('qcc-tnw')
window.geometry('400x600')
l = Label(window,text='调用')
l.pack()
E1 = Text(window,width='100',height='100')

def imgde():
    image = ImageGrab.grabclipboard()
    s = 'xxx.png'
    image.save(s)
    request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
    f = open(s,'rb')
    img = base64.b64encode(f.read())
    params = {'image':img}
    access_token = 'xxxxxxx'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencode'}
    response = requests.post(request_url,data=params,headers=headers)
    if response:
        for i in response.json()['words_result']:
            E1.insert('insert',i['words']+ '\n')
            E1.pack(side=LEFT)
        pyperclip.copy(E1.get('1.0','end'))

img_txt = Button(window,text='文字识别',width=15,height=1,command=imgde)
cut_en = Button(window,text='英文分割',width=15,height=1)
cut_cn = Button(window,text='中文分割',width=15,height=1)
img_txt.pack(anchor="nw")
cut_en.pack(anchor='nw')
cut_cn.pack(anchor='nw')
window.wm_attributes('-topmost',1)
window.mainloop()
