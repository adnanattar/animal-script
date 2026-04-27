"""Control, input, and output commands for AnimalScript."""

from animal_script.conditions import Conditions


class Control:
    """Dispatch and evaluate non-arithmetic AnimalScript commands."""

    @staticmethod
    def evaluate_control(tokens, animal_script):
        """Route a tokenized control statement to its command handler."""
        try:
            if tokens[0] == "Monkeys":
                return Control.evaluate_monkeys(tokens, animal_script)
            elif tokens[0] == "Tiger":
                return Control.evaluate_tiger(tokens, animal_script)
            elif tokens[0] == "Dolphin":
                return Control.evaluate_dolphin(tokens, animal_script)
            elif tokens[0] == "Whale":
                return Control.evaluate_whale(tokens, animal_script)
            return "Unknown statement."
        except ValueError:
            return "Invalid operands. Please provide valid numbers."
        except Exception:
            return "Follow the Animal Rules"

    @staticmethod
    def evaluate_monkeys(tokens, animal_script):
        """Evaluate an inclusive ``Monkeys`` loop.

        The language guide describes ``Monkeys i 0 5`` as iterating from 0 to 5
        inclusive, so this intentionally differs from Python's exclusive
        ``range`` stop value.
        """
        if len(tokens) not in [4, 5]:
            return "Invalid loop. Use: Monkeys <variable_name> <start> <end> [<step>]."

        var_name = tokens[1]
        start = int(tokens[2])
        end = int(tokens[3])
        step = int(tokens[4]) if len(tokens) == 5 else 1

        if step == 0:
            return "Invalid loop. Step cannot be zero."

        stop = end + 1 if step > 0 else end - 1
        result = []
        for value in range(start, stop, step):
            animal_script.variables[var_name] = value
            result.append(f"{var_name} set to {value}.")

        return "\n".join(result)

    @staticmethod
    def evaluate_tiger(tokens, animal_script):
        """Evaluate a ``Tiger`` conditional expression."""
        if len(tokens) < 2:
            return "Invalid condition. Use: Tiger <condition>."

        return Conditions.evaluate_expression(tokens[1:], animal_script.variables)

    @staticmethod
    def evaluate_dolphin(tokens, animal_script):
        """Prompt for input and store it in the interpreter variable table."""
        if len(tokens) != 2:
            return "Invalid input. Use: Dolphin <variable_name>."

        var_name = tokens[1]
        user_input = input(f"Enter value for {var_name}: ")
        if user_input.startswith('"') and user_input.endswith('"'):
            animal_script.variables[var_name] = user_input.strip('"')
        else:
            try:
                animal_script.variables[var_name] = int(user_input)
            except ValueError:
                animal_script.variables[var_name] = user_input

        return f"Variable {var_name} set to {user_input}."

    @staticmethod
    def _message_from_tokens(tokens):
        """Return the message portion of a ``Whale`` statement."""
        if len(tokens) == 2:
            return tokens[1]
        return " ".join(tokens[1:])

    @staticmethod
    def evaluate_whale(tokens, animal_script):
        """Print a literal message or a known variable value."""
        if len(tokens) < 2:
            return "Invalid input. Please provide a message or variable name after 'Whale'."

        message = Control._message_from_tokens(tokens)
        if len(tokens) == 2 and message in animal_script.variables:
            value = animal_script.variables[message]
            return f"Whale says: {value}" if isinstance(value, str) else f"Variable {message} is set to {value}"

        return f"Whale says: {message}"
