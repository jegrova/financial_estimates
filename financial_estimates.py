import utils


csv_files = utils.get_all_reports()
df = utils.gather_data(csv_files)
output_df = utils.create_empty_df(df['date'])

months = utils.get_input_months(df['date'])
for (month, year) in months:
    income_sum = utils.income_month(df, year, month)
    output_df = utils.save_value_to_output(output_df, year, month, income_sum)

print(output_df)

# TODO create class data

# TODO celkem výdaje v měsící

# TODO součty každého měsíce podle budgetů
# TODO stav po každém měsíci podle budgetů

# TODO rozdíl v měsíci
# TODO procento neutracených peněz
# TODO měsíční zůstatek na účtu
# TODO měsíční průměr zůstatků na účtu
# TODO roční zůstatek po všech měsících
# TODO převést výpočty z sheetu
