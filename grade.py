import pandas as pd
import sys

zybook_csv_path = sys.argv[1]
zybook_col = sys.argv[2]
d2l_col = sys.argv[3]
d2l_saved_name = sys.argv[4]

# get usernames for class
class_list_path = "classlist.txt"
class_list = []
with open(class_list_path, 'r') as f:
    line = f.readline()
    while line:
        class_list.append(line.strip())
        line = f.readline()


# read in zybooks
zybook_df = pd.read_csv(zybook_csv_path)
try:
    zybook_grade_col = zybook_df[zybook_col]
except KeyError:
    print("****** KeyError ******")
    print('"{}" is not a column in the zybooks csv'.format(zybook_col))
    print('**********************')
    print('Column options are: {}'.format(', '.join(zybook_df.columns.values)))
