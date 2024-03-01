from __future__ import annotations

import sys
from typing import Callable

import pandas as pd
import yaml

from pandas_etl.extract import extract
from pandas_etl.load import load
from pandas_etl.transform import transform
from pandas_etl.utils.exceptions import ConfigurationError
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
        data = yaml.safe_load(file)

    if "extract" not in data:
        raise ConfigurationError("The plan must contain at least an 'extract' key.")

    for part in ["extract", "transform", "load"]:
        steps = data.get(part, [])

        if not isinstance(steps, list):
            raise ConfigurationError(f"The {part} part must be a list.")

        for i, step in enumerate(steps, start=1):
            if not isinstance(step, dict):
                raise ConfigurationError(f"The step {i} in the {part} part is not a dictionary.")
            if len(step) != 1:
                raise ConfigurationError(f"The step {i} in the {part} part must contain only one key.")

            _, params = list(step.items())[0]
            if not isinstance(params, dict):
                raise ConfigurationError(f"The parameters of the step {i} in the {part} part must be a dictionary.")

    return data


def _run(
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
        if on_failure and fail_fast:
            print_warning(f"Fail fast is enabled. Skipping remaining {description}.")
            break

        try:
            key, params = list(step.items())[0]
            datasets = func(key, params, datasets)
            print_success(f"{description.title()} {key} ran successfully.", i, total_loader)
        except Exception as e:
            print_error(f"Error running {description} {key}: {e}", i, total_loader)
            on_failure = True
    return datasets, on_failure


def main(path_plan: str, path_mermaid: str | None = None, fail_fast: bool = False):
    plan = load_plan(path_plan)

    if path_mermaid:
        from pandas_etl.utils.mermaid import generate_mermaid

        generate_mermaid(plan, path_mermaid)

    datasets: dict[str, pd.DataFrame] = {}

    datasets, on_failure = _run(datasets, plan["extract"], fail_fast, False, "extractors", extract)
    datasets, on_failure = _run(datasets, plan.get("transform", []), fail_fast, on_failure, "transformers", transform)
    _, on_failure = _run(datasets, plan.get("load", []), fail_fast, on_failure, "loaders", load)

    sys.exit(1 if on_failure else 0)


if __name__ == "__main__":
    main("tests/resources/example.yaml", path_mermaid="tests/resources/example.mermaid", fail_fast=True)
    # main("tests/resources/sqlite.yaml", path_mermaid="tests/resources/sqlite.mermaid", fail_fast=True)
