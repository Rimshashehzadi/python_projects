import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    # Corrected the AM/PM specifier from %P to %p
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)  # Call the function every 1000 ms (1 second)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='red', foreground='white')
label.pack(anchor='center')

time()

root.mainloop()
