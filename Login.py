from tkinter import *

window = Tk()
window.title("Login")
window.geometry('400x200')

lbl = Label(window, text="Options", font=("Arial Bold", 15)).pack()

# Frames
usernameFrame = Frame(window)
usernameFrame.pack()

passwordFrame = Frame(window)
passwordFrame.pack()

buttonFrame = Frame(window)
buttonFrame.pack()

# Username
usernameLabel = Label(usernameFrame, text="Username")
usernameLabel.pack(side=LEFT)

usernameEntry = Entry(usernameFrame, width=15)
usernameEntry.pack(side=RIGHT)

# Password
passwordLabel = Label(passwordFrame, text="Username")
passwordLabel.pack(side=LEFT)

passwordEntry = Entry(passwordFrame, width=15)
passwordEntry.pack(side=RIGHT)

# Buttons
btn = Button(buttonFrame, text="Login").pack(side=LEFT)
# btn = Button(buttonFrame, text="Cancel").pack(side=RIGHT)

window.mainloop()