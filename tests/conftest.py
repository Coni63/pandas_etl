from __future__ import annotations

import random
import shutil
import string
from pathlib import Path

import pandas as pd
import pytest

TMP_DIR = Path("tests/tmp")


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    TMP_DIR.mkdir(exist_ok=True)


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    shutil.rmtree(TMP_DIR)


@pytest.fixture(name="temp_file", scope="function")
def temp_file():
    suffix = "".join([random.choice(string.ascii_letters) for _ in range(10)])
    return TMP_DIR / f"temp_{suffix}.tmp"


@pytest.fixture(name="datasets")
def get_datasets():
    return {
        "df1": pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}),
        "df2": pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]}),
    }
