from __future__ import annotations

from pandas_etl.extract.e_csv import extract_csv


def test_extract_csv_invalid_param():
    input_params = {"filepath_or_buffer": "tests/resources/source_a.csv", "invalid_param": "invalid"}

    df = extract_csv(input_params)
    assert len(df) == 2
    assert len(df.columns) == 1


def test_extract_csv_valid_param():
    input_params = {"filepath_or_buffer": "tests/resources/source_a.csv", "sep": ";"}

    df = extract_csv(input_params)
    assert len(df) == 2
    assert len(df.columns) == 2
