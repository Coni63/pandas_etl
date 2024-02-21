from __future__ import annotations

import pandas as pd


def DataFrameTransformer(func):
    def wrapper(datasets: dict[str, pd.DataFrame], params: dict) -> dict[str, pd.DataFrame]:
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

        datasets[target_name] = func(dfs, params)

        return datasets

    return wrapper
