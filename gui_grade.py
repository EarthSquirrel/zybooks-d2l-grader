import tkinter as tk
from gui_functions import *

top = tk.Tk()

btn_upload_file = tk.Button(top, text="Upload File", command=upload_file)
btn_upload_file.pack(side=tk.LEFT)

top.mainloop()
