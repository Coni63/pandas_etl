from __future__ import annotations

import pandas as pd

from pandas_etl.utils.helper import filter_parameters


def _join(datasets: dict[str, pd.DataFrame], params: dict) -> dict[str, pd.DataFrame]:
    """
    Join the data.

    Args:
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
        params (dict): The parameters to join the data.
    """
    left = datasets[params["left"]]
    right = datasets[params["right"]]
    target_name = params.get("target", left)

    filter_params = filter_parameters(pd.merge, params)
    del filter_params["left"]
    del filter_params["right"]

    datasets[target_name] = pd.merge(left, right, **filter_params)
    return datasets


def _concat(datasets: dict[str, pd.DataFrame], params: dict) -> dict[str, pd.DataFrame]:
    """
    Concatenate the data.

    Args:
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
        params (dict): The parameters to concatenate the data.
    """
    dfs = [datasets[source] for source in params["sources"]]
    target_name = params["target"]

    filter_params = filter_parameters(pd.concat, params)
    if "objs" in filter_params:
        del filter_params["objs"]

    datasets[target_name] = pd.concat(dfs, **filter_params)
    return datasets
