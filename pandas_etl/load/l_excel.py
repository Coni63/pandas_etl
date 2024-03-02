from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def load_excel(df: pd.DataFrame, params: dict):
    """
    Save the given dataframe to Excel.

    Args:
        df (pd.DataFrame): The dataframe to save.
        params (dict): The parameters to load the data.
    """
    filtered_params = filter_parameters(df.to_excel, params)
    df.to_excel(**filtered_params)
