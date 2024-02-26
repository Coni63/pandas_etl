from __future__ import annotations

import pandas as pd
from sqlalchemy import create_engine

from pandas_etl.utils.helper import filter_parameters


def load_sql(df: pd.DataFrame, params: dict):
    """
    Save the given dataframe to CSV.

    Args:
        df (pd.DataFrame): The dataframe to save.
        params (dict): The parameters to load the data.
    """
    filtered_params = filter_parameters(df.to_sql, params)

    engine = create_engine(params["con"])

    del filtered_params["con"]
    if "name" in filtered_params:
        del filtered_params["name"]

    df.to_sql(name=params["tablename"], con=engine, **filtered_params)
