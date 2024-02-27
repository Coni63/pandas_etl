from __future__ import annotations

import pandas as pd
import pytest

from pandas_etl.transform.t_join import _concat
from pandas_etl.transform.t_join import _join


@pytest.fixture()
def test_dfs() -> list[pd.DataFrame]:
    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df2 = pd.DataFrame({"C": [1, 2, 4], "D": [10, 11, 12]})
    return [df1, df2]


def test_join(test_dfs):
    left, right = test_dfs
    params = {"left": left, "right": right, "left_on": "A", "right_on": "C", "how": "outer"}
    df = _join(test_dfs, params)
    assert list(df.columns) == ["A", "B", "C", "D"]
    assert df.shape == (4, 4)


def test_join_on(test_dfs):
    test_dfs[0].index = ["a", "b", "c"]
    test_dfs[1].index = ["b", "c", "d"]
    params = {"left_index": True, "right_index": True, "how": "inner"}
    df = _join(test_dfs, params)
    assert list(df.columns) == ["A", "B", "C", "D"]
    assert df.shape == (2, 4)


def test_join_no_params(test_dfs):
    with pytest.raises(pd.errors.MergeError):
        _join(test_dfs, {})


def test_concat(test_dfs):
    params = {"axis": 0}
    df = _concat(test_dfs, params)
    assert list(df.columns) == ["A", "B", "C", "D"]
    assert df.shape == (6, 4)


def test_concat_axis_1(test_dfs):
    params = {"axis": 1, "objs": test_dfs}
    df = _concat(test_dfs, params)
    assert list(df.columns) == ["A", "B", "C", "D"]
    assert df.shape == (3, 4)


def test_concat_no_params(test_dfs):
    df = _concat(test_dfs, {})
    assert list(df.columns) == ["A", "B", "C", "D"]
    assert df.shape == (6, 4)
