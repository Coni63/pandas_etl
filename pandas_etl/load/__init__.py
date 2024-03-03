from __future__ import annotations

import pandas as pd

from .l_csv import load_csv
from .l_custom import load_custom
from .l_excel import load_excel
from .l_json import load_json
from .l_sql import load_sql
from .l_xml import load_xml
from pandas_etl.utils.exceptions import KeyMissingError


def load(loader: str, params: dict, datasets: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
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
        "csv": load_csv,
        "sql": load_sql,
        "excel": load_excel,
        "json": load_json,
        "xml": load_xml,
        "custom": load_custom,
    }

    if "source" not in params:
        raise KeyMissingError("The step must contain a 'source' key (dataset to save).")

    try:
        df = datasets[params["source"]]
    except KeyError as e:
        raise KeyMissingError(
            f"""Source '{e}' not available in existing datasets.
            This can be linked to invalid step order or typo in the plan file.""",
        )

    if loader not in mapping:
        raise NotImplementedError(f"Loader '{loader}' not supported.")

    mapping[loader](df, params)

    return datasets
