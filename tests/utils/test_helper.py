from __future__ import annotations

import pytest

from pandas_etl.utils.helper import _format_message
from pandas_etl.utils.helper import filter_parameters


def foo(a, b=2, c=3, *args, **kwargs):
    return "foo"


@pytest.mark.parametrize(
    "input_params, output_params",
    [
        ({"a": 2, "b": "test"}, {"a": 2, "b": "test"}),
        ({"c": 2, "b": "test"}, {"c": 2, "b": "test"}),
        ({"other": "a"}, {}),
    ],
)
def test_inspect(input_params, output_params):
    assert filter_parameters(foo, input_params) == output_params


@pytest.mark.parametrize(
    "input_message, step, max_step, output_message",
    [
        ("test", None, None, "test"),
        ("test", 2, 3, "test...[2/3]"),
        ("test", 12, 13, "test.[12/13]"),
        ("too long message", 12, 13, "to...[12/13]"),
        ("too long message", None, None, "too long ..."),
    ],
)
def test_format_message(input_message, step, max_step, output_message):
    assert _format_message(input_message, step, max_step, 12) == output_message
