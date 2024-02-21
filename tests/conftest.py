from __future__ import annotations

import pandas as pd
import pytest


@pytest.fixture(name="datasets")
def get_datasets():
    return {
        "df1": pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}),
        "df2": pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]}),
    }
