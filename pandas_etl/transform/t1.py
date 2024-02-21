from __future__ import annotations

import pandas as pd

from pandas_etl.utils.decorator import DataFrameTransformer


@DataFrameTransformer
def t1(df: pd.DataFrame, params: dict):
    """
    Dummy function during development.
    """
    return df
