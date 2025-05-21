def dataconverter(file):
    """
    Places file into a dataframe

    Parameters
    ----------
    file : *.csv
    Return
    ------
    df : array
        .csv file in a data frame
    """
    import pandas as pd
    filename = file
    df = pd.read_csv(file, na_values=-999)
    return(df)