from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def load_csv(df: pd.DataFrame, params: dict):
    """
    Save the given dataframe to CSV.

    Args:
        df (pd.DataFrame): The dataframe to save.
        params (dict): The parameters to load the data.
    """
    if "filepath_or_buffer" in params:
        # Rename the parameter to the fit the other methods
        # If the user provide the proper command, no issue
        params["path_or_buf"] = params["filepath_or_buffer"]
        del params["filepath_or_buffer"]

    filtered_params = filter_parameters(df.to_csv, params)
    df.to_csv(**filtered_params)
