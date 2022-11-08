import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu Principal")
        self.geometry("1080x900")
        self.iconbitmap('GUI/image/icons/tienda.ico')
        #self.resizable(False, False)
        self.columnconfigure(0, weight = 3)
        self.columnconfigure(1, weight = 3)
        self.columnconfigure(2, weight = 3)
        self.columnconfigure(3, weight = 3)
        self.columnconfigure(4, weight = 3)
        self._crear_menu()
        self._crear_botones_action()

    # Crear el menu   
    def _crear_menu(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        # Crear el menu de opciones
        opciones_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Opciones', menu=opciones_menu)
        #opciones_menu.add_command(label='Login', command=self._login)
        #opciones_menu.add_command(label='Salir', command=self.destroy)
        #opciones_menu.add_command(label='Login')
        opciones_menu.add_command(label='Salir')
        # Crear el menu de ayuda
        ayuda_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Ayuda', menu=ayuda_menu)
        #ayuda_menu.add_command(label='Acerca de', command=self._acerca_de)
        ayuda_menu.add_command(label='Acerca de')

    
    def _crear_botones_action(self):
        photo = tk.PhotoImage(file = r"GUI/image/img/arduino.png")
        photo1 = tk.PhotoImage(file = r"GUI/image/img/info.png")
        photo2 = tk.PhotoImage(file = r"GUI/image/img/pdf.png")

        btnInfo = tk.Button(self, image = photo, width = 50, height = 50)
        btnInfo1 = tk.Button(self,  image = photo1, width=50, height=50)
        btnInfo2 = tk.Button(self, image = photo2, width=50, height=50)
        btnInfo3 = tk.Button(self, image = photo, width = 50, height = 50)
        btnInfo4 = tk.Button(self, image = photo, width = 50, height = 50)

        btnInfo.grid(row = 1, column = 0, sticky="NWE")
        btnInfo1.grid(row = 1, column = 1, sticky="NWE")
        btnInfo2.grid(row = 1, column = 2, sticky="NWE")
        btnInfo3.grid(row = 1, column = 3, sticky="NWE")
        btnInfo4.grid(row = 1, column = 4, sticky="NWE")

if __name__ == '__main__':
    app = Main()
    app.mainloop()