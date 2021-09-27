import tkinter as tk
from tkinter import ttk

# initialize window
root = tk.Tk()
root.geometry('600x300+0+0')
root.title('Buttons')


def settings():
    settings_win = tk.Toplevel()
    settings_win.geometry('1600x800+0+0')
    settings_win.title('Home')


settings_Btn = tk.Button(root, text='Settings', bg='green', command=settings)
settings_Btn.place(x=50, y=50)
