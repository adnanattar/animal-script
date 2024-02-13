import sys
from arithmetic import Arithmetic
from conditions import Conditions
from control import Control

class AnimalScript:
    def __init__(self):
        self.variables = {}

    def evaluate(self, input_str):
        try:
            tokens = input_str.split()
            if tokens[0] in ["Monkeys", "Tiger", "Dolphin", "Whale"]:
                return Control.evaluate_control(tokens, self)
            elif tokens[0] in ["Elephants", "Frogs", "Bees", "Lions", "Giraffes", "Kangaroos", "Rhinos", "Zebras", "Pandas", "Lemurs", "Owls"]:
                return Arithmetic.perform_operation(*tokens)
            else:
                return "Unknown statement."
        except ValueError:
            return "Invalid operands. Please provide valid numbers."
        except Exception as e:
            return "Follow the Animal Rules"

if __name__ == "__main__":
    animal_script = AnimalScript()

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        try:
            with open(input_file, "r") as file:
                for line in file:
                    result = animal_script.evaluate(line.strip())
                    print(result)
        except Exception as e:
            print("Follow the Animal Rules")
    else:
        print("Enter AnimalScript commands manually. Type 'exit' to quit.")
        while True:
            command = input(">>> ")
            if command.lower() == "exit":
                break
            try:
                result = animal_script.evaluate(command.strip())
                print(result)
            except Exception as e:
                print("Follow the Animal Rules")
