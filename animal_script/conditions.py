"""Conditional expression support for AnimalScript's ``Tiger`` command."""


class Conditions:
    """Evaluate simple boolean and comparison expressions."""

    COMPARISON_OPERATORS = {
        "<": lambda left, right: left < right,
        "<=": lambda left, right: left <= right,
        ">": lambda left, right: left > right,
        ">=": lambda left, right: left >= right,
        "==": lambda left, right: left == right,
        "!=": lambda left, right: left != right,
    }

    @staticmethod
    def _resolve_value(token, variables=None):
        """Resolve a token as a variable, boolean literal, integer, or string."""
        variables = variables or {}

        if token in variables:
            return variables[token]
        if token == "True":
            return True
        if token == "False":
            return False

        try:
            return int(token)
        except ValueError:
            return token

    @staticmethod
    def evaluate_condition(condition):
        """Convert a boolean-like condition into AnimalScript output."""
        try:
            if condition:
                return "Roar Condition is True."
            else:
                return "Roar Condition is False."
        except Exception:
            return "Follow the Animal Rules"

    @staticmethod
    def evaluate_expression(tokens, variables=None):
        """Evaluate tokens after ``Tiger``.

        Supported forms are a single boolean-like value, such as ``Tiger True``,
        or a three-token comparison, such as ``Tiger i < 10``.
        """
        if len(tokens) == 1:
            value = Conditions._resolve_value(tokens[0], variables)
            return Conditions.evaluate_condition(bool(value))

        if len(tokens) != 3:
            return "Invalid condition. Use: Tiger <left> <operator> <right>."

        left_token, operator, right_token = tokens
        if operator not in Conditions.COMPARISON_OPERATORS:
            return "Invalid condition operator."

        variables = variables or {}
        # Identifier-looking tokens must exist unless they are known literals.
        if left_token not in variables and left_token.isidentifier() and left_token not in ["True", "False"]:
            return f"Variable {left_token} is not defined."
        if right_token not in variables and right_token.isidentifier() and right_token not in ["True", "False"]:
            return f"Variable {right_token} is not defined."

        try:
            left = Conditions._resolve_value(left_token, variables)
            right = Conditions._resolve_value(right_token, variables)
            result = Conditions.COMPARISON_OPERATORS[operator](left, right)
            return Conditions.evaluate_condition(result)
        except Exception:
            return "Follow the Animal Rules"
