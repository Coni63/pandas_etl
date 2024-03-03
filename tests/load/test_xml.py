from __future__ import annotations

import pandas as pd

from pandas_etl.load.l_xml import load_xml


def test_load_xml_renamed_key(mocker, datasets, temp_file):
    spy_to_xml = mocker.spy(pd.DataFrame, "to_xml")
    input_params = {"filepath_or_buffer": temp_file, "invalid_param": "invalid"}
    provided_params = {"path_or_buffer": temp_file}

    test_df = datasets["df1"]

    load_xml(test_df, input_params)
    spy_to_xml.assert_called_once_with(test_df, **provided_params)


def test_load_xml_rename_buffer(mocker, datasets, temp_file):
    spy_to_xml = mocker.spy(pd.DataFrame, "to_xml")
    input_params = {"path_or_buffer": temp_file, "invalid_param": "invalid"}
    provided_params = {"path_or_buffer": temp_file}

    test_df = datasets["df1"]

    load_xml(test_df, input_params)
    spy_to_xml.assert_called_once_with(test_df, **provided_params)
