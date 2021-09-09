import tkinter as tk
from tkinter.filedialog import askopenfilename

def upload_file():
    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename() 
    print(filename)

