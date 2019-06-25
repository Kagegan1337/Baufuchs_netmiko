from tkinter import *


# Create window
window = Tk()
window.title("VLAN/Port Config")
window.geometry('400x200')

lbl = Label(window, text="Options", font=("Arial Bold", 15)).pack()


# Frames
vlanFrame = Frame(window)
vlanFrame.pack()

portFrame = Frame(window)
portFrame.pack()

buttonFrame = Frame(window)
buttonFrame.pack()

# Functions:


# on change dropdown value // function change vlan here
def change_vlan(*args):
    print(tkvar.get())


# toggle-Button (Port change ON/OFF)
def toggle():
    if portButton.config('relief')[-1] == 'sunken':
        portButton.config(relief="raised")
        portButton.config(text="OFF")
        portButton.config(bg="red")
    else:
        portButton.config(relief="sunken")
        portButton.config(text="ON")
        portButton.config(bg="lightgreen")


# Create a Tkinter variable
tkvar = StringVar(window)

vlans = {"vlan_1", "vlan_2", "vlan 3"}
tkvar.set("vlan_1")  # default option


# Row: VLAN
vlanLabel = Label(vlanFrame, text="VLAN:")
vlanLabel.pack(side=LEFT)

vlanMenu = OptionMenu(vlanFrame, tkvar, *vlans)
vlanMenu.pack(side=RIGHT)


# Row: Port
portLabel = Label(portFrame, text="Port")
portLabel.pack(side=LEFT)

portButton = Button(portFrame, text="Off", bg="red", relief="raised", command=toggle)
portButton.pack(side=RIGHT)


# Buttons
saveButton = Button(buttonFrame, text="Save").pack(side=LEFT)
cancelButton = Button(buttonFrame, text="Cancel").pack(side=RIGHT)


# link function to change dropdown
tkvar.trace('w', change_vlan)


window.mainloop()