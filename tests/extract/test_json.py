from __future__ import annotations

from io import StringIO

from pandas_etl.extract.e_json import extract_json


def test_extract_json(datasets):
    test_df = datasets["df1"]

    buffer = StringIO()
    test_df.to_json(buffer, orient="records")
    buffer.seek(0)

    params = {"path_or_buffer": buffer, "orient": "records"}

    df = extract_json(params)
    assert len(df) == 3
    assert len(df.columns) == 2
