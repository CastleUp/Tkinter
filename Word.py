import tkinter as tk
import ttkbootstrap as ttk

def export():
    with open('text_file', 'w') as tw:
        tw.write(input_text.get())

root = tk.Tk()
root.title('Window and Widgets')
root.geometry('800x600')

ttk.Label(master= root, text='Write your text', font= 'Calbri 15').pack(pady= 10)

input_text_string = tk.StringVar()
input_text = ttk.Entry(master = root, width= 200 , textvariable = input_text_string)
input_text.pack(pady= 10)

button = ttk.Button(master = root, text = 'Export', width= 40, command= export)
button.pack(pady= 10)

root.mainloop()