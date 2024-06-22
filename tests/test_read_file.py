import pytest

from utils.util import read_file

class TestReadFileClass:

    def test_read_existing_file(self):
        file_path = "tests/hello.txt"
        expected_output = "Hello, I am Bob. I like to code in Python."
        assert read_file(file_path) == expected_output