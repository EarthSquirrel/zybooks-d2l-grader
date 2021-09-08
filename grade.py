import pandas as pd
import sys

zybook_csv_path = sys.argv[1]
zybook_column = sys.argv[2]
d2l_column = sys.argv[3]
d2l_saved_name = sys.argv[4]

# get usernames for class
class_list_path = "classlist.txt"
class_list = []
with open(class_list_path, 'r') as f:
    line = f.readline()
    while line:
        class_list.append(line.strip())
        line = f.readline()

print(class_list)

# read in zybooks
zybook_df = pd.read_csv(zybook_csv_path)
