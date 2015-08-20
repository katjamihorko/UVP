from tkinter import *

from datetime import *


class Placilo():

    def __init__(self, master):

        menu = Menu(master)
        master.config(menu = menu)

        file_menu = Menu(menu)
        menu.add_cascade(label = 'Možnosti', menu = file_menu)

        file_menu.add_command(label = 'Odpri', command = self.odpri)
        file_menu.add_command(label = 'Shrani', command = self.shrani)
        file_menu.add_separator()
        file_menu.add_command(label = 'Izhod', command = master.destroy)

        Label(master, text = 'IZRAČUN DELOVNIH DNI ZA ŠTUDENTE').grid(row = 0, columnspan = 10)

        Label(master, text = 'Vnesi plačani (neto) znesek:').grid(row = 1, column = 0)
        Label(master, text = 'Bruto plačani znesek:').grid(row = 1, column = 2)
        Label(master, text = 'Delovna doba:').grid(row = 1, column = 3)
        Label(master, text = 'Mesecev:').grid(row = 1, column = 4)
        Label(master, text = 'Dni:').grid(row = 1, column = 5)

        gumb_izracunaj = Button(master, text = 'Izračunaj!', command = self.izracunaj)
        gumb_izracunaj.grid(row = 2, column = 1)

        self.zvezek = Listbox(master, selectmode = SINGLE)
        self.zvezek.grid(row = 3, rowspan = 1, column = 0, columnspan = 6, sticky = S+W+E+N)

        self.znesek = DoubleVar(master, value = 0)
        self.bruto = DoubleVar(master, value = 0)
        self.meseci = DoubleVar(master, value = 0)
        self.dnevi = DoubleVar(master, value = 0)

        self.sez_placil = []

        polje_znesek = Entry(master, textvariable = self.znesek)
        polje_znesek.grid(row = 2, column = 0)

        polje_bruto = Entry(master, textvariable = self.bruto)
        polje_bruto.grid(row = 2, column = 2)

        polje_meseci = Entry(master, textvariable = self.meseci)
        polje_meseci.grid(row = 2, column = 4)

        polje_dnevi = Entry(master, textvariable = self.dnevi)
        polje_dnevi.grid(row = 2, column = 5)
        


    def izracunaj(self):
       self.bruto.set(self.znesek.get() * 100 // 84.5)
       if self.bruto.get() > 15:
           self.dnevi.set((self.bruto.get() - self.znesek.get()) // 4.3)
           if self.dnevi.get() > 29:
               self.meseci.set(self.dnevi.get() // 30)
               self.dnevi.set(self.dnevi.get() - self.meseci.get() * 30)
           else:
               self.meseci.set(0)
           self.zvezek.insert(0, str(date.today()) + ' Pridobljena delovna doba: ' + str(self.meseci.get()) + ' mesecev in ' + str(self.dnevi.get()) + ' dni.')
           self.sez_placil += [str(date.today()) + ' Pridobljena delovna doba: ' + str(self.meseci.get()) + ' mesecev in ' + str(self.dnevi.get()) + ' dni.']

    def shrani(self):
        ime = filedialog.asksaveasfilename()
        if ime == "": 
            return
        with open(ime, 'wt', encoding = 'utf8') as f:
            for placilo in self.sez_placil:
                f.write(placilo + '\n')

    def odpri(self):
        ime = filedialog.askopenfilename()
        if ime == '':
            return
        with open(ime, encoding = 'utf8') as f:
            for vrstica in f:
                self.zvezek.insert(0, vrstica)
        

root = Tk()

aplikacija = Placilo(root)

root.mainloop()
