def data_cleaner (dataframe):
    """
    Converts data frame into float and adds NaN value to blank cells

    Parameters
    ----------
    dataframe : object, float, or numpy array
        Data frame as an object or missing values
    Return
    ------
    cleaned : float
        Data frame as a float with NaN values added
    """
    import pandas as pd
    cleaned = pd.to_numeric(dataframe, errors='coerce')
    return(cleaned)