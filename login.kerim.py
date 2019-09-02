from tkinter import *

def buttonVerarbeitenClick():
    listeAusgewaehlt = listboxNamen.curselection()
    itemAusgewaehlt = listeAusgewaehlt[0]
    nameAusgewaehlt = listboxNamen.get(itemAusgewaehlt)
    textBegruessung = 'Sie besetzen ' + nameAusgewaehlt +' !'
    labelText.config(text=textBegruessung)

# Erstellen des Fensters
window = Tk()
window.title("JOKAP - Network")
lbl = Label(window, text="Port Manager")
lbl.grid(column=0, row=0)
window.geometry('350x200')


# Rahmen Listbox
frameListbox = Frame(master=window, bg='#FFCFC9')
frameListbox.place(x=40, y=30, width=160, height=80)

# Rahmen Ausgabe
frameAusgabe = Frame(master=window, bg='#D5E88F')
frameAusgabe.place(x=40, y=115, width=160, height=30)

# Rahmen Verarbeitung
frameVerarbeitung = Frame(master=window, bg='#FBD975')
frameVerarbeitung.place(x=40, y=150, width=160, height=30)

# Kontrollvariable
text = StringVar()

# Listbox
listboxNamen = Listbox(master=frameListbox, selectmode='browse')
listboxNamen.insert('end', 'Port 1')
listboxNamen.insert('end', 'Port 2')
listboxNamen.insert('end', 'Port 3')
listboxNamen.insert('end', 'Port 4')
listboxNamen.insert('end', 'Port 5')
listboxNamen.insert('end', 'Port 6')
listboxNamen.insert('end', 'Port 7')
listboxNamen.insert('end', 'Port 8')
listboxNamen.place(x=5, y=4, width=150, height=70)

# Scrollbar
yScroll = Scrollbar(master=frameListbox, orient='vertical')
yScroll.place(x=144, y=5, width=10, height=67)
listboxNamen.config(yscrollcommand=yScroll.set)
yScroll.config(command=listboxNamen.yview)

# Label Text
labelText = Label(master=frameAusgabe, bg='white')
labelText.place(x=5, y=5, width=150, height=20)

# Button verarbeiten
buttonVerarbeiten = Button(master=frameVerarbeitung, text='auswählen', command=buttonVerarbeitenClick)
buttonVerarbeiten.place(x=5, y=5, width=150, height=20)

# Bild
imageWuerfel1 = PhotoImage(file='green.png')

labelWuerfel = Label(image=imageWuerfel1)
labelWuerfel.place(x=40, y=25, width=30, height=30)


# Aktivierung des Fensters
window.mainloop()