import re
import pathlib
import os


class LogAnalyser:
    def __init__(self, path_log: str):
        self.path_log = path_log

    def return_error_log(self) -> list[str]:
        error_regex = re.compile("%ERROR.*")
        with open(self.path_log, "r") as file_log:
            text = file_log.read()
        lines_matched = error_regex.findall(text)
        print(lines_matched)
        return lines_matched

    def return_warning_log(self) -> list[str]:
        pass



if __name__ == "__main__":
    root_file = pathlib.Path(__file__).parent.parent.resolve()
    path = os.path.join(root_file, "text_files", "fake_logs.txt")
    # test LogAnalyser class
    instance = LogAnalyser(path)
    assert isinstance(instance, LogAnalyser)
    assert instance.path_log
    lines_matched = instance.return_error_log()
    assert isinstance(lines_matched, list)
    assert len(lines_matched) == 2
    # This test will fail
    assert len(lines_matched) == 3
