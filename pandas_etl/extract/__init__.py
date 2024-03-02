from __future__ import annotations

import pandas as pd

from .e_csv import extract_csv
from .e_excel import extract_excel
from .e_json import extract_json
from .e_sql import extract_sql
from .e_xml import extract_xml
from pandas_etl.utils.exceptions import KeyMissingError


def extract(extractor: str, params: dict, datasets: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """
    Load the data.

    Args:
        extractor (str): The extractor to use.
        params (dict): The parameters to load the data.
        datasets (dict[str, pd.DataFrame]): All datasets currently available.

    Returns:
        dict[str, pd.DataFrame]: The current state of the data.
    """
    mapping = {
        "csv": extract_csv,
        "sql": extract_sql,
        "excel": extract_excel,
        "json": extract_json,
        "xml": extract_xml,
    }

    if extractor not in mapping:
        raise NotImplementedError(f"Extractor '{extractor}' not supported.")

    if "name" not in params:
        raise KeyMissingError("The step must contain a 'name' key (dataset name for later transformations).")

    dataset_name = params["name"]
    datasets[dataset_name] = mapping[extractor](params)

    return datasets
