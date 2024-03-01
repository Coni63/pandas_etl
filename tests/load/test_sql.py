from __future__ import annotations

import sqlite3

from pandas_etl.load.l_sql import load_sql


def test_load_sql(temp_file, datasets):
    test_df = datasets["df1"]

    conn = f"sqlite:///{temp_file}"
    load_sql(test_df, {"con": conn, "tablename": "test"})

    with sqlite3.connect(temp_file) as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM test")
        result = cur.fetchone()
        assert result[0] == 3
