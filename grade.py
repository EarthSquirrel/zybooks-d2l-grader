import pandas as pd
import sys
import re
from os.path import exists, split, join

# get command line inputs
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

# create empty d2l df
d2l_df_cols = ['Username', d2l_col, 'End-of-Line Indicator']
d2l_df = pd.DataFrame([], columns=d2l_df_cols)

# create lists to hold missing rows
used_zybooks = []
used_d2l = []


# go through mapping and do zybook things
for index, row in mapping.iterrows():
    # get grade from zybook df
    zybook_index = (row['First name'], row['Last name'])
    try:
        grade = zybook_df.loc[zybook_index, zybook_col]
        grade = round(grade*10/29, 1)
        used_d2l.append(index)
        used_zybooks.append(zybook_index)
        graded = pd.DataFrame([[index, grade, '#']], columns=d2l_df_cols)
        d2l_df = d2l_df.append(graded, ignore_index=True)
    except KeyError:
        print('{} did not map to zybook index'.format(index))
        grade = 'ERROR'  # TODO: What to put here?

#print(d2l_df)
d2l_df.to_csv(d2l_saved_name, index=False)


# print not accounted for values
print('***************************************************')
# tell d2l usernames not outputed
# s.difference(t)   s - t        new set with elements in s but not in t
d2l_missed = list(set(mapping.index.values).difference(set(used_d2l)))
print('d2l usernames with no zybook grade:')
print(d2l_missed)
# tell zybook names not outputed
zybook_missed = list(set(zybook_df.index.values).difference(set(used_zybooks)))
print('zybook names with no d2l username:')
print(zybook_missed)
