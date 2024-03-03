from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def extract_excel(params: dict) -> pd.DataFrame:
    """
    Load the data from a json file.

    Args:
        params (dict): The parameters to load the data.

    Returns:
        pd.DataFrame: The loaded data.
    """
    if "path_or_buffer" in params:
        # Rename the parameter to the fit the other methods
        # If the user provide the proper command, no issue
        params["io"] = params["path_or_buffer"]
        del params["path_or_buffer"]

    params = filter_parameters(pd.read_excel, params)

    return pd.read_excel(**params)
