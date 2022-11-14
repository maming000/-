import time
import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
import cv2
import numpy as np
from PIL import ImageGrab

def CreateWidgets():
    labelattachmentEmail = Label(root,text='存储到',font=('',10,'bold'),
                                 bg='darkslategrey')
    labelattachmentEmail.grid(row=1,column=0,pady=5,padx=5)
    root.entryattachmentEmail=Entry(root,width=30)
    root.entryattachmentEmail.grid(row=1,column=1,pady=5,padx=5)
    bu = Button(root,text='选择存放位置及名称',command=Browse,width=15)
    bu.grid(row=1,column=2,pady=5,padx=5)
    bu = Button(root,text="截图",command=Screenshot,width=10)
    bu.grid(row=2,column=1,pady=5,padx=5)
    bu = Button(root,text='指定区域截图',command=ScreenshotROI,width=10)
    bu.grid(row=2,column=2,pady=5,padx=5)


def Browse():
    root.fileName = filedialog.asksaveasfilename(title='SAVE AS',
                                                 initialdir='D:/',
                                                 defaultextension='.png',
                                                 filetypes=(("PNG fILES","*.png"),('ALL Files','*.*')))
    root.entryattachmentEmail.insert('1',root.fileName)
def Screenshot():
    root.state('icon')
    time.sleep(0.2)
    screenshot=pyautogui.screenshot()
    screenshot.save(root.fileName)

def ScreenshotROI():
    root.state('icon')
    time.sleep(0.2)
    curScreen = ImageGrab.grab()
    point1,point2 = select_roi(curScreen)
    screenshot = pyautogui.screenshot(region=(point1[0],point1[1],point2[0],point2[1]))
    screenshot.save(root.fileName)

def on_mouse(event,x,y,flags,key):
    global img,point1,point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x,y)
        cv2.circle(img2,point1,10,(0,255,0),thickness=2)
        cv2.imshow('image',img2)
    elif event ==
root = tk.Tk()
root.title('截图')
root.config(background='darkslategrey')
CreateWidgets()
root.mainloop()
