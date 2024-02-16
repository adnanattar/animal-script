import unittest
from animal_script.main import AnimalScript

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
        self.assertEqual(result, "Gallops 3.3333333333333335")

    def test_bitwise_xor(self):
        result = self.animal_script.evaluate("Pandas 5 ^ 3")
        self.assertEqual(result, "Rolls 6")

    def test_bitwise_or(self):
        result = self.animal_script.evaluate("Lemurs 5 | 3")
        self.assertEqual(result, "Leaps 7")

    def test_bitwise_and(self):
        result = self.animal_script.evaluate("Owls 5 & 3")
        self.assertEqual(result, "Hoots 1")

if __name__ == '__main__':
    unittest.main()