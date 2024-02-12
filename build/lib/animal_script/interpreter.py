import sys

class AnimalScript:
    def __init__(self):
        self.variables = {}

    def evaluate(self, input_str):
        try:
            # Split input string into tokens
            tokens = input_str.split()

            # Check for control statements
            if tokens[0] == "Monkeys":
                var_name = tokens[1]
                start = int(tokens[2])
                end = int(tokens[3])
                step = int(tokens[4]) if len(tokens) > 4 else 1
                result = ""
                for i in range(start, end, step):
                    self.variables[var_name] = i
                    result += f"{var_name} set to {i}.\n"
                return result.strip()
            elif tokens[0] == "Tiger":
                condition = ' '.join(tokens[1:])
                return self.evaluate_condition(condition)
            elif tokens[0] == "Dolphin":
                var_name = tokens[1]
                user_input = input(f"Enter value for {var_name}: ")
                if user_input.startswith('"') and user_input.endswith('"'):
                    # If input is enclosed within double quotes, store it as a string
                    self.variables[var_name] = user_input.strip('"')
                    return f"Variable {var_name} set to {user_input}."
                else:
                    # Treat input as an integer
                    self.variables[var_name] = int(user_input)
                    return f"Variable {var_name} set to {user_input}."
            elif tokens[0] == "Whale":
                if len(tokens) < 2:
                    return "Invalid input. Please provide a message or variable name after 'Whale'."
                if tokens[1].startswith('"') and tokens[1].endswith('"'):
                    # If input is enclosed within double quotes, print the data within quotes
                    message = tokens[1].strip('"')
                    return f"Whale says: {message}"
                else:
                    # Treat input as a variable
                    var_name = tokens[1]
                    if var_name in self.variables:
                        value = self.variables[var_name]
                        return f"Whale says: {value}" if isinstance(value, str) else f"Variable {var_name} is set to {value}"
                    else:
                        return f"Variable {var_name} is not defined."

            # Check for arithmetic operations
            operator = tokens[0]
            operand1 = int(tokens[1]) if tokens[1].isdigit() else self.variables.get(tokens[1], 0)
            operator_symbol = tokens[2]
            operand2 = int(tokens[3]) if tokens[3].isdigit() else self.variables.get(tokens[3], 0)

            # Perform arithmetic operation based on the operator
            if operator == "Elephants":
                if operator_symbol != "+":
                    return "Invalid operator. Elephants only trumpet for addition ('+')."
                return f"Trumpets {operand1 + operand2}"
            elif operator == "Frogs":
                if operator_symbol != "-":
                    return "Invalid operator. Frogs only croak for subtraction ('-')."
                return f"Croaks {operand1 - operand2}"
            elif operator == "Bees":
                if operator_symbol != "*":
                    return "Invalid operator. Bees only buzz for multiplication ('*')."
                return f"Buzzes {operand1 * operand2}"
            elif operator == "Lions":
                if operand2 == 0:
                    return "You tried to divide by zero? Well, that's just dividing by my ex. You can't divide by zero, it's undefined!"
                else:
                    return f"Roar {operand1 / operand2}"
            else:
                return "Unknown statement."

        except ValueError:
            return "Invalid operands. Please provide valid numbers."

    def evaluate_condition(self, condition):
        # Evaluate condition and return result
        if condition:
            return "Roar Condition is True."
        else:
            return "Roar Condition is False."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file.animal")
        sys.exit(1)

    input_file = sys.argv[1]

    animal_script = AnimalScript()
    with open(input_file, "r") as file:
        for line in file:
            result = animal_script.evaluate(line.strip())
            print(result)
