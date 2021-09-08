import pandas as pd
import sys
import re
from os.path import exists

zybook_csv_path = sys.argv[1]
zybook_col = sys.argv[2]
d2l_col = sys.argv[3]
d2l_saved_name = sys.argv[4]


# Get mapping dataframe
mapping_path = 'd2l_zybook_mapping.csv'
if not exists(mapping_path):  # does mapping file exist
    print('****************************')
    print('ERROR: {} does not exist'.format(mapping_path))
    print('Run build_mapping.py to create')
    print('****************************')
    sys.exit()  # exit if cannot find the needed file
mapping = pd.read_csv(mapping_path)
mapping.set_index('d2l username', inplace=True)

# read in zybooks
zybook_df = pd.read_csv(zybook_csv_path)
zybook_df.set_index(['First name', 'Last name'], inplace=True)
try:
    zybook_grade_col = zybook_df[zybook_col]
except KeyError:
    print("****** KeyError ******")
    print('"{}" is not a column in the zybooks csv'.format(zybook_col))
    print('**********************')
    print('Column options are: {}'.format(', '.join(zybook_df.columns.values)))
    sys.exit()
