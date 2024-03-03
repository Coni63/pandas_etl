from __future__ import annotations

from io import StringIO

from pandas_etl.extract.e_xml import extract_xml


def test_extract_json():
    data_xml = """<?xml version='1.0' encoding='utf-8'?>
    <data xmlns="http://example.com">
        <row>
            <shape>square</shape>
            <degrees>360</degrees>
            <sides>4.0</sides>
        </row>
        <row>
            <shape>circle</shape>
            <degrees>360</degrees>
            <sides/>
        </row>
        <row>
            <shape>triangle</shape>
            <degrees>180</degrees>
            <sides>3.0</sides>
        </row>
    </data>
    """
    buffer = StringIO(data_xml)
    params = {"path_or_buffer": buffer}

    df = extract_xml(params)
    assert len(df) == 3
    assert len(df.columns) == 3
