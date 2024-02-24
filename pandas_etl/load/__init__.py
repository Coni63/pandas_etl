from __future__ import annotations

import pandas as pd

from .l_csv import load_csv


def load(loader: str, params: dict, datasets: dict[str, pd.DataFrame]):
    """
    Load the data.

    Args:
        extractor (str): The extractor to use.
        params (dict): The parameters to load the data.
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
    """
    df = datasets[params["source"]]
    match loader:
        case "csv":
            return load_csv(df, params)
        case _:
            raise NotImplementedError(f"Loader '{loader}' not supported.")
