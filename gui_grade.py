import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import pandas as pd
#from gui_functions import *

# Variables that do things
zybook_csv_path = ''
zybook_df = pd.DataFrame()


root = tk.Tk()

# row values
row_upload_btn = 0
row_show_file_name = 1
row_separator = 2
row_zybook_col = 3
row_d2l_col = 4
row_zybook_pts = 5
row_d2l_pts = 6
row_run = 10

# OptionMenu to select column of zybook
separator = ttk.Separator(root, orient='horizontal')
#separator.grid(row=2, columnspan=99, sticky="nswe", padx=2, pady=5)
text = 'Select zyBook grade column'
label_select_zybook_col = tk.Label(root, text=text)
# this will hold selected zybook column
zybook_col_var = tk.StringVar(root)

# ROW 4: d2l column name
label_d2l_col = tk.Label(root, text="D2L column name")
entry_d2l_col = tk.Entry(root)

# ROW 5: zybook point adjustments
label_zybook_pts = tk.Label(root, text="Total zyBook points: ")
entry_zybook_pts = tk.Entry(root)

# ROW 6: d2l point adjustment
label_d2l_pts = tk.Label(root, text="D2L points")
entry_d2l_pts = tk.Entry(root)


# label to display file name
uploaded_file_str = tk.StringVar()
label_uploaded_file = tk.Label(root, textvariable=uploaded_file_str)
uploaded_file_str.set('select a file to upload')
label_uploaded_file.grid(row=row_show_file_name, columnspan=2, sticky='')


# controls to upload a file
def upload_file():
    global zybook_csv_path, zybook_df
    print('Calling: upload_file')
    # show an "Open" dialog box and return the path to the selected file
    zybook_csv_path = askopenfilename()
    uploaded_file_str.set(os.path.split(zybook_csv_path)[1])
    zybook_df = pd.read_csv(zybook_csv_path)

    # make things visible
    separator.grid(row=row_separator, columnspan=99, sticky="nswe", padx=2,
                   pady=5)
    label_select_zybook_col.grid(row=row_zybook_col, column=0)
    zybook_col_list = set(zybook_df.columns.values)
    zybook_col_select = tk.OptionMenu(root, zybook_col_var, *zybook_col_list)
    zybook_col_select.grid(row=row_zybook_col, column=1)

    label_d2l_col.grid(row=row_d2l_col, column=0)
    entry_d2l_col.grid(row=row_d2l_col, column=1)
    label_zybook_pts.grid(row=row_zybook_pts, column=0)
    entry_zybook_pts.grid(row=row_zybook_pts, column=1)
    label_d2l_pts.grid(row=row_d2l_pts, column=0)
    entry_d2l_pts.grid(row=row_d2l_pts, column=1)


label_upload_file = tk.Label(root, text="zyBook csv file: ")
label_upload_file.grid(row=row_upload_btn, column=0)
btn_upload_file = tk.Button(root, text="Upload File", command=upload_file)
btn_upload_file.grid(row=row_upload_btn, column=1)

def process():
    # get values from window
    zybook_col = zybook_col_var.get()
    d2l_col = entry_d2l_col.get()
    zybook_pts = entry_zybook_pts.get()
    d2l_pts = entry_d2l_pts.get()



btn_process = tk.Button(root, command=process, text="Run")
btn_process.grid(row=row_run, columnspan=99)

root.mainloop()
