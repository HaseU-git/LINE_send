#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import tkinter
from tkinter import messagebox
import pyautogui
import send_message_on_whatsapp

    

def btn_click():
    index = 0 
    friend_list = friend_list_entry.get().splitlines()
    temp_message_list = message_list_entry.get().splitlines()
    image_list = image_list_entry.get().splitlines()
    message_flag = message_list_entry.get() != ""
    image_flag = image_list_entry.get() != ""

    message_list = []
    for i in temp_message_list:
        message_list.append(i.replace('\\n', '\n'))

    send_message_on_whatsapp.launch_whatsapp()

    while index < len(friend_list):
        if message_flag:
            send_message_on_whatsapp.send_message(friend_list[index], message_list[index])
        if image_flag:
            send_message_on_whatsapp.send_photo(friend_list[index], image_list[index])
        index = index + 1
    pyautogui.hotkey('command', 'tab')
    messagebox.showinfo("終了報告", "全ての送信が完了しました")

    
root = tkinter.Tk()
root.title(u"WhatsApp send bulk")
root.geometry("300x300")

iconfile = 'send.png'
img = tkinter.Image("photo", file=iconfile)
root.iconphoto(True, img)


lbl = tkinter.Label(text='To')
lbl.place(x=30, y=50)

friend_list_entry = tkinter.Entry(width=20)
friend_list_entry.place(x=85, y=50)

lbl = tkinter.Label(text='Content')
lbl.place(x=30, y=110)

message_list_entry = tkinter.Entry(width=20)
message_list_entry.place(x=85, y=110)

lbl = tkinter.Label(text='Image')
lbl.place(x=30, y=170)

image_list_entry = tkinter.Entry(width=20)
image_list_entry.place(x=85, y=170)

btn = tkinter.Button(root, text='send', command=btn_click)
btn.place(x=120, y=230)

root.mainloop()
