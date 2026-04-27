import unittest

from animal_script.conditions import Conditions


class TestConditions(unittest.TestCase):
    def test_evaluate_condition(self):
        self.assertEqual(
            Conditions.evaluate_condition(True),
            "Roar Condition is True.",
        )
        self.assertEqual(
            Conditions.evaluate_condition(False),
            "Roar Condition is False.",
        )

    def test_evaluate_expression_with_variable(self):
        self.assertEqual(
            Conditions.evaluate_expression(["i", "<", "10"], {"i": 5}),
            "Roar Condition is True.",
        )

    def test_evaluate_expression_with_boolean_literal(self):
        self.assertEqual(
            Conditions.evaluate_expression(["False"]),
            "Roar Condition is False.",
        )


if __name__ == '__main__':
    unittest.main()
