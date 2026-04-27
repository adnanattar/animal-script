import unittest
from unittest.mock import patch

from animal_script.main import AnimalScript


class TestControl(unittest.TestCase):
    def test_evaluate_control(self):
        animal_script = AnimalScript()
        self.assertEqual(
            animal_script.evaluate("Monkeys i 1 3"),
            "i set to 1.\ni set to 2.\ni set to 3.",
        )

    def test_evaluate_condition_control(self):
        animal_script = AnimalScript()
        animal_script.variables["i"] = 3
        self.assertEqual(
            animal_script.evaluate("Tiger i < 10"),
            "Roar Condition is True.",
        )

    def test_evaluate_input_control(self):
        animal_script = AnimalScript()
        with patch("builtins.input", return_value="Ada"):
            self.assertEqual(
                animal_script.evaluate("Dolphin name"),
                "Variable name set to Ada.",
            )
        self.assertEqual(animal_script.variables["name"], "Ada")

    def test_evaluate_print_control(self):
        animal_script = AnimalScript()
        self.assertEqual(
            animal_script.evaluate('Whale "Hello"'),
            "Whale says: Hello",
        )


if __name__ == '__main__':
    unittest.main()
