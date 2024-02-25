from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def _rename(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    filter_params = filter_parameters(df.rename, params)

    if params.get("inplace", False):
        df.rename(**filter_params)
        return df

    return df.rename(**filter_params)


def _drop(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    filter_params = filter_parameters(df.drop, params)

    if params.get("inplace", False):
        df.drop(**filter_params)
        return df

    return df.drop(**filter_params)


def _filter(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    if "expr" not in params:
        raise ValueError("No 'expr' provided.")

    if params.get("inplace", False):
        df.query(params["expr"], inplace=True)
        return df

    return df.query(params["expr"])
