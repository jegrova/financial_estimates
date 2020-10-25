#!/usr/bin/env python3

import utils

csv_files = utils.get_all_reports()
df = utils.gather_data(csv_files)
output_df = utils.create_empty_df(df['date'])
print(output_df)

january = utils.data_month_range(df, 2020, 1)
print(january)

# TODO součty každého měsíce podle budgetů
# TODO stav po každém měsíci podle budgetů
# TODO celkem příjmy v měsíci
# TODO celkem výdaje v měsící
# TODO rozdíl v měsíci
# TODO procento neutracených peněz
# TODO měsíční zůstatek na účtu
# TODO měsíční průměr zůstatků na účtu
# TODO roční zůstatek po všech měsících
# TODO převést výpočty z sheetu
