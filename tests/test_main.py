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

    # Add more test methods for other arithmetic operations...

if __name__ == '__main__':
    unittest.main()
