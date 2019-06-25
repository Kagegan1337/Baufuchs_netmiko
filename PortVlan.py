from tkinter import *

window = Tk()
window.title("Options")
window.geometry('400x200')

lbl = Label(window, text="Options", font=("Arial Bold", 15)).pack()

# Frames
vlanFrame = Frame(window)
vlanFrame.pack()

portFrame = Frame(window)
portFrame.pack()

buttonFrame = Frame(window)
buttonFrame.pack()

# Create a Tkinter variable
tkvar = StringVar(window)

vlans = {"vlan_1", "vlan_2", "vlan 3"}
tkvar.set("vlan_1")  # default option

# Reihe: VLAN
vlanLabel = Label(vlanFrame, text="VLAN:")
vlanLabel.pack(side=LEFT)

vlanMenu = OptionMenu(vlanFrame, tkvar, *vlans)
vlanMenu.pack(side=RIGHT)

# Reihe: Port
portLabel = Label(portFrame, text="Port")
portLabel.pack(side=LEFT)

portEntry = Entry(portFrame, width=15) # on/off switch here
portEntry.pack(side=RIGHT)

# Buttons
SaveButton = Button(buttonFrame, text="Save").pack(side=LEFT)
# btn = Button(buttonFrame, text="Cancel").pack(side=RIGHT)

# Functions:


# on change dropdown value // füller
def change_vlan(*args):
    print(tkvar.get())


# link function to change dropdown
tkvar.trace('w', change_vlan)




window.mainloop()