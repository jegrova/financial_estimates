import datetime
import glob
import pandas


pandas.set_option('display.max_rows', None)


def get_all_reports():
    """
    Get all csv files in reports directory

    :return: csv files
    :rtype: list
    """
    return glob.glob("./reports/*.csv")


def gather_data(csv_files):
    """
    Retrieve all data from all csv files and store them in one dataframe

    :param list csv_files: csv files
    :return: data from csv files
    :rtype: pandas.core.frame.DataFrame
    """

    df_from_each_file = (pandas.read_csv(f, sep=';') for f in csv_files)
    df = pandas.concat(df_from_each_file, ignore_index=True)
    df = df.set_index(pandas.DatetimeIndex(df['date']))
    return df


def data_month_range(data, year, month):
    """
    Retrieve data for selected month and year

    :param DataFrame data: input data
    :param int year: selected year
    :param int month: selected month
    :return: data for selected month and year
    :rtype: pandas.core.frame.DataFrame
    """
    return data.loc[f'{year}-{month}']


def create_empty_df(date):
    """
    Method for creating empty output DataFrame

    Months and corresponding years are gather from input data,
    columns Income and Expenses are created and set to 0 in both cases.

    :param pandas.core.series.Series date: 'date' column in input data
    :return: empty output DataFrame
    :rtype: pandas.core.frame.DataFrame
    """
    unique_months = get_input_months(date)
    first_month = unique_months[0][0]
    first_year = unique_months[0][1]
    periods = len(unique_months)

    months = [d.strftime('%B-%Y') for d in
              pandas.date_range(start=f'{first_year}-{first_month}', freq='M', periods=periods)]
    return pandas.DataFrame(0.0, index=months, columns=['Income', 'Expenses'])


def get_input_months(date):
    """
    Get all months and corresponding years from input data

    :param pandas.core.series.Series date: 'date' column in input data
    :return: month and year tuples
    :rtype: list of tuples
    """
    month = pandas.DatetimeIndex(date).month
    year = pandas.DatetimeIndex(date).year
    return sorted(set(list(zip(month, year))))


def filter_category_income(data):
    """
    Get only the data that has category set to anything from the filter

    :param DataFrame data: input data
    :return: filtered data
    :rtype: pandas.core.frame.DataFrame
    """
    filter_income = ['Income', 'Checks, coupons', 'Child Support', 'Dues & grants', 'Gifts', 'Interests, dividends',
                     'Lending, renting', 'Lottery, gambling', 'Refunds (tax, purchase)', 'Rental income', 'Sale',
                     'Wage, invoices']
    return data[data['category'].isin(filter_income)]


def sum_amount(data):
    """
    Get sum of the data in 'ref_currency_amount' column

    :param DataFrame data: input data
    :return: sum of data amount column
    :rtype: float
    """
    return data['ref_currency_amount'].sum()


def income_month(data, year, month):
    """
    Get income for specific month

    :param DataFrame data: input data
    :param int year: selected year
    :param int month: selected month
    :return: income value for specific month
    :rtype: float
    """
    data_per_month = data_month_range(data, year, month)
    income_df = filter_category_income(data_per_month)
    return sum_amount(income_df)


def save_value_to_output(data, year, month, value):
    """
    Change Income value in DataFrame for specific month

    :param DataFrame data:
    :param int year: selected year
    :param int month: selected month
    :param value: output value
    :return: data with changed value
    :rtype: pandas.core.frame.DataFrame
    """
    month_str = datetime.date(year, month, 1).strftime('%B-%Y')
    data['Income'][month_str] = value
    return data
