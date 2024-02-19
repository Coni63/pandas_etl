from __future__ import annotations

import pandas as pd

from .extract_csv import load_csv


def load(extractor: str, params: dict) -> pd.DataFrame:
    """
    Load the data.

    Args:
        params (dict): The parameters to load the data.

    Returns:
        pd.DataFrame: The loaded data.
    """
    match extractor:
        case "csv":
            return load_csv(params)
        case _:
            raise NotImplementedError(f"Extractor '{extractor}' not supported.")
