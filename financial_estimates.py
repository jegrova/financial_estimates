#!/usr/bin/env python3

import utils

# TODO převést výpočty z sheetu


import pandas

csv_files = utils.get_all_reports_current_dir()

df_from_each_file = (pandas.read_csv(f, sep=';') for f in csv_files)
concatenated_df = pandas.concat(df_from_each_file, ignore_index=True)

# TODO součty každého měsíce podle budgetů
# TODO stav po každém měsíci podle budgetů
# TODO celkem příjmy v měsíci
# TODO celkem výdaje v měsící
# TODO rozdíl v měsíci
# TODO procento neutracených peněz
# TODO měsíční zůstatek na účtu
# TODO měsíční průměr zůstatků na účtu
# TODO roční zůstatek po všech měsících



print(concatenated_df.loc[664])

print(concatenated_df['date'])
concatenated_df['date']= pandas.to_datetime(concatenated_df['date'])
print(concatenated_df['date'])
concatenated_df.set_index([concatenated_df.index, 'date'], drop=False, inplace=True)
print(concatenated_df['date'].loc['2020-09-30 21:00:18'])
