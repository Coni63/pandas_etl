from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import load_custom_function


def _custom(dfs: pd.DataFrame | list[pd.DataFrame], params: dict) -> pd.DataFrame:
    """
    Call a custom function tha can accept multiple dataframes (use has to handle single dataframe process aswell).

    Args:
        datasets (pd.DataFrame | list[pd.DataFrame]): The dataframes provided to the custom function.
        params (dict): The parameters to join the data.

    Returns:
        pd.DataFrame: The processed dataframe.
    """
    func = load_custom_function(params)
    return func(dfs, params)
