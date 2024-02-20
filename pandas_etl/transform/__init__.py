from __future__ import annotations

import pandas as pd

from .t1 import t1
from .t_join import _concat
from .t_join import _join


def transform(transform: str, params: dict, datasets: dict[str, pd.DataFrame]):
    """
    Load the data.

    Args:
        extractor (str): The extractor to use.
        params (dict): The parameters to load the data.
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
    """
    match transform:
        case "t1":
            return t1(datasets, params)
        case "join":
            return _join(datasets, params)
        case "concat":
            return _concat(datasets, params)
        case _:
            return t1(datasets, params)
            # raise NotImplementedError(f"Transformation '{transform}' not supported.")
