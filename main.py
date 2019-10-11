__author__ = 'Andres Julian'
import easygui as eg
import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk
from tkinter.scrolledtext import ScrolledText


class APP:

    def __init__(self):
        # creat ventana
        self.r = Tk()
        self.r.geometry('400x500')
        self.r.configure(bg='beige')
        self.r.title('Cantidad de Informacaion')
        # Creat Pestañas
        tab_control = ttk.Notebook(self.r)
        txt = ttk.Frame(tab_control)
        arch = ttk.Frame(tab_control)
        tab_control.add(txt, text='Texto')
        tab_control.add(arch, text='Archivo')
        tab_control.pack(expand=1, fill='both')
        # archivo
        self.cajtexto = ScrolledText(arch, width=35, height=4)
        self.cajtexto.place(x=10, y=29)
        laD = Label(arch, text="Desplazamiento ", fg="black")
        laD.place(x=10, y=105)
        self.cajdes = ttk.Entry(arch, justify=tk.LEFT)
        self.cajdes.place(x=100, y=105)
        self.cajaruta = ttk.Entry(arch, justify=tk.LEFT)
        self.cajaruta.place(x=10, y=5, width=298, height=20)
        self.cajaruta.insert(0, 'c:/usuario/ejemplo')
        self.cajfin = ScrolledText(arch, width=45, height=19)
        self.cajfin.place(x=10, y=150)
        # TExto
        self.cajatexto = ScrolledText(txt, width=35, height=5)
        self.cajatexto.place(x=10, y=15)
        laD = Label(txt, text="Desplazamiento ", fg="black")
        laD.place(x=10, y=105)
        self.cajades = ttk.Entry(txt, justify=tk.LEFT)
        self.cajades.place(x=100, y=105)
        self.cajafin = ScrolledText(txt, width=45, height=19)
        self.cajafin.place(x=10, y=150)
        # button inicio3
        self.botnini = ttk.Button(arch, text='Archivo', command=self.direccion)
        self.botnini.place(x=315, y=4)
        self.botonini = ttk.Button(txt, text='Iniciar', command=self.cesar)
        self.botonini.place(x=315, y=15)
        self.botnini = ttk.Button(arch, text='Iniciar', command=self.cesar)
        self.botnini.place(x=315, y=35)
        self.botnini.config(state=tk.DISABLED)
        self.r.mainloop()

    def cesar(self):
        self.limpiesa(1)
        ruta = self.cajaruta.get()
        if ruta == "c:/usuario/ejemplo":
            des = int(self.cajades.get())
            texto = self.cajatexto.get('0.1', END)
            T = 1
        else:
            des = int(self.cajdes.get())
            texto = []
            ruta = self.cajaruta.get()
            print(ruta)
            archivo = open(ruta, encoding="utf8")
            txt = archivo.readlines()
            self.cajtexto.insert('0.1', txt)
            for i in range(len(txt)):
                for j in range(len(txt[i])):
                    texto.append(txt[i][j])
            texto = str(texto)
            T = 0
            archivo.close()
        asci = []
        for i in range(len(texto)):
            asci.append(chr(ord(texto[i]) + des))
        # asci = str(asci)
        self.imprimi(asci, T)
        self.limpiesa(0)

    def imprimi(self, elemento, t):
        if t is 1:
            self.cajafin.insert(0.1,elemento)
        else:
            self.cajfin.insert(0.1,elemento)

    def direccion(self):
        # self.cajaruta.config(state=tk.NORMAL)
        self.cajaruta.delete(0, END)
        extension = ["*.txt"]
        archivo = eg.fileopenbox(msg="Abrir archivo",
                                 title="Control: fileopenbox",
                                 default='',
                                 filetypes=extension)
        self.cajaruta.insert(0, archivo)
        self.cajaruta.config(state=tk.DISABLED)
        self.botnini.config(state=tk.NORMAL)

    def limpiesa(self, tipo):
        if tipo == 1:
            self.cajfin.delete(0.1, END)
            self.cajafin.delete(0.1, END)
        elif tipo == 0:
            self.cajades.delete(0, END)
            self.cajdes.delete(0, END)
            self.cajaruta.config(state=tk.NORMAL)
            self.cajaruta.delete(0, END)
            self.cajaruta.insert(0, 'c:/usuario/ejemplo')


def main():
    mi_app = APP()
    return 0


if __name__ == '__main__':
    print("Creado por", __author__)
    main()
