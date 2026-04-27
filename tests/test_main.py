import io
import unittest
from contextlib import redirect_stdout
from tempfile import NamedTemporaryFile
from unittest.mock import patch

from animal_script.main import AnimalScript
from animal_script.main import main


class TestAnimalScript(unittest.TestCase):
    def setUp(self):
        self.animal_script = AnimalScript()

    def test_addition(self):
        result = self.animal_script.evaluate("Elephants 3 + 4")
        self.assertEqual(result, "Trumpets 7")

    def test_subtraction(self):
        result = self.animal_script.evaluate("Frogs 5 - 2")
        self.assertEqual(result, "Croaks 3")

    def test_multiplication(self):
        result = self.animal_script.evaluate("Bees 3 * 4")
        self.assertEqual(result, "Buzzes 12")

    def test_division(self):
        result = self.animal_script.evaluate("Lions 10 / 2")
        self.assertEqual(result, "Roar 5.0")

    def test_exponentiation(self):
        result = self.animal_script.evaluate("Giraffes 2 ** 3")
        self.assertEqual(result, "Stretches 8")

    def test_modulus(self):
        result = self.animal_script.evaluate("Kangaroos 10 % 3")
        self.assertEqual(result, "Hops 1")

    def test_floor_division(self):
        result = self.animal_script.evaluate("Rhinos 10 // 3")
        self.assertEqual(result, "Charges 3")

    def test_true_division(self):
        result = self.animal_script.evaluate("Zebras 10 / 3")
        self.assertEqual(result, "Gallops 3.3333")

    def test_bitwise_xor(self):
        result = self.animal_script.evaluate("Pandas 5 ^ 3")
        self.assertEqual(result, "Rolls 6")

    def test_bitwise_or(self):
        result = self.animal_script.evaluate("Lemurs 5 | 3")
        self.assertEqual(result, "Leaps 7")

    def test_bitwise_and(self):
        result = self.animal_script.evaluate("Owls 5 & 3")
        self.assertEqual(result, "Hoots 1")

    def test_for_loop_is_inclusive(self):
        result = self.animal_script.evaluate("Monkeys i 0 5")
        self.assertEqual(
            result,
            "i set to 0.\n"
            "i set to 1.\n"
            "i set to 2.\n"
            "i set to 3.\n"
            "i set to 4.\n"
            "i set to 5.",
        )
        self.assertEqual(self.animal_script.variables["i"], 5)

    def test_for_loop_with_step(self):
        result = self.animal_script.evaluate("Monkeys i 0 5 2")
        self.assertEqual(result, "i set to 0.\ni set to 2.\ni set to 4.")
        self.assertEqual(self.animal_script.variables["i"], 4)

    def test_condition_true(self):
        self.animal_script.evaluate("Monkeys i 0 5")
        result = self.animal_script.evaluate("Tiger i < 10")
        self.assertEqual(result, "Roar Condition is True.")

    def test_condition_false(self):
        self.animal_script.evaluate("Monkeys i 0 5")
        result = self.animal_script.evaluate("Tiger i > 10")
        self.assertEqual(result, "Roar Condition is False.")

    def test_print_statement(self):
        result = self.animal_script.evaluate('Whale "Hello"')
        self.assertEqual(result, "Whale says: Hello")

    def test_print_statement_with_spaces(self):
        result = self.animal_script.evaluate('Whale "Hello Animal Script"')
        self.assertEqual(result, "Whale says: Hello Animal Script")

    def test_input_statement(self):
        with patch("builtins.input", return_value="10"):
            result = self.animal_script.evaluate("Dolphin age")

        self.assertEqual(result, "Variable age set to 10.")
        self.assertEqual(self.animal_script.variables["age"], 10)

    def test_input_value_can_be_used_in_arithmetic(self):
        with patch("builtins.input", return_value="10"):
            self.animal_script.evaluate("Dolphin age")

        result = self.animal_script.evaluate("Elephants age + 5")
        self.assertEqual(result, "Trumpets 15")

    def test_cli_entrypoint_target_is_importable(self):
        self.assertTrue(callable(main))

    def test_main_runs_animal_file(self):
        with NamedTemporaryFile("w+", suffix=".animal", delete=True) as file:
            file.write("Elephants 3 + 4\n")
            file.write('Whale "Hello"\n')
            file.flush()

            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = main([file.name])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue(), "Trumpets 7\nWhale says: Hello\n")


if __name__ == '__main__':
    unittest.main()
