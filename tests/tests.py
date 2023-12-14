import unittest
from src.ans import extract_errors

class TestExtractErrors(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_log.txt"
        with open(self.log_file, 'w') as f:
            f.write(
                "INFO: This is an info message.\nERROR: This is an error!\nWARNING: This is a warning.\n")

    def test_extract_errors(self):
        errors = extract_errors(self.log_file)
        self.assertEqual(errors, ["ERROR: This is an error!"])

    def test_no_errors(self):
        with open(self.log_file, 'w') as f:
            f.write("INFO: No errors here.\n")
        errors = extract_errors(self.log_file)
        self.assertEqual(errors, [])

    def tearDown(self):
        import os
        os.remove(self.log_file)


if __name__ == '__main__':
    unittest.main()
