import pandas as pd
import numpy as np

min_rate = 0
max_rate = 0


def npv(seq_of_rates: np.array, data: pd.DataFrame) -> tuple:
    global min_rate
    global max_rate
    
    for a_rate in seq_of_rates:
        max_date = data['Date'].max()
        data['npv'] = data['Amount'] * ((1 + (a_rate / 100)) ** ((max_date - data['Date']).dt.days / 365))
        
        if data['Amount'].sum() > 0:
            if data['npv'].sum() > 0:
                min_rate = a_rate
            else:
                max_rate = a_rate
                break
        else:
            if data['npv'].sum() < 0:
                min_rate = a_rate
            else:
                max_rate = a_rate
                break
    
    return min_rate, max_rate


def xirr(data: pd.DataFrame) -> float:
    
    """
    Parameters
    -----------
    data: a pandas dataframe
        This dataframe should have only two columns: one with dates and other with amount.
        The amount should be negative if it is a debit transaction and positive if it is a credit transaction.
        Example:
            Date	    Amount
            01/01/2010	-10000
            01/01/2011	-20000
            01/01/2016	-10000
            01/01/2017	-10000
            01/01/2018	 60000
    
    Returns
    -------
    a float with accuracy of up to 4 decimals
        Example: 3.6032
            That is, the XIRR return for the transactions in the above example is 3.6032%
    """
    
    # Finding out which column contains Date and Amount
    try:
        data.iloc[:, 0].astype(float)
        col_names = ['Amount', 'Date']
    except Exception as _:
        col_names = ['Date', 'Amount']
    
    # Renaming the columns accordingly and converting to correct data types
    data.columns = col_names
    data = data.assign(Date = pd.to_datetime(arg = data['Date'], infer_datetime_format = True, dayfirst = True).dt.date,
                       Amount = data['Amount'].astype(float))
    
    if data['Amount'].sum() > 0:
        step_values = [100, 10, 1, 0.01, 0.001, 0.0001]
        stop = 10000
    else:
        step_values = [-100, -10, -1, -0.01, -0.001, -0.0001]
        stop = -10000
    
    start = 0
    for i in range(len(step_values)):
        seq_of_rates = np.arange(start = start, stop = stop, step = step_values[i])
        start, stop = npv(seq_of_rates, data)
    
    return (start + stop) / 2


if __name__ == '__main__':
    file_path = input('Enter the path to csv file (eg., C:/Desktop/data.csv): ')
    data = pd.read_csv(file_path)
    print(f'XIRR return is {round(xirr(data), 5)} %')
