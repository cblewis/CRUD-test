#!/usr/bin/env python3

import os
import time
from tkinter import *

#Masterfully crafted by Cameron Lewis

root = Tk()

menu = Menu(root)
root.config(menu=menu)

def displayme():
    labelResult3 = Label(root, text="This script was masterfully crafted by Cameron Lewis.", bg="green", fg="white")
    labelResult3.pack(side=BOTTOM, fill=X)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Who made this?", command=displayme)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)


theLabel = Label(root, text="This program creates, writes, renames and deletes a test file in the directory specified.")
theLabel.pack(side=TOP)

theLabelPrompt = Label(root, text="Paste the directory you want to CRUD test below:")
theLabelPrompt.pack(side=TOP)

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

entryField = Entry(root)
entryField.pack(side=TOP, fill=X)

def MainFunction():
    try:
        file_path = entryField.get()
        os.startfile(file_path)
        os.path.join('crudfile_test.txt')
        #if not os.path.exists(file_path):
        #    os.makedirs(file_path)
        os.chdir(file_path)
        with open("crudfile_test.txt", 'w') as file:
            file.write("This file has been made to automate")
            file.write("\nCRUD testing these directories.")
            file.close()
        time.sleep(3.0)
        os.rename("crudfile_test.txt", "crudfile_test_renamed.txt")
        time.sleep(3.0)
        os.remove("crudfile_test_renamed.txt")
        labelResult = Label(root, text="The test was successful.", bg="green", fg="white")
        labelResult.pack(side=BOTTOM, fill=X)
    except:
        labelResult2 = Label(root, text="ERRROR: Either no directory was found or the writing/renaming process failed.", bg="red", fg="white")
        labelResult2.pack(side=BOTTOM, fill=X)

button1 = Button(bottomFrame, text="Press this button to initiate.",
                 command=MainFunction)
button1.pack()

button2 = Button(bottomFrame, text="Press this button to exit.",
                 command=exit)
button2.pack()

#c = Checkbutton(root, text="Test this here.")
#c.pack(side=RIGHT)

root.geometry("500x200")
root.mainloop()