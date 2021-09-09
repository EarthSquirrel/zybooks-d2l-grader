import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
#from gui_functions import *

# Variables that do things
zybook_csv_path = ''



root = tk.Tk()

# label to display file name
uploaded_file_str = tk.StringVar()
label_uploaded_file = tk.Label(root, textvariable=uploaded_file_str)
uploaded_file_str.set('select a file to upload')
label_uploaded_file.grid(row=1, columnspan=2, sticky='')


# controls to upload a file
def upload_file():
    print('Calling: upload_file')
    # show an "Open" dialog box and return the path to the selected file
    zybook_csv_path = askopenfilename() 
    uploaded_file_str.set(os.path.split(zybook_csv_path)[1])
label_upload_file = tk.Label(root, text="zyBook csv file: ")
label_upload_file.grid(row=0, column=0)
btn_upload_file = tk.Button(root, text="Upload File", command=upload_file)
btn_upload_file.grid(row=0, column=1)



root.mainloop()
