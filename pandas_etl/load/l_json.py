from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def load_json(df: pd.DataFrame, params: dict):
    """
    Save the given dataframe to JSON.

    Args:
        df (pd.DataFrame): The dataframe to save.
        params (dict): The parameters to load the data.
    """
    filtered_params = filter_parameters(df.to_json, params)
    df.to_json(**filtered_params)
