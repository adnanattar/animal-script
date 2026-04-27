# AnimalScript

AnimalScript is a small educational programming language with animal-themed
commands. It is designed for beginners who want to practice basic programming
ideas such as arithmetic, variables, loops, conditions, input, and output.

[![Downloads](https://static.pepy.tech/badge/animal-script)](https://pepy.tech/project/animal-script)

## Installation

AnimalScript supports Python 3.9 and newer.

Install the published package from PyPI:

```bash
pip install animal-script
```

For local development, clone the repository and install it in editable mode:

```bash
git clone https://github.com/adnanattar/animal-script.git
cd animal-script
python -m pip install -e .
```

## Quick Start

Run the interactive interpreter:

```bash
python -m animal_script.main
```

Example session:

```text
Enter AnimalScript commands manually. Type 'exit' to quit.
>>> Elephants 3 + 4
Trumpets 7
>>> Whale "Hello"
Whale says: Hello
>>> exit
```

You can also run a `.animal` file:

```bash
python -m animal_script.main examples/guide_demo.animal
```

After installing the package, the console command is available too:

```bash
animal-script examples/guide_demo.animal
```

AnimalScript statements must be typed inside the interpreter or saved inside a
`.animal` file. If you type `Elephants 3 + 4` directly in your terminal shell,
the shell will try to run `Elephants` as an operating-system command.

## Example Program

```animal
Elephants 3 + 4
Monkeys i 0 5
Tiger i < 10
Whale "Hello"
```

Output:

```text
Trumpets 7
i set to 0.
i set to 1.
i set to 2.
i set to 3.
i set to 4.
i set to 5.
Roar Condition is True.
Whale says: Hello
```

## Language Reference

### Arithmetic

| Command | Operation | Syntax | Example | Output |
| --- | --- | --- | --- | --- |
| `Elephants` | Addition | `Elephants n + m` | `Elephants 3 + 4` | `Trumpets 7` |
| `Frogs` | Subtraction | `Frogs n - m` | `Frogs 5 - 2` | `Croaks 3` |
| `Bees` | Multiplication | `Bees n * m` | `Bees 3 * 4` | `Buzzes 12` |
| `Lions` | Division | `Lions n / m` | `Lions 10 / 2` | `Roar 5.0` |
| `Giraffes` | Exponentiation | `Giraffes n ** m` | `Giraffes 2 ** 3` | `Stretches 8` |
| `Kangaroos` | Modulus | `Kangaroos n % m` | `Kangaroos 10 % 3` | `Hops 1` |
| `Rhinos` | Floor division | `Rhinos n // m` | `Rhinos 10 // 3` | `Charges 3` |
| `Zebras` | True division | `Zebras n / m` | `Zebras 10 / 3` | `Gallops 3.3333` |
| `Pandas` | Bitwise XOR | `Pandas n ^ m` | `Pandas 5 ^ 3` | `Rolls 6` |
| `Lemurs` | Bitwise OR | `Lemurs n \| m` | `Lemurs 5 \| 3` | `Leaps 7` |
| `Owls` | Bitwise AND | `Owls n & m` | `Owls 5 & 3` | `Hoots 1` |

Operands can be integer literals or variables already stored in the current
interpreter session.

### Control Statement

`Monkeys` creates an inclusive loop:

```animal
Monkeys i 0 5
```

This sets `i` to `0`, `1`, `2`, `3`, `4`, and `5`. A custom step is optional:

```animal
Monkeys i 0 5 2
```

### Conditional Statement

`Tiger` evaluates a boolean value or a simple comparison:

```animal
Tiger i < 10
Tiger True
```

Supported comparison operators are `<`, `<=`, `>`, `>=`, `==`, and `!=`.

### Print Statement

`Whale` prints a string literal or a known variable:

```animal
Whale "Hello AnimalScript"
Whale i
```

### Input Statement

`Dolphin` asks the user for a value and stores it in a variable:

```animal
Dolphin age
Elephants age + 5
```

Numeric input is stored as an integer. Other input is stored as text.

## Development

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the test suite:

```bash
python -m unittest discover -v
python -m pytest -q
```

Check package metadata:

```bash
python setup.py check --metadata --strict
```

## Project Layout

```text
animal_script/
  main.py            # CLI and top-level evaluator
  arithmetic.py      # Arithmetic and bitwise commands
  control.py         # Monkeys, Tiger, Dolphin, and Whale commands
  conditions.py      # Tiger condition evaluation helpers
  file_operations.py # File helper utilities
  data_structures.py # Educational data-structure examples
tests/               # Unit and regression tests
examples/            # Runnable .animal examples
```

## Documentation

The public language guide is available at:

<https://adnanattar.gitbook.io/animal-script-language-guide>

## Contributing

Contributions are welcome. Before opening a pull request, run the test commands
above and update documentation if your change affects language behavior.

See [contributing.md](contributing.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

AnimalScript is released under the [MIT License](LICENSE).

## Author

Created by [Adnan B. Attar](https://github.com/adnanattar).
