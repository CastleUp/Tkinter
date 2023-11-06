import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

root = tk.Tk()
root.geometry('300x300')

string_var = tk.StringVar(value= 'start value')

label = ttk.Label(master=root, text='Lable', textvariable= string_var)
label.pack()

entry =ttk.Entry(textvariable= string_var)
entry.pack()

button = ttk.Button(master= root, text = 'button', command= button_func)
button.pack(pady=5)

testing_entri_strung = tk.StringVar(value= 'test')
entry_1 =ttk.Entry(textvariable= testing_entri_strung)
entry_2 =ttk.Entry(textvariable= testing_entri_strung)
label_1 = ttk.Label(textvariable= testing_entri_strung)
label_1.pack()
entry_1.pack()
entry_2.pack()

root. mainloop()