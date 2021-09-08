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


#
complete_d2l_usernames = []  # store the usernames that work in zybooks
missed_zybooks_users = []
# go through each row in zybooks and find corresponding d2l username
for index, row in zybook_df.iterrows():
    added = False
    #print('Zybook: {} {}'.format(row['First name'], row['Last name']))
    # compare last name to d2l usernames
    for student in class_list:
        student = student.lower()
        if row['Last name'].lower() in student:
            if row['First name'].lower() in student:
                complete_d2l_usernames.append(student)
                #print(student)
                added = True
                # TODO: update d2l grade csv
    if not added:
        missed_zybooks_users.append([row['First name'], row['Last name']])

print(missed_zybooks_users)

print('complete_d2l_usernames len: {}'.format(len(complete_d2l_usernames)))
print('class_list len: {}'.format(len(class_list)))
