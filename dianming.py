import random
import linecache
import tkinter as tk

window = tk.Tk()
window.title('窗口标题')
window.geometry('300x300')
text1 = tk.Text(window, width=30, height=10, bg='grey', font=('Arial', 12))
text1.grid(row=0,rowspan=1,column=1)
#scroll = tk.Scrollbar()
#scroll.grid(column=2)
#scroll.config(command=text1.yview)
#text1.config(yscrollcommand=scroll.set)


    #file = open(file='1.txt',mode='r+',encoding='utf-8')
def xianshi():
    with open(file='1.txt', mode='r+', encoding='utf-8') as f:
        count = len(f.readlines())
        co = random.randint(1, count)
        print(co)
    bianliang=linecache.getline('1.txt',co)
    text1.insert('1.0',bianliang)
def clear():
    text1.delete('1.0',tk.END)

b=tk.Button(text='选择',command=xianshi)
b.grid(row=2,column=1,columnspan=1)
b1=tk.Button(text='清除',command=clear)
b1.grid(row=2,column=2)
window.mainloop()
