import pytest
import pathlib
import os

from module_test.exemple_test import LogAnalyser


@pytest.fixture(scope="session")
def path_log():
    root_file = pathlib.Path(__file__).parent.parent.resolve()
    return os.path.join(root_file, "text_files", "fake_logs.txt")


@pytest.fixture(scope="session")
def log_analyser(path_log: str):
    return LogAnalyser(path_log)