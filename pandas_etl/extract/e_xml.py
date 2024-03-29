from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def extract_xml(params: dict) -> pd.DataFrame:
    """
    Load the data from an xml file.

    Args:
        params (dict): The parameters to load the data.

    Returns:
        pd.DataFrame: The loaded data.
    """
    params = filter_parameters(pd.read_xml, params)

    return pd.read_xml(**params)
