import tkinter as tk
from gui_functions import *

root = tk.Tk()

# controls to upload a file
label_upload_file = tk.Label(root, text="zyBook csv file: ")
label_upload_file.pack(side=tk.LEFT)
btn_upload_file = tk.Button(root, text="Upload File", command=upload_file)
btn_upload_file.pack(side=tk.RIGHT)

root.mainloop()
