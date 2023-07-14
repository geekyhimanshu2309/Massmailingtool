import tkinter as tk
from tkinter import filedialog
import pandas as pd

file_path = ""
def open_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files","*.xlsx")])
    file_name_entry.delete(0,tk.END)
    file_name_entry.insert(0,file_path)
    data_frame = pd.read_excel(file_path)
    print(data_frame)
    
window = tk.Tk()

title_label = tk.Label(window, text="Select Excel File:")
title_label.pack()

file_name_entry = tk.Entry(window,width=50)
file_name_entry.pack()

button = tk.Button(window, text="Open File",command=open_file)
button.pack()

window.mainloop()