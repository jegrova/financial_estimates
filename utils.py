import glob
import pandas


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
    return data.loc[f'{year}-{month}-01':f'{year}-{month}-31']


def create_empty_df(date):
    """
    Method for creating empty output DataFrame

    Months and corresponding years are gather from input data,
    columns Income and Expenses are created and set to 0 in both cases.

    :param pandas.core.series.Series date: 'date' column in input data
    :return: empty output DataFrame
    :rtype: pandas.core.frame.DataFrame
    """
    month = pandas.DatetimeIndex(date).month
    year = pandas.DatetimeIndex(date).year
    unique_months = sorted(set(list(zip(month, year))))

    first_month = unique_months[0][0]
    first_year = unique_months[0][1]
    periods = len(unique_months)

    months = [d.strftime('%B-%Y') for d in
              pandas.date_range(start=f'{first_year}-{first_month}', freq='M', periods=periods)]
    return pandas.DataFrame(0, index=months, columns=['Income', 'Expenses'])
