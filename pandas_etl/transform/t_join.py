from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def _join(dfs: list[pd.DataFrame], params: dict) -> pd.DataFrame:
    """
    Join the data.

    Args:
        dfs (list[pd.DataFrame]): The data to join.
        params (dict): The parameters to join the data.
    """
    left, right = dfs

    filter_params = filter_parameters(pd.merge, params)
    del filter_params["left"]
    del filter_params["right"]

    return pd.merge(left, right, **filter_params)


def _concat(dfs: list[pd.DataFrame], params: dict) -> pd.DataFrame:
    """
    Concatenate the data.

    Args:
        dfs (list[pd.DataFrame]): The data to concatenate.
        params (dict): The parameters to concatenate the data.
    """

    filter_params = filter_parameters(pd.concat, params)
    if "objs" in filter_params:
        del filter_params["objs"]

    return pd.concat(dfs, **filter_params)
