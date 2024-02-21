from __future__ import annotations

import pytest

from pandas_etl.transform.t_custom import _custom


def test_custom_valid_func(datasets):
    params = {"func": "tests.resources.custom_script.foo", "source": "df1"}
    result = _custom(datasets, params)
    # check the dataset due to decorator
    assert len(result) == 2
    assert isinstance(result, dict)


def test_custom_invalid_func(datasets):
    params = {"func": "dummy_module.dummy_func"}
    with pytest.raises(ValueError):
        _custom(datasets, params)
