import io
import unittest
from contextlib import redirect_stdout

from animal_script.error_handling import ErrorHandling


class TestErrorHandling(unittest.TestCase):
    def test_error_handling_functionality(self):
        output = io.StringIO()
        with redirect_stdout(output):
            ErrorHandling.handle_error("Bad command")

        self.assertEqual(output.getvalue(), "Error: Bad command\n")


if __name__ == '__main__':
    unittest.main()
