import pytest
from animal_script.interpreter import AnimalScript

@pytest.fixture
def animal_script_instance():
    return AnimalScript()

def test_evaluate():
    animal_script = AnimalScript()
    assert animal_script.evaluate("Elephants 2 + 3") == "Trumpets 5"

def test_another_evaluation(animal_script_instance):
    assert animal_script_instance.evaluate("Frogs 5 - 2") == "Croaks 3"

# Add more test functions as needed
