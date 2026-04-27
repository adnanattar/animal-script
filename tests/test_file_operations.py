import unittest
from tempfile import NamedTemporaryFile

from animal_script.file_operations import FileOperations


class TestFileOperations(unittest.TestCase):
    def test_file_operations_functionality(self):
        with NamedTemporaryFile("w+", delete=True) as file:
            self.assertEqual(
                FileOperations.write_to_file(file.name, "Elephants 3 + 4"),
                "Content successfully written to file.",
            )
            self.assertEqual(
                FileOperations.read_commands_from_file(file.name),
                ["Elephants 3 + 4"],
            )

    def test_missing_file_returns_message(self):
        self.assertEqual(
            FileOperations.read_commands_from_file("missing-file.animal"),
            "File not found. Please provide a valid file path.",
        )


if __name__ == '__main__':
    unittest.main()
