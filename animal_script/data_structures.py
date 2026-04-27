"""Educational examples for Python data structures with animal-themed data."""


class DataStructures:
    """Return simple list, dictionary, and set examples.

    These helpers are not part of the command interpreter yet; they exist as
    examples that can be tested and reused by future language features.
    """

    @staticmethod
    def list_example():
        """Build and mutate a list of animal names."""
        try:
            animal_list = ["Elephant", "Lion", "Giraffe", "Zebra", "Tiger"]

            # Keep a couple of access examples visible for learners.
            first_animal = animal_list[0]
            last_animal = animal_list[-1]
            _ = (first_animal, last_animal)

            animal_list[2] = "Monkey"
            animal_list.append("Bear")
            animal_list.remove("Lion")

            return animal_list
        except Exception as e:
            return "An error occurred: " + str(e)

    @staticmethod
    def dictionary_example():
        """Build and mutate a dictionary of animal characteristics."""
        try:
            animal_dict = {
                "Elephant": "Big",
                "Lion": "Fierce",
                "Giraffe": "Tall",
                "Zebra": "Striped",
                "Tiger": "Predator",
            }

            elephant_characteristic = animal_dict['Elephant']
            tiger_characteristic = animal_dict.get('Tiger')
            _ = (elephant_characteristic, tiger_characteristic)

            animal_dict['Giraffe'] = 'Long Neck'
            animal_dict['Hippo'] = 'Heavy'
            del animal_dict['Zebra']

            return animal_dict
        except Exception as e:
            return "An error occurred: " + str(e)

    @staticmethod
    def set_example():
        """Build and mutate a set of animal sounds."""
        try:
            animal_sounds = {"Roar", "Trumpet", "Growl", "Snarl"}

            animal_sounds.add("Howl")
            animal_sounds.remove("Snarl")

            return animal_sounds
        except Exception as e:
            return "An error occurred: " + str(e)
