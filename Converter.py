import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = input_entryInt.get()
    km_output = mile_input * 1.61
    output_labelStr.set(f'{round(km_output,1)} km')

#Создаем главное окно приложения
root = tk.Tk()
root.geometry("400x150")
root.title("Converter")

title_lable = ttk.Label(master = root, text = 'Miles to Kilometers', font = 'Calibri 20')
title_lable.pack()

input_frame = ttk.Frame(master= root)
input_entryInt = tk.IntVar()
input_entry = ttk.Entry(master=input_frame, textvariable = input_entryInt)
input_button = ttk.Button(master=input_frame, text = 'Convert', command= convert)
input_entry.pack(side='left', padx= 10)
input_button.pack(side='left')
input_frame.pack(padx=15)

output_labelStr = tk.StringVar()
output_label = ttk.Label(master = root, text= 'Output', font= 'Calibri 15 bold', textvariable = output_labelStr)
output_label.pack(pady=10)

#Запуск приложения
root.mainloop()