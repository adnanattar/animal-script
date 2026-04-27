import unittest

from animal_script.data_structures import DataStructures


class TestDataStructures(unittest.TestCase):
    def test_data_structure_functions(self):
        self.assertEqual(
            DataStructures.list_example(),
            ["Elephant", "Monkey", "Zebra", "Tiger", "Bear"],
        )
        self.assertEqual(
            DataStructures.dictionary_example(),
            {
                "Elephant": "Big",
                "Lion": "Fierce",
                "Giraffe": "Long Neck",
                "Tiger": "Predator",
                "Hippo": "Heavy",
            },
        )
        self.assertEqual(
            DataStructures.set_example(),
            {"Roar", "Trumpet", "Growl", "Howl"},
        )


if __name__ == '__main__':
    unittest.main()
