from tkinter import *
from tkinter import Menu
from tkinter import filedialog, messagebox

# Basic App Config

root = Tk()
root.geometry("1280x720")
root.title("Notepad App in Python by Arhan Jain")
root.config(bg="#212121")

# App Functionality

def OpenFile():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            WritingArea_Text.delete('1.0', END)
            WritingArea_Text.insert(END, file.read())

def QuestionSaveFile():
    if current_file_path:
        with open(current_file_path, 'w') as file:
            file.write(WritingArea_Text.get('1.0', END))
    else:
        QuestionSaveAsFile()

def QuestionSaveAsFile():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(WritingArea_Text.get('1.0', END))
        global current_file_path
        current_file_path = file_path

def QuestionSaveFileOnClose():
    if len(WritingArea_Text.get('1.0', END)) > 1:
        response = messagebox.askyesnocancel("You are forgetting something", "Please make sure you save this file")
        if response is True:
            QuestionSaveFile()
        elif response is None:
            return
    root.destroy()

def ExitApp():
    root.destroy()

def UndoAction():
    global undo_stack, redo_stack, ignore_changes
    if len(undo_stack) > 1:
        ignore_changes = True
        redo_stack.append(undo_stack.pop())
        WritingArea_Text.delete("1.0", END)
        WritingArea_Text.insert(END, undo_stack[-1])
        ignore_changes = False

def RedoAction():
    global undo_stack, redo_stack, ignore_changes
    if redo_stack:
        ignore_changes = True
        undo_stack.append(redo_stack.pop())
        WritingArea_Text.delete("1.0", END)
        WritingArea_Text.insert(END, undo_stack[-1])
        ignore_changes = False

undo_stack = [""]
redo_stack = []
ignore_changes = False

def CopyText():
    text = WritingArea_Text.get("sel.first", "sel.last")
    root.clipboard_clear()
    root.clipboard_append(text)

def CutText():
    text = WritingArea_Text.get("sel.first", "sel.last")
    root.clipboard_clear()
    root.clipboard_append(text)
    WritingArea_Text.delete("sel.first", "sel.last")

def PasteText():
    text = root.clipboard_get()
    WritingArea_Text.insert("insert", text)

def OnKeyPress(event):
    global undo_stack, redo_stack, ignore_changes
    if not ignore_changes:
        redo_stack = []
        undo_stack.append(WritingArea_Text.get("1.0", END))

current_file_path = None
root.protocol("WM_DELETE_WINDOW", QuestionSaveFileOnClose)

# App Design

TopMenuBar = Menu(root, background="#3d3d3d", foreground="#3d3d3d", activebackground="#3d3d3d",
                  activeforeground="#3d3d3d")
root.config(menu=TopMenuBar)

TopMenuBar_File = Menu(TopMenuBar, tearoff=0, background="#3d3d3d", foreground="White",
                       activebackground="#3d3d3d", activeforeground="White")

OpenMenu = TopMenuBar_File.add_command(label="Open File (Ctrl+O)", font = 50, command=OpenFile)
CloseMenu = TopMenuBar_File.add_command(label="Close File (Ctrl+W)", font = 50, command=QuestionSaveFileOnClose)
SaveMenu = TopMenuBar_File.add_command(label="Save File (Ctrl+S)", font = 50, command=QuestionSaveFile)
SaveAsMenu = TopMenuBar_File.add_command(label="Save File as (Ctrl+Shift+S)", font = 50, command=QuestionSaveAsFile)
ExitMenu = TopMenuBar_File.add_command(label="Exit Arhan's notepad (Alt+F4)", font = 50, command=ExitApp)

TopMenuBar_Edit = Menu(TopMenuBar, tearoff=0, background="#3d3d3d", foreground="White",
                        activebackground="#3d3d3d", activeforeground="White")

UndoMenu = TopMenuBar_Edit.add_command(label="Undo (Ctrl+Z)", font = 50, command=UndoAction)
RedoMenu = TopMenuBar_Edit.add_command(label="Redo (Ctrl+Y)", font = 50, command=RedoAction)
CopyMenu = TopMenuBar_Edit.add_command(label="Copy text (Ctrl+C)", font = 50, command=CopyText)
CutMenu = TopMenuBar_Edit.add_command(label="Cut text (Ctrl+X)", font = 50, command=CutText)
PasteMenu = TopMenuBar_Edit.add_command(label="Paste Text (Ctrl+V)", font = 50, command=PasteText)

TopMenuBar_Preferences = Menu(TopMenuBar, tearoff=0, background="#3d3d3d", foreground="White",
                       activebackground="#3d3d3d", activeforeground="White")

TopMenuBar.add_cascade(label="File", menu=TopMenuBar_File, underline=0)
TopMenuBar.add_cascade(label="Edit", menu=TopMenuBar_Edit, underline=0)

WritingArea_Scrollbar = Scrollbar(root, width=15, orient=VERTICAL)
WritingArea_Scrollbar.pack(side = RIGHT, fill=Y)

WritingArea_Text = Text(root, fg="White", bg="#3d3d3d", font=("Times", 16),
                        yscrollcommand=WritingArea_Scrollbar.set, undo=True,
                        autoseparators=True, maxundo=-1)
WritingArea_Text.bind("<Key>",OnKeyPress)
WritingArea_Text.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

WritingArea_Scrollbar.config(command=WritingArea_Text.yview)
WritingArea_Scrollbar.pack()

# Key Binds

root.bind("<Control-S>", lambda event: QuestionSaveAsFile())
root.bind("<Control-s>", lambda event: QuestionSaveFile())
root.bind("<Control-o>", lambda event: OpenFile())
root.bind("<Control-w>", lambda event: QuestionSaveFileOnClose())
root.bind("<Control-c>", lambda event: CopyText())
root.bind("<Control-x>", lambda event: CutText())
root.bind("Control-v", lambda event: PasteText())
root.bind("Control-z", lambda event: UndoAction())
root.bind("Conntrol-y", lambda event: RedoAction())

# Running Application

if __name__ == '__main__':
    root.mainloop()
