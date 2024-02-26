from __future__ import annotations

import sys
from typing import Callable

import pandas as pd
import yaml

from pandas_etl.extract import extract
from pandas_etl.load import load
from pandas_etl.transform import transform
from pandas_etl.utils.helper import print_error
from pandas_etl.utils.helper import print_section
from pandas_etl.utils.helper import print_success
from pandas_etl.utils.helper import print_warning


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


def run(
    datasets: dict[str, pd.DataFrame],
    steps: list[dict],
    fail_fast: bool,
    on_failure: bool,
    description: str,
    func: Callable,
):
    print_section(description.upper())
    total_loader = len(steps)
    for i, step in enumerate(steps):
        if on_failure:
            print_warning(f"Fail fast is enabled. Skipping remaining {description}.")
            break

        try:
            key, params = list(step.items())[0]
            func(key, params, datasets)
            print_success(f"{description.title()} {key} ran successfully.", i, total_loader)
        except Exception as e:
            print_error(f"Error running {description} {key}: {e}", i, total_loader)
            if fail_fast:
                on_failure = True
    return on_failure


def main(path_plan: str, path_mermaid: str | None = None, fail_fast: bool = False):
    plan = load_plan(path_plan)

    if path_mermaid:
        from pandas_etl.utils.mermaid import generate_mermaid

        generate_mermaid(plan, path_mermaid)

    datasets: dict[str, pd.DataFrame] = {}

    on_failure = run(datasets, plan["extract"], fail_fast, False, "extractors", extract)
    on_failure = run(datasets, plan.get("transform", []), fail_fast, on_failure, "transformers", transform)
    on_failure = run(datasets, plan.get("load", []), fail_fast, on_failure, "loaders", load)

    sys.exit(1 if on_failure else 0)


if __name__ == "__main__":
    main("tests/resources/sqlite.yaml", path_mermaid="tests/resources/sqlite.mermaid", fail_fast=True)
