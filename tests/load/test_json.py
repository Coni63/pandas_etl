from __future__ import annotations

import pandas as pd

from pandas_etl.load.l_json import load_json


def test_load_json(mocker, datasets, temp_file):
    spy_to_json = mocker.spy(pd.DataFrame, "to_json")
    input_params = {"path_or_buf": temp_file, "invalid_param": "invalid"}
    provided_params = {"path_or_buf": temp_file}

    test_df = datasets["df1"]

    load_json(test_df, input_params)
    spy_to_json.assert_called_once_with(test_df, **provided_params)
