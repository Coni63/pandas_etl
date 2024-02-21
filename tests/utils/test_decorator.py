from __future__ import annotations

import pandas as pd
import pytest

from pandas_etl.utils.decorator import DataFrameTransformer


@DataFrameTransformer
def dummy_func(dfs, params):
    if isinstance(dfs, list):
        return pd.concat(dfs)
    else:
        return dfs


def test_DataFrameTransformer_with_sources(datasets):
    params = {"sources": ["df1", "df2"], "target": "df3"}
    result = dummy_func(datasets, params)
    assert "df3" in result
    assert len(result["df3"]) == 6


def test_DataFrameTransformer_left_right(datasets):
    params = {"left": "df1", "right": "df2"}
    result = dummy_func(datasets, params)
    assert len(result["df1"]) == 6


def test_DataFrameTransformer_source(datasets):
    params = {"source": "df1"}
    result = dummy_func(datasets, params)
    assert "df1" in result
    assert len(result["df1"]) == 3


def test_DataFrameTransformer_no_params(datasets):
    params = {"source": "df1", "target": "df3"}
    result = dummy_func(datasets, params)
    assert "df3" in result
    assert len(result["df3"]) == 3


def test_DataFrameTransformer_no_params_error(datasets):
    params = {}
    with pytest.raises(ValueError):
        dummy_func(datasets, params)
