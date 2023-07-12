import pytest

from module_test.exemple_test import LogAnalyser


# To start the tests, simply run "pytest" into your terminal. You have to be at the root
# of your project.
class TestClass:
    def test_instance_and_init(self, log_analyser: LogAnalyser):
        assert isinstance(log_analyser, LogAnalyser)
        assert log_analyser.path_log

    def test_error_line_match(self, log_analyser: LogAnalyser):
        lines_matched = log_analyser.return_error_log()
        assert isinstance(lines_matched, list)
        assert len(lines_matched) == 2

    def test_wrong_amonth_of_matched_lines(self, log_analyser: LogAnalyser):
        lines_matched = log_analyser.return_error_log()
        with pytest.raises(Exception):
            # This MUST raise an Exception to succeed the test
            assert len(lines_matched) == 3