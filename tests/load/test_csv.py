from __future__ import annotations

import pandas as pd

from pandas_etl.load.l_csv import load_csv


def test_load_csv(mocker, datasets, temp_file):
    spy_to_csv = mocker.spy(pd.DataFrame, "to_csv")
    input_params = {"path_or_buf": temp_file, "invalid_param": "invalid"}
    provided_params = {"path_or_buf": temp_file}

    test_df = datasets["df1"]

    load_csv(test_df, input_params)
    spy_to_csv.assert_called_once_with(test_df, **provided_params)
