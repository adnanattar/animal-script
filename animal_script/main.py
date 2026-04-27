"""Command-line entry point and top-level evaluator for AnimalScript.

The interpreter currently supports one statement per line. Each statement is
split with ``shlex`` so quoted strings such as ``Whale "Hello world"`` stay
together while comments and blank lines are ignored.
"""

import sys
import shlex

from animal_script.arithmetic import Arithmetic
from animal_script.control import Control


class AnimalScript:
    """Stateful AnimalScript interpreter.

    Variables live on the interpreter instance so commands from the same file
    or REPL session can share values. For example, ``Dolphin age`` stores a
    value that can later be used by ``Elephants age + 5``.
    """

    CONTROL_STATEMENTS = {"Monkeys", "Tiger", "Dolphin", "Whale"}
    ARITHMETIC_STATEMENTS = {
        "Elephants",
        "Frogs",
        "Bees",
        "Lions",
        "Giraffes",
        "Kangaroos",
        "Rhinos",
        "Zebras",
        "Pandas",
        "Lemurs",
        "Owls",
    }

    def __init__(self):
        self.variables = {}

    def evaluate(self, input_str):
        """Evaluate one AnimalScript statement and return printable output.

        Returning ``None`` means the input was empty or a comment-only line and
        should not print anything.
        """
        try:
            if not input_str or not input_str.strip():
                return None

            tokens = shlex.split(input_str, comments=True)
            if not tokens:
                return None

            if tokens[0] in self.CONTROL_STATEMENTS:
                return Control.evaluate_control(tokens, self)
            elif tokens[0] in self.ARITHMETIC_STATEMENTS:
                if len(tokens) != 4:
                    return "Invalid operation. Use: <Animal> <operand> <operator> <operand>."
                return Arithmetic.perform_operation(*tokens, variables=self.variables)

            return "Unknown statement."
        except ValueError:
            return "Invalid operands. Please provide valid numbers."
        except Exception:
            return "Follow the Animal Rules"


def run_file(file_path, animal_script):
    """Execute every statement in an AnimalScript file."""
    with open(file_path, "r") as file:
        for line in file:
            result = animal_script.evaluate(line.strip())
            if result is not None:
                print(result)


def run_repl(animal_script):
    """Run the interactive prompt used by ``python -m animal_script.main``."""
    print("Enter AnimalScript commands manually. Type 'exit' to quit.")
    while True:
        command = input(">>> ")
        if command.lower() == "exit":
            break

        result = animal_script.evaluate(command.strip())
        if result is not None:
            print(result)


def main(argv=None):
    """Console-script entry point for ``animal-script``."""
    argv = sys.argv[1:] if argv is None else argv
    animal_script = AnimalScript()

    if len(argv) == 1:
        try:
            run_file(argv[0], animal_script)
        except Exception:
            print("Follow the Animal Rules")
            return 1
        return 0

    run_repl(animal_script)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
