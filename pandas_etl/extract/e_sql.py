from __future__ import annotations

import pandas as pd
from sqlalchemy import create_engine

from pandas_etl.utils.helper import filter_parameters


def extract_sql(params: dict) -> pd.DataFrame:
    """
    Load the data from a database.

    Args:
        params (dict): The parameters to load the data.

    Returns:
        pd.DataFrame: The loaded data.
    """
    try:
        engine = create_engine(params["con"])

        filtered_params = filter_parameters(pd.read_sql, params)
        del filtered_params["con"]

        return pd.read_sql(con=engine, **filtered_params)
    except Exception as e:
        raise e
    finally:
        engine.dispose()
