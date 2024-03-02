from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def load_xml(df: pd.DataFrame, params: dict):
    """
    Save the given dataframe to XML.

    Args:
        df (pd.DataFrame): The dataframe to save.
        params (dict): The parameters to load the data.
    """
    if "path_or_buf" in params:
        # Rename the parameter to the fit the other methods
        # If the user provide the proper command, no issue
        params["path_or_buffer"] = params["path_or_buf"]
        del params["path_or_buf"]
    filtered_params = filter_parameters(df.to_xml, params)
    df.to_xml(**filtered_params)
