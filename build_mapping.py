import pandas as pd
import sys

# paths to files from command line input
zybook_csv_path = sys.argv[1]
d2l_class_list_path = sys.argv[2]

# get usernames for class
d2l_class_list = []
with open(d2l_class_list_path, 'r') as f:
    line = f.readline()
    while line:
        d2l_class_list.append(line.strip())
        line = f.readline()
