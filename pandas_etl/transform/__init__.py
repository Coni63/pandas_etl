from __future__ import annotations

import pandas as pd

from .t1 import func1
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
    mapping_func = {
        "t1": func1,
        "join": _join,
        "concat": _concat,
        "t2": func1,
    }

    if "sources" in params:
        dfs = [datasets[source] for source in params["sources"]]
        first_name = params["sources"][0]
    elif "left" in params and "right" in params:
        dfs = [datasets[params["left"]], datasets[params["right"]]]
        first_name = params["left"]
    elif "source" in params:
        dfs = datasets[params["source"]]
        first_name = params["source"]
    else:
        raise ValueError("Invalid/Missing parameters for DataFrameTransformer")

    target_name = params.get("target", first_name)

    if transform not in mapping_func:
        raise NotImplementedError(f"Transformation '{transform}' not supported.")

    datasets[target_name] = mapping_func[transform](dfs, params)
