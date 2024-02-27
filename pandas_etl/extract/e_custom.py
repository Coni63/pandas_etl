from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import load_custom_function


def extract_custom(params: dict) -> pd.DataFrame:
    """
    Call a custom function to load the data.

    Args:
        params (dict): The parameters to load the data.
    """
    func = load_custom_function(params)

    return func(params)
