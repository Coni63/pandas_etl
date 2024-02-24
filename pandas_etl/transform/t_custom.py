from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import load_custom_function


def _custom(dfs: list[pd.DataFrame], params: dict) -> pd.DataFrame:
    """
    Join the data.

    Args:
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
        params (dict): The parameters to join the data.
    """
    func = load_custom_function(params)
    return func(dfs, params)
