from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("ClickrCounter")
root.config(background="Black")

ClickCount = 0

ClickCountShow = Label(root, text=f"You have clicked {ClickCount} times", bg="Black", fg="White", font=("ROG Fonts", 17))
ClickCountShow.pack()

def IncreaseClickCount():
    global ClickCount
    ClickCount += 1
    ClickCountShow.config(text=f"You have clicked {ClickCount} times")

ClickBtn = Button(root, text="Click Me!", fg="White", bg="#212020", font=("Script MT Bold", 30),width=100, height=50, command=IncreaseClickCount)
ClickBtn.pack(padx=30, pady=20)

root.mainloop()
root.quit