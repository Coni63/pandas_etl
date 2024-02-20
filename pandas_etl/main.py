from __future__ import annotations

import pandas as pd
import yaml

import pandas_etl.extract
import pandas_etl.load
import pandas_etl.transform
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


def run_extractors(datasets: dict[str, pd.DataFrame], extractors: list[dict], fail_fast: bool, on_failure: bool):
    print_section("EXTRACTORS")
    total_extractors = len(extractors)
    for i, extractor in enumerate(extractors, 1):
        if on_failure:
            print_warning("Fail fast is enabled. Skipping remaining extractors.")
            break

        try:
            key, params = list(extractor.items())[0]
            pandas_etl.extract.extract(key, params, datasets)
            print_success(f"Extractor {key} ran successfully.", i, total_extractors)
        except Exception as e:
            print_error(f"Error running extractor {key}: {e}", i, total_extractors)
            if fail_fast:
                on_failure = True
    return on_failure


def run_transformers(datasets: dict[str, pd.DataFrame], transformers: list[dict], fail_fast: bool, on_failure: bool):
    print_section("TRANSFORMERS")
    total_tranformer = len(transformers)
    for i, transformer in enumerate(transformers):
        if on_failure:
            print_warning("Fail fast is enabled. Skipping remaining transformers.")
            break

        try:
            key, params = list(transformer.items())[0]
            pandas_etl.transform.transform(key, params, datasets)
            print_success(f"Tranformation {key} ran successfully.", i, total_tranformer)
        except Exception as e:
            print_error(f"Error running extractor {key}: {e}", i, total_tranformer)
            if fail_fast:
                on_failure = True
    return on_failure


def run_loaders(datasets: dict[str, pd.DataFrame], loaders: list[dict], fail_fast: bool, on_failure: bool):
    print_section("LOADERS")
    total_loader = len(loaders)
    for i, loader in enumerate(loaders):
        if on_failure:
            print_warning("Fail fast is enabled. Skipping remaining loader.")
            break

        try:
            key, params = list(loader.items())[0]
            pandas_etl.load.load(key, params, datasets)
            print_success(f"Loader {key} ran successfully.", i, total_loader)
        except Exception as e:
            print_error(f"Error running extractor {key}: {e}", i, total_loader)
            if fail_fast:
                on_failure = True
    return on_failure


def main(path_plan: str, include_mermaid: bool = False, fail_fast: bool = False):
    plan = load_plan(path_plan)

    if include_mermaid:
        from pandas_etl.utils.mermaid import generate_mermaid

        target_path = path_plan.replace(".yaml", ".mermaid")
        generate_mermaid(plan, target_path)

    datasets: dict[str, pd.DataFrame] = {}

    on_failure = False
    on_failure = run_extractors(datasets, plan["extract"], fail_fast=fail_fast, on_failure=on_failure)
    on_failure = run_transformers(datasets, plan["transform"], fail_fast=fail_fast, on_failure=on_failure)
    on_failure = run_loaders(datasets, plan["load"], fail_fast=fail_fast, on_failure=on_failure)


if __name__ == "__main__":
    main("tests/resources/example.yaml", include_mermaid=True, fail_fast=True)
