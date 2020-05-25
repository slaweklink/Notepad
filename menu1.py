# Notepad style application that can open, edit, and save text documents.
# Optional: Add syntax highlighting and other features.

from tkinter import *
from tkinter import messagebox #dodajemy możliwość wyświetlania wiadomości
from tkinter import filedialog #dodajemy możliwość otwierania okna dialogowego zapisz/otwórz


def nowy_plik():
    text1.delete(1.0, END)

def openfile():
    global file1
    global nazwa_pliku
    text1.delete(1.0, END)
    nazwa_pliku = filedialog.askopenfilename()
    file1 = open(nazwa_pliku, "r+")
    text1.insert(1.0, file1.read())
    root.title(str(nazwa_pliku))

def zapisz():
    file1.seek(0)
    file1.truncate(0)
    tekstdozapisania = str(text1.get(1.0, END))
    file1.write(tekstdozapisania)
    file1.close()

def donothing():
    messagebox.showinfo("Info", "Ja nic nie robię")
    messagebox.showinfo("Info", "ja też nie")

def oprogramie():
    messagebox.showinfo("O programie", "Prosty edytor tekstu stworzony za pomocą Pythona")

def pomoc():
    messagebox.showinfo("Pomoc","Nie potrzebujesz pomocy, to naprawdę prosty program!")

def zapiszjako():
    file2 = filedialog.asksaveasfile(mode="w")
    if file2 is None: # jeśli użytkownik kliknie cancel to program nic nie zwróci
        return
    tekstdozapisania = str(text1.get(1.0, END)) #zaczyna od 1.0 nie 0.0
    file2.write(tekstdozapisania)
    file2.close()

#creating the window
root = Tk()
text1 = Text(root, height = 100, width = 400) #creating a textbox
text1.pack() #making the textbox visible
#definiowanie parametrów okna
root.geometry("800x600") #ustawiamy wymiary ekranu
root.title("Edytor tekstu SlavkoNote") #changing the name of the window


#tworzymy menu plik
menubar = Menu(root) #główne menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nowy", command=nowy_plik)
filemenu.add_command(label="Otwórz", command=openfile)
filemenu.add_command(label="Zapisz", command=zapisz)
filemenu.add_command(label="Zapisz jako...", command=zapiszjako)


filemenu.add_separator()

filemenu.add_command(label="Zamknij program", command=root.quit)
menubar.add_cascade(label="Plik", menu=filemenu) #dodajemy menu plik do całego menu
#koniec tworzenia menu plik

#tworzymy menu edycja
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cofnij", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Wytnij", command=donothing)
editmenu.add_command(label="Kopiuj", command=donothing)
editmenu.add_command(label="Wklej", command=donothing)
editmenu.add_command(label="Usuń", command=donothing)
editmenu.add_command(label="Zaznacz wszystko", command=donothing)

menubar.add_cascade(label="Edycja", menu=editmenu)
#koniec tworzenia menu edycja

#tworzymy menu pomoc
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="O programie", command=oprogramie)
helpmenu.add_command(label="Pomoc", command=pomoc)
menubar.add_cascade(label="Pomoc", menu=helpmenu)
#koniec tworzenia menu pomoc


root.config(menu=menubar) # dodajemy menu o nazwie menubar
root.mainloop()
