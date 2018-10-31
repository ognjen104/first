import datetime
import os

#Tkinter
from tkinter import *
    
window = Tk()
window.title('Bijela tehnika')
frame = Frame(window,width=660, height=280)
frame.pack()

#Baza
import sqlite3 as dbapi

conn = dbapi.connect('Baza\\baza_bijele_tehnike.db')
cur=conn.cursor()

#Aparat
et1 = Label(frame, text = "Aparat:",anchor=W)
et1.place(x = 10, y = 10, width=120, height=25)

aparat = StringVar(window)
aparat.set("") # default value
meni_aparat = OptionMenu(window, aparat, "masina_za_ves", "masina_za_sudje", "masina_za_susenje", "elektricni_sporet", "frizider", "zamrzivac", "blender", "mikser", "usisivac")
meni_aparat.place(x = 10, y = 40, width=140, height=25)
#Proizvodjac
et2 = Label(frame, text = "Proizvodjac:",anchor=W)
et2.place(x = 10, y = 70, width=120, height=25)

proizvodjac = StringVar(window)
proizvodjac.set("") # default value
meni_proizvodjac = OptionMenu(window, proizvodjac, "Beko", "Gorenje", "Elektrolux", "Vox", "Zanussi", "LG", "Miele", "Samsung")
meni_proizvodjac.place(x = 10, y = 100, width=140, height=25)
#Boja
et3 = Label(frame, text = "Boja:",anchor=W)
et3.place(x = 10, y = 130, width=120, height=25)

boja = StringVar(window)
boja.set("") # default value
meni_boja = OptionMenu(window, boja, "bijela", "siva", "crna", "crvena")
meni_boja.place(x = 10, y = 160, width=140, height=25)



#Provjeri stanje
def provjeri_stanje():
    if(aparat.get()!="" and proizvodjac.get()!="" and boja.get()!=""):
        cur.execute('SELECT * FROM bijela_tehnika WHERE aparat="'+aparat.get()+'" and proizvodjac="'+proizvodjac.get()+'" and boja="'+boja.get()+'" ')
        result=cur.fetchone()
        if(result):
            message='Aparat:            '+result[1]+'\nProizvodjac:   '+result[2]+'\nBoja:                '+result[3]+'\nCijena:             '+str(result[4])+' KM\nStanje              '+str(result[5])
            poruka.configure(text=message)
            conn.commit()
            return True
        else:
            poruka.configure(text="Nema na stanju trazenog artikla.")
            return False
    else:
        poruka.configure(text="Niste unijeli sve podatke.")
        return False
        
dugme1 = Button(frame, text = "Provjeri stanje", command = lambda: provjeri_stanje())
dugme1.place(x = 200, y = 10, width=200, height=25)

poruka = Label(frame, text="", height=50, width=120, bg="white", justify=LEFT, anchor=NW)
poruka.place(x = 200, y = 40, width=200, height=145)



#Naruci
def naruci(): 
    if(provjeri_stanje()):
        cur.execute('SELECT * FROM bijela_tehnika WHERE aparat="'+aparat.get()+'" and proizvodjac="'+proizvodjac.get()+'" and boja="'+boja.get()+'" ')
        result=cur.fetchone()
        
        if (result[5]==1):
            cur.execute('DELETE FROM bijela_tehnika WHERE ide = "'+result[0]+'"')
        else:
            cur.execute('UPDATE bijela_tehnika SET stanje="'+str(result[5]-1)+'" WHERE id="'+str(result[0])+'"')   
        conn.commit()
        
        datoteka = inputIme.get()+'_'+inputPrezime.get()+'_'+str(result[0])+'.txt'
        izlaz = open('Narudzbe/'+datoteka, 'w')
        izlaz.write('|------------------------------------|\n|      TRGOVINA BIJELE TEHNIKE\n|------------------------------------|\n|\n|Naruceno za:\n|\n|Ime:               '+inputIme.get()+'\n|Prezime:           '+inputPrezime.get()+'\n|Adresa:            '+inputAdresa.get()+'\n|Telefon:           '+inputTelefon.get()+'\n|------------------------------------|\n|ID:                '+str(result[0])+'\n|Aparat:            '+result[1]+'\n|Proizvodjac:       '+result[2]+'\n|Boja:              '+result[3]+'\n|\n|cijena bez PDV:    '+str(result[4]-(result[4]*17/100))+' KM\n|PDV (17%):         '+str(result[4]*17/100)+' KM\n|Cijena sa PDV:     '+str(result[4])+'\n|------------------------------------|\n|\n|Datum:\n|'+str(datetime.date.today())+'\n|------------------------------------|')
        
        izlaz.close()
        os.startfile('Narudzbe\\'+datoteka)
        
    else:
        poruka.configure(text="Niste odabrali artikal.")
    
etIme = Label(frame, text = "Ime:",anchor=W)
etIme.place(x = 450, y = 10, width=50, height=25)
ime=StringVar()
inputIme = Entry(frame, width = 140, textvariable=ime)
inputIme.place(x = 510, y = 10, width=140, height=25)

etPrezime = Label(frame, text = "Prezime:",anchor=W)
etPrezime.place(x = 450, y = 40, width=50, height=25)
prezime=StringVar()
inputPrezime = Entry(frame, width = 140, textvariable=prezime)
inputPrezime.place(x = 510, y = 40, width=140, height=25)

etAdresa = Label(frame, text = "Adresa:",anchor=W)
etAdresa.place(x = 450, y = 80, width=50, height=25)
adresa=StringVar()
inputAdresa = Entry(frame, width = 140, textvariable=adresa)
inputAdresa.place(x = 510, y = 80, width=140, height=25)

etTelefon = Label(frame, text = "Telefon:",anchor=W)
etTelefon.place(x = 450, y = 120, width=50, height=25)
telefon=StringVar()
inputTelefon = Entry(frame, width = 140, textvariable=telefon)
inputTelefon.place(x = 510, y = 120, width=140, height=25)

def stampaj():
    cur.execute('SELECT * FROM bijela_tehnika WHERE aparat="'+aparat.get()+'" and proizvodjac="'+proizvodjac.get()+'" and boja="'+boja.get()+'" ')
    result=cur.fetchone()
    conn.commit()
    naziv = inputIme.get()+'_'+inputPrezime.get()+'_'+str(result[0])+'.txt'
    if(os.path.isfile('Naridzbe\\'+naziv)):
         os.startfile('Narudzbe\\'+naziv, "print")
    else:
        naruci()
        os.startfile('Narudzbe\\'+naziv, "print")
    
dugme2 = Button(frame, text = "Naruci", command = lambda: naruci())
dugme2.place(x = 450, y = 160, width=200, height=25)

dugme3 = Button(frame, text = "Stampaj narudzbu", command = lambda: stampaj())
dugme3.place(x = 450, y = 200, width=200, height=25)

dugme4 = Button(frame, text = "Izadji", command = lambda: quit())
dugme4.place(x = 450, y = 240, width=200, height=25)


def reset():
    aparat.set("")
    proizvodjac.set("")
    boja.set("")
    poruka.configure(text="")
    ime.set("")
    prezime.set("")
    adresa.set("")
    telefon.set("")

dugme5 = Button(frame, text = "Reset", command = lambda: reset())
dugme5.place(x = 200, y = 200, width=200, height=25)

window.mainloop()