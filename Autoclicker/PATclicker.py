from tkinter import *
from PIL import Image, ImageTk
import threading
from pynput import keyboard
import pyautogui
import sys
import os
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()
root.title("Pogo's Autoclicker - Arhan Jain / FallDrop[ch]")
root.geometry("840x400")
icon = PhotoImage(file=resource_path(r"Fileicon.ico"))
root.iconphoto(False, icon)
root.config(bg="#363636")
root.resizable(False, False)

click_thread = None
stop_event = threading.Event()

def startclick(event=None):
    global click_thread
    global durationsecs
    global stop_event

    if click_thread is None or not click_thread.is_alive():
        cps = clickrepeat_textbox.get()
        durationsecs = 9999
        cpsfloat = float(cps)
        total_clicks = cpsfloat * durationsecs

        stop_event.clear()
        click_thread = threading.Thread(target=autoclick, args=(total_clicks, cpsfloat, stop_event))
        click_thread.start()
    else:
        print("Autoclicker is already running!")

def autoclick(total_clicks, cpsfloat, stop_event):
    start_time = time.time()

    total_clicks = int(total_clicks)

    for x in range(total_clicks):
        if stop_event.is_set():
            break
        
        pyautogui.leftClick()

        time.sleep(1 / cpsfloat)

        if time.time() - start_time >= durationsecs:
            break

def stopclick(event=None):
    global click_thread

    if click_thread is not None and click_thread.is_alive():
        stop_event.set()
        click_thread.join()
    else:
        print("Autoclicker is not running!")

def f6f5click(key, event=None):
    global click_thread
    global durationsecs
    global stop_event

    if key == keyboard.Key.f6:
        if click_thread is None or not click_thread.is_alive():
            cps = clickrepeat_textbox.get()
            durationsecs = 9999
            cpsfloat = float(cps)
            total_clicks = cpsfloat * durationsecs

            stop_event.clear()
            click_thread = threading.Thread(target=autoclick, args=(total_clicks, cpsfloat, stop_event))
            click_thread.start()
        else:
            print("Autoclicker is already running!")

    if key == keyboard.Key.f5:
        if click_thread is not None and click_thread.is_alive():
            stop_event.set()
            click_thread.join()
        else:
            print("Autoclicker is not running!")

def listenf6f5event():
    with keyboard.Listener(on_press=f6f5click) as listener:
        listener.join()

key_listener_thread = threading.Thread(target=listenf6f5event)
key_listener_thread.daemon = True
key_listener_thread.start()

img = Image.open(resource_path("Falldropchicon.png"))
img = img.resize((840, 200), Image.ANTIALIAS)   
nameiconprocessing = ImageTk.PhotoImage(img)
nameicon_label = Label(root, image=nameiconprocessing)
nameicon_label.pack()

repeat_text = Label(root, text="No. of clicks to repeat per second:", font=("Britannic Bold", 15), fg="White", bg="#363636")
repeat_text.place(x=10, y=210)

clickrepeat_textbox = Entry(root, font=("Arial", 15), fg="White", bg="Grey")
clickrepeat_textbox.place(x=10, y=250)

Start_btn = Button(root, font=("Britannic Bold", 30), text="START AUTOCLICKING (F6)", fg="White", bg="#3e7532", command=startclick)
Start_btn.place(x=330, y=210)

Stop_btn = Button(root, font=("Britannic Bold", 30), text="STOP AUTOCLICKING (F5)", fg="White", bg="#324363", command=stopclick)
Stop_btn.place(x=330, y=300)

root.mainloop()
