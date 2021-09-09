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

# OptionMenu to select column of zybook
separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=2, columnspan=99, sticky="nswe", padx=2, pady=5)
text = 'Select zyBook grade column'
label_select_zybook_col = tk.Label(root, text=text)
label_select_zybook_col.grid(row=3, column=0)
# make random thing in OptionMenu that will be updated when file uploaded
zybook_col_var = tk.StringVar(root)
zybook_col_list = ('upload csv file',)
zybook_col_select = tk.OptionMenu(root, zybook_col_var, *zybook_col_list)
zybook_col_select.grid(row=3, column=1)

# ROW 4: d2l column name
label_d2l_col = tk.Label(root, text="D2L column name")
label_d2l_col.grid(row=4, column=0)
entry_d2l_col = tk.Entry(root)
entry_d2l_col.grid(row=4, column=1)

# ROW 5: point adjustments



# label to display file name
uploaded_file_str = tk.StringVar()
label_uploaded_file = tk.Label(root, textvariable=uploaded_file_str)
uploaded_file_str.set('select a file to upload')
label_uploaded_file.grid(row=1, columnspan=2, sticky='')


# controls to upload a file
def upload_file():
    global zybook_csv_path, zybook_df
    print('Calling: upload_file')
    # show an "Open" dialog box and return the path to the selected file
    zybook_csv_path = askopenfilename()
    uploaded_file_str.set(os.path.split(zybook_csv_path)[1])
    zybook_df = pd.read_csv(zybook_csv_path)

    # update zybook column options
    # Reset var and delete all old options
    zybook_col_var.set('')
    zybook_col_select['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to StringVar)
    new_choices = set(zybook_df.columns.values)
    for choice in new_choices:
        zybook_col_select['menu'].add_command(label=choice,
                                              command=tk._setit(zybook_col_var,
                                                                choice))

label_upload_file = tk.Label(root, text="zyBook csv file: ")
label_upload_file.grid(row=0, column=0)
btn_upload_file = tk.Button(root, text="Upload File", command=upload_file)
btn_upload_file.grid(row=0, column=1)

def process():
    # get the zybook column
    zybook_col = zybook_col_var.get()
    print('selected zybook column: ', zybook_col)

    # get d2l column label
    d2l_col = entry_d2l_col.get()
    print('D2L column label: ', d2l_col)


btn_process = tk.Button(root, command=process, text="Run")
btn_process.grid(row=10, columnspan=99)

root.mainloop()
