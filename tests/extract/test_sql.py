from __future__ import annotations

from pandas_etl.extract.e_sql import extract_sql
from pandas_etl.load.l_sql import load_sql


def test_load_sql(temp_file, datasets):
    test_df = datasets["df1"]

    conn = f"sqlite:///{temp_file}"

    # this is tested in tests/load/test_sql.py
    # just create the table
    load_sql(test_df, {"con": conn, "tablename": "test", "index": False})

    df = extract_sql({"con": conn, "sql": "SELECT * FROM test"})
    assert len(df) == 3
    assert len(df.columns) == 2
