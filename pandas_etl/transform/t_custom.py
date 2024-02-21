from __future__ import annotations

import importlib

import pandas as pd

from pandas_etl.utils.decorator import DataFrameTransformer


@DataFrameTransformer
def _custom(dfs: list[pd.DataFrame], params: dict) -> pd.DataFrame:
    """
    Join the data.

    Args:
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
        params (dict): The parameters to join the data.
    """
    if "func" not in params:
        raise ValueError("for custom function, 'func' is required.")

    module_name, func_name = params["func"].rsplit(".", 1)
    try:
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
        func(dfs, params)
    except (ImportError, AttributeError) as e:
        raise ValueError(f"Error loading function '{func_name}' in {module_name}, {e}")
