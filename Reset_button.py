import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def text_from_enty():
    entry_text = entry.get()

    label['text'] = entry_text
    entry['state'] = 'disabled'

def refresh():
    label['text'] = "label"
    entry['state'] = 'enabled'
    entry_string.set('')

window = tk.Tk()
window.geometry('200x250')

label = ttk.Label(master= window, text = 'label', font= 'Calibri 20')

entry_string = tk.StringVar()
entry = ttk.Entry(master= window, textvariable= entry_string)

button = ttk.Button(master = window, text = 'button', command= text_from_enty)

back_button = ttk.Button(master = window, text = 'Go to original', command= refresh, bootstyle=(INFO, OUTLINE))

label.pack()
entry.pack(pady=10)
button.pack()
back_button.pack(pady=15)

window.mainloop()