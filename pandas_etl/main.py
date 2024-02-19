from __future__ import annotations

import pandas as pd
import yaml


def load_plan(path_plan: str) -> dict:
    """
    Load the plan.

    Args:
        path_plan (str): The path to the plan.

    Returns:
        dict: The loaded plan.
    """
    with open(path_plan) as file:
        return yaml.safe_load(file)


def run_extractors(datasets: dict[str, pd.DataFrame], extractors: list[dict]):
    return


def run_transformers(datasets: dict[str, pd.DataFrame], transformers: list[dict]):
    return


def run_loaders(datasets: dict[str, pd.DataFrame], loaders: list[dict]):
    return


def main(path_plan: str, include_mermaid: bool = False):
    plan = load_plan(path_plan)

    from pprint import pprint

    pprint(plan)

    if include_mermaid:
        from pandas_etl.utils.mermaid import generate_mermaid

        target_path = path_plan.replace(".yaml", ".mermaid")
        generate_mermaid(plan, target_path)

    datasets: dict[str, pd.DataFrame] = {}

    run_extractors(datasets, plan["extract"])

    run_transformers(datasets, plan["transform"])

    run_loaders(datasets, plan["load"])


if __name__ == "__main__":
    main("tests/resources/example.yaml", True)
