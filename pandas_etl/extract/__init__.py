from __future__ import annotations

import pandas as pd

from .e_csv import load_csv
from .e_sql import load_sql


def extract(extractor: str, params: dict, datasets: dict[str, pd.DataFrame]):
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

    if extractor not in mapping:
        raise NotImplementedError(f"Extractor '{extractor}' not supported.")

    dataset_name = params["name"]
    datasets[dataset_name] = mapping[extractor](params)
