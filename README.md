# zyBooks to D2L Grade Transferrer 
The goal of this script is to take students' grades from zyBooks and input
them into D2L.

### Initial Setup
The usernames in zyBooks and D2L are not the same therefore a mapping file must
first be created. To do this you need two files:
1. zyBook grade CSV file with usernames
2. A txt file with all the D2L usernames in the class

Run:
```
python build_mapping.py zybook_csv_path d2l_class_list_path
```
This script will make two files. 
* *d2l\_zybook\_mapping.csv:* This will contain the mapping of zyBook users
to D2L usernames. D2L usernames with no matching zyBook usernames will be
added to the end.
* *unmatched_zybooks.txt:* This will have the zyBook users that do not have 
matching D2L usernames. Some of these discrepancies are from students using
different names.
