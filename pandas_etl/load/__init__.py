from __future__ import annotations

import pandas as pd

from .l_csv import load_csv
from .l_sql import load_sql


def load(loader: str, params: dict, datasets: dict[str, pd.DataFrame]):
    """
    Load the data.

    Args:
        extractor (str): The extractor to use.
        params (dict): The parameters to load the data.
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
    """
    mapping = {
        "csv": load_csv,
        "sql": load_sql,
    }

    df = datasets[params["source"]]

    if loader not in mapping:
        raise NotImplementedError(f"Loader '{loader}' not supported.")

    mapping[loader](df, params)
