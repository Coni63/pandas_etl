from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import load_custom_function


def load_custom(df: pd.DataFrame, params: dict):
    """
    Save the given dataframe to CSV.

    Args:
        df (pd.DataFrame): The dataframe to save.
        params (dict): The parameters to load the data.
    """
    func = load_custom_function(params)
    return func(df, params)
