from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def extract_csv(params: dict) -> pd.DataFrame:
    """
    Load the data from a CSV file.

    Args:
        params (dict): The parameters to load the data.

    Returns:
        pd.DataFrame: The loaded data.
    """
    params = filter_parameters(pd.read_csv, params)

    return pd.read_csv(**params)
