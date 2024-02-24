from __future__ import annotations

import pandas as pd

from .e_csv import load_csv


def extract(extractor: str, params: dict, datasets: dict[str, pd.DataFrame]):
    """
    Load the data.

    Args:
        extractor (str): The extractor to use.
        params (dict): The parameters to load the data.
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
    """
    match extractor:
        case "csv":
            dataset_name = params["name"]
            datasets[dataset_name] = load_csv(params)
        case _:
            raise NotImplementedError(f"Extractor '{extractor}' not supported.")
