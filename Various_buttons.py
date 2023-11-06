import tkinter as tk
import ttkbootstrap as ttk

def ifelse():
    state_chek = check_var.get()
    if state_chek == True:
        print('good')
    else:
        print('bad')


root = tk.Tk()
root.title('buttons')
root.geometry('300x500')

#Simple button
button = ttk.Button(root, text = 'A simple button', command= ifelse)
button.pack()

#Checkbutton
check_var = tk.BooleanVar(value=True)
check_button = ttk.Checkbutton(
    root, 
    text = 'checkbox 1', 
    command= lambda: print(check_var.get()), 
    variable= check_var)
check_button.pack(pady=10)

#Radio buttons
radio1 = ttk.Radiobutton(root, text = 'radiobutton 1', value= 1)
radio2 = ttk.Radiobutton(root, text = 'radiobutton 2', value= 0)
radio1.pack()
radio2.pack()

root.mainloop()


