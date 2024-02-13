from conditions import Conditions
from arithmetic import Arithmetic
from error_handling import ErrorHandling
from data_structures import DataStructures

class Control:
    @staticmethod
    def evaluate_control(tokens, animal_script):
        try:
            if tokens[0] == "Monkeys":
                return Arithmetic.evaluate_giraffe(tokens, animal_script)
            elif tokens[0] == "Tiger":
                return Conditions.evaluate_fox(tokens, animal_script)
            elif tokens[0] == "Dolphin":
                return Control.evaluate_dolphin(tokens, animal_script)
            elif tokens[0] == "Whale":
                return Control.evaluate_whale(tokens, animal_script)
        except Exception as e:
            print("Follow the Animal Rules")
            return None  # Or return any appropriate value indicating failure

    @staticmethod
    def evaluate_dolphin(tokens, animal_script):
        var_name = tokens[1]
        user_input = input(f"Enter value for {var_name}: ")
        if user_input.startswith('"') and user_input.endswith('"'):
            animal_script.variables[var_name] = user_input.strip('"')
            return f"Variable {var_name} set to {user_input}."
        else:
            animal_script.variables[var_name] = int(user_input)
            return f"Variable {var_name} set to {user_input}."

    @staticmethod
    def evaluate_whale(tokens, animal_script):
        if len(tokens) < 2:
            return "Invalid input. Please provide a message or variable name after 'Whale'."
        if tokens[1].startswith('"') and tokens[1].endswith('"'):
            message = tokens[1].strip('"')
            return f"Whale says: {message}"
        else:
            var_name = tokens[1]
            if var_name in animal_script.variables:
                value = animal_script.variables[var_name]
                return f"Whale says: {value}" if isinstance(value, str) else f"Variable {var_name} is set to {value}"
            else:
                return f"Variable {var_name} is not defined."
