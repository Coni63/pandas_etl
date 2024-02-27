from __future__ import annotations

import pandas as pd

from .t_basic import _drop
from .t_basic import _filter
from .t_basic import _rename
from .t_join import _concat
from .t_join import _join
from pandas_etl.utils.exceptions import KeyMissingError


def transform(transform: str, params: dict, datasets: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """
    Load the data.

    Args:
        extractor (str): The extractor to use.
        params (dict): The parameters to load the data.
        datasets (dict[str, pd.DataFrame]): All datasets currently available.

    Returns:
        dict[str, pd.DataFrame]: The current state of the data.
    """
    mapping_func = {
        "join": _join,
        "concat": _concat,
        "rename": _rename,
        "drop": _drop,
        "filter": _filter,
    }

    try:
        if "sources" in params:
            dfs = [datasets[source] for source in params["sources"]]
            first_name = params["sources"][0]
        elif "left" in params and "right" in params:
            dfs = [datasets[params["left"]], datasets[params["right"]]]
            first_name = params["left"]
        elif "source" in params:
            dfs = datasets[params["source"]]
            first_name = params["source"]
            if "target" not in params:
                params["target"] = first_name
                params["inplace"] = True  # set the inplace for functions that support it
        else:
            raise KeyMissingError(
                "The step must contain a 'source' keys, a 'left & right' keys or 'sources' key with a list of sources.",
            )
    except KeyError as e:
        raise KeyMissingError(
            f"""Source '{e}' not available in existing datasets.
            This can be linked to invalid step order or typo in the plan file.""",
        )

    target_name = params.get("target", first_name)

    if transform not in mapping_func:
        raise NotImplementedError(f"Transformation '{transform}' not supported.")

    datasets[target_name] = mapping_func[transform](dfs, params)

    return datasets
