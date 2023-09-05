#ventana
from tkinter import *
from tkinter import messagebox as MessageBox

def test():
    MessageBox.showinfo("Juego Ahorcado", "Bienvenido Usuario") # título, mensaje

root = Tk()

Button(root, text = "HAZ CLIC AQUI", command=test).pack()

root.mainloop()

