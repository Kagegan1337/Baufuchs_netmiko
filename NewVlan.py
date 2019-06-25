from tkinter import *


# Create window
window = Tk()
window.title("VLAN-Config")
window.geometry('400x200')

lbl = Label(window, text="VLAN-Config", font=("Arial Bold", 15)).pack()


# Frames
vlanaddFrame = Frame(window)
vlanaddFrame.pack()

vlandeleteFrame = Frame(window)
vlandeleteFrame.pack()


# Row: Add
vlanLabel = Label(vlanaddFrame, text="Add:")
vlanLabel.pack(side=LEFT)

vlanaddEntry = Entry(vlanaddFrame, width=10)
vlanaddEntry.pack(side=LEFT)

vlanaddButton = Button(vlanaddFrame, text="Add")
vlanaddButton.pack(side=RIGHT)


# Row: Delete
portLabel = Label(vlandeleteFrame, text="Delete:")
portLabel.pack(side=LEFT)

vlandeleteEntry = Entry(vlandeleteFrame, width=10)
vlandeleteEntry.pack(side=LEFT)

vlandeleteButton = Button(vlandeleteFrame, text="Delete")
vlandeleteButton.pack(side=RIGHT)


window.mainloop()