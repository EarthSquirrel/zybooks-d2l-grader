import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
import os, sys, re
import pandas as pd
import grade

# Initilize variables that do things
zybook_csv_path = ''
zybook_df = pd.DataFrame()

# row values
row_upload_btn = 0
row_show_file_name = 1
row_separator = 2
row_zybook_col = 3
row_d2l_col = 4
row_zybook_pts = 5
row_d2l_pts = 6
row_missing_zybook = 7
row_run = 10

# create the main window
root = tk.Tk()
root.title('zyBook to D2L Grade Converter')
#root.eval('tk::PlaceWindow . center')

# separate file upload from necessary input parameters
separator = ttk.Separator(root, orient='horizontal')
text = 'Select zyBook grade column'
label_select_zybook_col = tk.Label(root, text=text)
# OptionMenu to select column of zybook - this will hold selected zybook column
zybook_col_var = tk.StringVar(root)

# ROW 4: d2l column name
label_d2l_col = tk.Label(root, text="D2L column name (assignment_name Points Grade)")
entry_d2l_col = tk.Entry(root)

# ROW 5: zybook point adjustments
label_zybook_pts = tk.Label(root, text="Total zyBook points: ")
entry_zybook_pts = tk.Entry(root)

# ROW 6: d2l point adjustment
label_d2l_pts = tk.Label(root, text="D2L points")
entry_d2l_pts = tk.Entry(root)

# ROW 7: Include d2l entries with no zybook username as 0s
label_missing_zybook = tk.Label(root, text="What to do with missing zybook users?")
missing_zybook_var = tk.StringVar()
# NOTE: Do NOT change the order of this set. It's important for later on
options_missing_zybook = ('Include as 0', 'Ignore') 
missing_zybook_var.set(options_missing_zybook[0])

# label to display file name, make appear on start of program
uploaded_file_str = tk.StringVar()
label_uploaded_file = tk.Label(root, textvariable=uploaded_file_str)
uploaded_file_str.set('**select a file to upload**')
label_uploaded_file.grid(row=row_show_file_name, columnspan=2, sticky='', 
                         padx=10)


# controls to upload a file
def upload_file():
    global zybook_csv_path, zybook_df
    btn_upload_file['text'] = "Upload Different File"
    # show an "Open" dialog box and return the path to the selected file
    zybook_csv_path = askopenfilename()
    uploaded_file_str.set(os.path.split(zybook_csv_path)[1])
    zybook_df = pd.read_csv(zybook_csv_path)
    zybook_header = zybook_df.columns.values

    # make things visible
    separator.grid(row=row_separator, columnspan=99, sticky="nswe", padx=2,
                   pady=5)
    label_select_zybook_col.grid(row=row_zybook_col, column=0)
    zybook_col_select = tk.OptionMenu(root, zybook_col_var, *zybook_header)
    predicted_header = ''
    for col in zybook_header:
        if 'points earned' in col.lower():
            predicted_header = col
            zybook_col_var.set(predicted_header)
            break
    zybook_col_select.grid(row=row_zybook_col, column=1)

    label_d2l_col.grid(row=row_d2l_col, column=0)
    entry_d2l_col.insert(0, ' points grade')
    entry_d2l_col.grid(row=row_d2l_col, column=1)
    label_zybook_pts.grid(row=row_zybook_pts, column=0)
    entry_zybook_pts.delete(0, tk.END)
    entry_zybook_pts.insert(0, re.sub("[^0-9]", "", predicted_header))
    entry_zybook_pts.grid(row=row_zybook_pts, column=1)
    entry_d2l_pts.delete(0, tk.END)
    entry_d2l_pts.insert(0, "10")
    label_d2l_pts.grid(row=row_d2l_pts, column=0)
    entry_d2l_pts.grid(row=row_d2l_pts, column=1)
    
    select_missing_zybook = tk.OptionMenu(root, missing_zybook_var, 
                                          *options_missing_zybook)
    label_missing_zybook.grid(row=row_missing_zybook, column=0)
    select_missing_zybook.grid(row=row_missing_zybook, column=1)

    btn_process.grid(row=row_run, columnspan=99)


# ROW 0: Show button to upload a file
label_upload_file = tk.Label(root, text="zyBook csv file: ")
label_upload_file.grid(row=row_upload_btn, column=0)
btn_upload_file = tk.Button(root, text="Upload File", command=upload_file)
btn_upload_file.grid(row=row_upload_btn, column=1)

def open_output():
    path = grade.get_d2l_save_name(zybook_csv_path)
    print(path)
    if sys.platform == 'win32':
        os.startfile(path)
    elif sys.platform == 'darwin':
        os.system('open "{}"'.format(path))
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        # NOTE: I cannot test this one, so I'm just hoping it works
        os.system('xdg-open "{}"'.format(path))
    else:
        print('{} is unknown'.format(sys.platform))

def process():
    # get values from window
    zybook_col = zybook_col_var.get()
    d2l_col = entry_d2l_col.get()
    zybook_pts = entry_zybook_pts.get()
    d2l_pts = entry_d2l_pts.get()
    if missing_zybook_var.get() == options_missing_zybook[0]:
        include_missing = True
    else:
        include_missing = False
    stats = grade.run(zybook_csv_path, zybook_col, d2l_col, zybook_pts, 
                      d2l_pts, include_missing)

    window_finished = tk.Toplevel(root) 
    window_finished.title('Complete')
    tk.Label(window_finished, text=stats, padx=4).pack()
    tk.Button(window_finished, text="Open output file", 
              command=open_output).pack()
    tk.Button(window_finished, text="Exit", command=root.destroy).pack()

btn_process = tk.Button(root, command=process, text="Run")

root.mainloop()
