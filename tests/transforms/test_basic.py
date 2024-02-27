from __future__ import annotations

import pandas as pd
import pytest

from pandas_etl.transform.t_basic import _drop
from pandas_etl.transform.t_basic import _filter
from pandas_etl.transform.t_basic import _rename


@pytest.fixture()
def test_df() -> pd.DataFrame:
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.index = ["a", "b", "c"]
    return df


# RENAME


def test_rename_columns_inplace(test_df):
    params = {"columns": {"A": "X", "B": "Y"}, "inplace": True}
    _rename(test_df, params)
    assert list(test_df.columns) == ["X", "Y"]


def test_rename_columns_not_inplace(test_df):
    params = {"columns": {"A": "X", "B": "Y"}, "inplace": False}
    df2 = _rename(test_df, params)
    assert list(test_df.columns) == ["A", "B"]
    assert list(df2.columns) == ["X", "Y"]


def test_rename_index_inplace(test_df):
    params = {"index": {"a": "x", "b": "y"}, "inplace": True}
    _rename(test_df, params)
    assert list(test_df.index) == ["x", "y", "c"]


def test_rename_index_not_inplace(test_df):
    params = {"index": {"a": "x", "b": "y"}, "inplace": False}
    df2 = _rename(test_df, params)
    assert list(test_df.index) == ["a", "b", "c"]
    assert list(df2.index) == ["x", "y", "c"]


# DROP


def test_drop_columns_inplace(test_df):
    params = {"columns": ["A"], "inplace": True}
    _drop(test_df, params)
    assert list(test_df.columns) == ["B"]


def test_drop_columns_not_inplace_using_labels(test_df):
    params = {"labels": ["A"], "axis": 1, "inplace": False}
    df2 = _drop(test_df, params)
    assert list(test_df.columns) == ["A", "B"]
    assert list(df2.columns) == ["B"]


def test_drop_rows_inplace(test_df):
    params = {"labels": ["a", "b"], "axis": 0, "inplace": True}
    _drop(test_df, params)
    assert list(test_df.index) == ["c"]


def test_drop_rows_not_inplace(test_df):
    params = {"index": ["a", "b"], "inplace": False}
    df2 = _drop(test_df, params)
    assert list(test_df.index) == ["a", "b", "c"]
    assert list(df2.index) == ["c"]


# FILTER


def test_filter_inplace(test_df):
    params = {"expr": "A > 1", "inplace": True}
    _filter(test_df, params)
    assert len(test_df) == 2


def test_filter_not_inplace(test_df):
    params = {"expr": "A > 1", "inplace": False}
    df2 = _filter(test_df, params)
    assert len(test_df) == 3
    assert len(df2) == 2


def test_filter_no_expr(test_df):
    params = {"inplace": False}
    with pytest.raises(ValueError):
        _filter(test_df, params)
