from __future__ import annotations

import pandas as pd

from pandas_etl.load.l_excel import load_excel


def test_load_excel(mocker, datasets, temp_file):
    spy_to_excel = mocker.spy(pd.DataFrame, "to_excel")
    input_params = {"excel_writer": temp_file, "invalid_param": "invalid"}
    provided_params = {"excel_writer": temp_file}

    test_df = datasets["df1"]

    load_excel(test_df, input_params)
    spy_to_excel.assert_called_once_with(test_df, **provided_params)
