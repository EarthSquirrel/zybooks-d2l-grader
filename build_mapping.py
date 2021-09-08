import pandas as pd
import sys
import re

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


# read in zybooks
zybook_df = pd.read_csv(zybook_csv_path)

# pair zybook name with d2l usernames
matched = []   # d2l usernames with matched zybook name
missed_zybooks_users = []
# go through each row in zybooks and find corresponding d2l username
for index, row in zybook_df.iterrows():
    added = False  # bool to tell if zybooks name matched d2l username
    # compare last name to d2l usernames
    for student in d2l_class_list:
        student = student.lower()
        last_name = row['Last name'].lower()
        last_name = re.sub(r'\W+', '', last_name)
        if last_name in student:
            first_name = row['First name'].lower()
            first_name = re.sub(r'\W+', '', first_name)
            if first_name in student:
                matched.append([student, row['First name'], row['Last name']])
                added = True
    if not added:
        missed_zybooks_users.append('{} {}'.format(row['First name'],
                                                   row['Last name']))

print('Zybook users not found:')
print(missed_zybooks_users)

print('D2L users not found:')
success_d2l = [match[0] for match in matched]
# s.difference(t)   s - t   new set with elements in s but not in t
missing_d2l = list(set(d2l_class_list).difference(set(success_d2l)))
print(missing_d2l)
