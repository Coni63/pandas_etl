from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def _join(dfs: list[pd.DataFrame], params: dict) -> pd.DataFrame:
    """
    Join the 2 dataframes from dfs.

    Args:
        dfs (list[pd.DataFrame]): The data to join.
        params (dict): The parameters to join the data.

    Returns:
        pd.DataFrame: The joined data.
    """
    left, right = dfs

    filter_params = filter_parameters(pd.merge, params)

    # Remove the left and right parameters as they are already provided in function call as args
    if "left" in filter_params:
        del filter_params["left"]
    if "right" in filter_params:
        del filter_params["right"]

    return pd.merge(left, right, **filter_params)


def _concat(dfs: list[pd.DataFrame], params: dict) -> pd.DataFrame:
    """
    Concatenate the data.

    Args:
        dfs (list[pd.DataFrame]): The data to concatenate.
        params (dict): The parameters to concatenate the data.

    Returns:
        pd.DataFrame: The concatenated data.
    """
    filter_params = filter_parameters(pd.concat, params)
    if "objs" in filter_params:
        del filter_params["objs"]

    return pd.concat(dfs, **filter_params)
