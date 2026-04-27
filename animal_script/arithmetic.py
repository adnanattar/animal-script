"""Arithmetic command handlers for AnimalScript.

Each animal keyword maps to one Python arithmetic or bitwise operation. Public
methods return language output strings instead of raising exceptions so the CLI
can keep running after invalid input.
"""


class Arithmetic:
    """Perform documented AnimalScript arithmetic operations."""

    ZERO_DIVISION_MESSAGE = (
        "You tried to divide by zero? Well, that's just arranging fight "
        "between Elephant and Ant. You can't divide by zero, it's undefined!"
    )

    @staticmethod
    def _resolve_operand(operand, variables=None):
        """Convert a literal or known variable name into an integer operand."""
        if isinstance(operand, int):
            return operand

        variables = variables or {}
        if operand in variables:
            operand = variables[operand]

        return int(operand)

    @staticmethod
    def _format_division(value):
        """Match the language guide's compact division output."""
        return str(round(value, 4))

    @staticmethod
    def perform_operation(operator, operand1, operator_symbol, operand2, variables=None):
        """Run one arithmetic command.

        Args:
            operator: Animal keyword such as ``Elephants`` or ``Zebras``.
            operand1: Left operand, either an integer literal or variable name.
            operator_symbol: Symbol expected by that animal command.
            operand2: Right operand, either an integer literal or variable name.
            variables: Current interpreter variable table.
        """
        try:
            operand1 = Arithmetic._resolve_operand(operand1, variables)
            operand2 = Arithmetic._resolve_operand(operand2, variables)

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
                if operator_symbol == "/":
                    if operand2 == 0:
                        return Arithmetic.ZERO_DIVISION_MESSAGE
                    return f"Roar {Arithmetic._format_division(operand1 / operand2)}"
                else:
                    return "Invalid operator. Lions only roar for division ('/')."
            elif operator == "Giraffes":
                if operator_symbol != "**":
                    return "Invalid operator. Giraffes only perform exponentiation ('**')."
                return f"Stretches {operand1 ** operand2}"
            elif operator == "Kangaroos":
                if operator_symbol != "%":
                    return "Invalid operator. Kangaroos only hop for modulus ('%')."
                if operand2 == 0:
                    return Arithmetic.ZERO_DIVISION_MESSAGE
                return f"Hops {operand1 % operand2}"
            elif operator == "Rhinos":
                if operator_symbol != "//":
                    return "Invalid operator. Rhinos only charge for floor division ('//')."
                if operand2 == 0:
                    return Arithmetic.ZERO_DIVISION_MESSAGE
                return f"Charges {operand1 // operand2}"
            elif operator == "Zebras":
                if operator_symbol != "/":
                    return "Invalid operator. Zebras only gallop for true division ('/')."
                if operand2 == 0:
                    return Arithmetic.ZERO_DIVISION_MESSAGE
                return f"Gallops {Arithmetic._format_division(operand1 / operand2)}"
            elif operator == "Pandas":
                if operator_symbol != "^":
                    return "Invalid operator. Pandas only roll for bitwise XOR ('^')."
                return f"Rolls {operand1 ^ operand2}"
            elif operator == "Lemurs":
                if operator_symbol != "|":
                    return "Invalid operator. Lemurs only leap for bitwise OR ('|')."
                return f"Leaps {operand1 | operand2}"
            elif operator == "Owls":
                if operator_symbol != "&":
                    return "Invalid operator. Owls only hoot for bitwise AND ('&')."
                return f"Hoots {operand1 & operand2}"
            else:
                return "Unknown statement."
        except (TypeError, ValueError):
            return "Invalid operands. Please provide valid numbers."
        except Exception:
            return "Follow the Animal Rules"
