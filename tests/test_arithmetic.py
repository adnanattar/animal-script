import unittest

from animal_script.arithmetic import Arithmetic


class TestArithmetic(unittest.TestCase):
    def test_perform_operation(self):
        self.assertEqual(
            Arithmetic.perform_operation("Elephants", "3", "+", "4"),
            "Trumpets 7",
        )

    def test_variables_can_be_resolved(self):
        self.assertEqual(
            Arithmetic.perform_operation(
                "Frogs",
                "age",
                "-",
                "2",
                variables={"age": 10},
            ),
            "Croaks 8",
        )

    def test_zero_division_returns_language_error(self):
        self.assertIn(
            "You can't divide by zero",
            Arithmetic.perform_operation("Zebras", "10", "/", "0"),
        )


if __name__ == '__main__':
    unittest.main()
