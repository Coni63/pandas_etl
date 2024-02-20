from __future__ import annotations

import pandas as pd


def t1(datasets: dict[str, pd.DataFrame], params: dict):
    """
    Transform the data.

    Args:
        datasets (dict[str, pd.DataFrame]): All datasets currently available.
        params (dict): The parameters to transform the data.
    """
    df = datasets[params["source"]]
    target_name = params.get("target", params["source"])
    # Do something with the dataframe
    datasets[target_name] = df
