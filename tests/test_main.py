from __future__ import annotations

from unittest.mock import mock_open
from unittest.mock import patch

import pandas as pd
import pytest

from pandas_etl.main import load_plan
from pandas_etl.main import main
from pandas_etl.utils.exceptions import ConfigurationError

# load_plan


def test_load_plan_success():
    mock_yaml_file = """
    extract:
      - step1: {}
    transform:
      - step2: {}
    load:
      - step3: {}
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_file)):
        result = load_plan("dummy_path")
    assert "extract" in result
    assert "transform" in result
    assert "load" in result


def test_load_plan_no_extract_key():
    mock_yaml_file = """
    transform:
      - step2: {}
    load:
      - step3: {}
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_file)):
        with pytest.raises(ConfigurationError, match="The plan must contain at least an 'extract' key."):
            load_plan("dummy_path")


def test_load_plan_part_not_list():
    mock_yaml_file = """
    extract: "not a list"
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_file)):
        with pytest.raises(ConfigurationError, match="The extract part must be a list."):
            load_plan("dummy_path")


def test_load_plan_step_not_dict():
    mock_yaml_file = """
    extract:
      - "not a dict"
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_file)):
        with pytest.raises(ConfigurationError, match="The step 1 in the extract part is not a dictionary."):
            load_plan("dummy_path")


def test_load_plan_step_more_than_one_key():
    mock_yaml_file = """
    extract:
      - step1: {}
        step2: {}
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_file)):
        with pytest.raises(ConfigurationError, match="The step 1 in the extract part must contain only one key."):
            load_plan("dummy_path")


def test_load_plan_params_not_dict():
    mock_yaml_file = """
    extract:
      - step1: "not a dict"
    """
    with patch("builtins.open", mock_open(read_data=mock_yaml_file)):
        with pytest.raises(
            ConfigurationError,
            match="The parameters of the step 1 in the extract part must be a dictionary.",
        ):
            load_plan("dummy_path")


# main


def test_main(mocker):
    mock_load_plan = mocker.patch(
        "pandas_etl.main.load_plan",
        return_value={
            "extract": [{"step1": {}}],
            "transform": [{"step2": {}}],
            "load": [{"step3": {}}],
        },
    )
    mock_extract = mocker.patch("pandas_etl.main.extract", return_value={"dataset1": pd.DataFrame()})
    mock_transform = mocker.patch(
        "pandas_etl.main.transform",
        return_value={"dataset1": pd.DataFrame(), "dataset2": pd.DataFrame()},
    )
    mock_load = mocker.patch("pandas_etl.main.load", return_value=None)
    mock_generate_mermaid = mocker.patch("pandas_etl.utils.mermaid.generate_mermaid")
    mock_exit = mocker.patch("sys.exit")

    main("dummy_path", "dummy_mermaid_path", True)

    mock_load_plan.assert_called_once_with("dummy_path")
    mock_generate_mermaid.assert_called_once_with(mock_load_plan.return_value, "dummy_mermaid_path")
    mock_extract.assert_called_once_with("step1", {}, {})

    mock_transform.assert_called_once()
    mock_transform.call_args[0][0] == "step2"
    mock_transform.call_args[0][1] == {}
    assert "dataset1" in mock_transform.call_args[0][2]

    mock_load.assert_called_once()
    mock_load.call_args[0][0] == "step3"
    mock_load.call_args[0][1] == {}
    assert "dataset1" in mock_load.call_args[0][2]
    assert "dataset2" in mock_load.call_args[0][2]

    mock_exit.assert_called_once_with(0)


def test_main_error(mocker):
    mock_load_plan = mocker.patch(
        "pandas_etl.main.load_plan",
        return_value={
            "extract": [{"step1": {}}],
            "transform": [{"step2": {}}],
            "load": [{"step3": {}}],
        },
    )
    mock_extract = mocker.patch("pandas_etl.main.extract", side_effect=Exception("error"))
    mock_transform = mocker.patch(
        "pandas_etl.main.transform",
        return_value={"dataset1": pd.DataFrame(), "dataset2": pd.DataFrame()},
    )
    mock_load = mocker.patch("pandas_etl.main.load", return_value=None)
    mocker.patch("pandas_etl.utils.mermaid.generate_mermaid")
    mock_exit = mocker.patch("sys.exit")

    main("dummy_path", "dummy_mermaid_path", fail_fast=True)

    mock_load_plan.assert_called_once()
    mock_extract.assert_called_once()
    mock_transform.assert_not_called()
    mock_load.assert_not_called()

    mock_exit.assert_called_once_with(1)


def test_main_error_wo_fail_fast(mocker):
    mock_load_plan = mocker.patch(
        "pandas_etl.main.load_plan",
        return_value={
            "extract": [{"step1": {}}],
            "transform": [{"step2": {}}],
            "load": [{"step3": {}}],
        },
    )
    mock_extract = mocker.patch("pandas_etl.main.extract", side_effect=Exception("error"))
    mock_mermaid = mocker.patch("pandas_etl.utils.mermaid.generate_mermaid")
    mock_transform = mocker.patch(
        "pandas_etl.main.transform",
        return_value={"dataset1": pd.DataFrame(), "dataset2": pd.DataFrame()},
    )
    mock_load = mocker.patch("pandas_etl.main.load", return_value=None)
    mock_exit = mocker.patch("sys.exit")

    main("dummy_path", "dummy_mermaid_path", fail_fast=False)

    mock_load_plan.assert_called_once()
    mock_extract.assert_called_once()
    mock_mermaid.assert_called_once()
    mock_transform.assert_called_once()
    mock_load.assert_called_once()

    mock_exit.assert_called_once_with(1)
