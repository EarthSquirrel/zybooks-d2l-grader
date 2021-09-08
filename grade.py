import pandas as pd
import sys

zybook_csv_path = sys.argv[1]
zybook_column = sys.argv[2]
d2l_column = sys.argv[3]
d2l_saved_name = sys.argv[4]


# read in zybooks
zybook_df = pd.read_csv(zybook_csv_path)
print(zybook_df[zybook_column])
