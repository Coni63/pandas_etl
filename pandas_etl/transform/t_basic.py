from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def _rename(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """
    Rename the rows / columns of the dataframe.

    Args:
        df (pd.DataFrame): The dataframe to rename.
        params (dict): The parameters to rename the dataframe.

    Returns:
        pd.DataFrame: The renamed dataframe (inplace or shallow copy).
    """
    filter_params = filter_parameters(df.rename, params)

    if params.get("inplace", False):
        df.rename(**filter_params)
        return df

    return df.rename(**filter_params)


def _drop(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """
    Drop some rows / columns of the dataframe.

    Args:
        df (pd.DataFrame): The dataframe to drop.
        params (dict): The parameters to drop the dataframe.

    Returns:
        pd.DataFrame: The dropped dataframe (inplace or shallow copy).
    """
    filter_params = filter_parameters(df.drop, params)

    if params.get("inplace", False):
        df.drop(**filter_params)
        return df

    return df.drop(**filter_params)


def _filter(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """
    Filter the dataframe according to the 'expr' parameter.

    Args:
        df (pd.DataFrame): The dataframe to filter.
        params (dict): The parameters to filter the dataframe.

    Returns:
        pd.DataFrame: The filtered dataframe (inplace or shallow copy).
    """
    if "expr" not in params:
        raise ValueError("No 'expr' provided.")

    if params.get("inplace", False):
        df.query(params["expr"], inplace=True)
        return df

    return df.query(params["expr"])
