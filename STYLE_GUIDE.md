# AnimalScript Style Guide

This guide describes conventions for writing readable `.animal` files that work
with the current AnimalScript interpreter.

## File Format

- Use the `.animal` extension for AnimalScript programs.
- Write one statement per line.
- Keep examples short and beginner-friendly.
- Use blank lines only when they make a longer file easier to scan.

## Variables

- Use descriptive names for values you read with `Dolphin` or create with
  `Monkeys`.
- Prefer lower camel case for multi-word names.

```animal
Dolphin totalApples
Elephants totalApples + 5
```

## Arithmetic

- Put spaces around operators.
- Use the animal command that matches the operation.

```animal
Elephants 3 + 4
Frogs 10 - 2
Bees 6 * 7
Zebras 10 / 3
```

## Control Statements

Use `Monkeys` for inclusive loops:

```animal
Monkeys i 0 5
```

Use the optional step only when it helps readability:

```animal
Monkeys i 0 10 2
```

## Conditions

Use `Tiger` with a boolean literal or a simple comparison:

```animal
Tiger True
Tiger i < 10
Tiger totalApples >= 5
```

Supported comparison operators are `<`, `<=`, `>`, `>=`, `==`, and `!=`.

## Input and Output

Use `Dolphin` for input:

```animal
Dolphin age
```

Use `Whale` for output. Quote text that contains spaces:

```animal
Whale "Hello AnimalScript"
Whale age
```

## Comments

The interpreter uses shell-style parsing, so `#` starts a comment when it is not
inside quotes.

```animal
Elephants 3 + 4 # Adds two numbers
Whale "Hello # not a comment"
```

## Error Handling

Prefer small programs and simple statements. If a command fails, check:

- The animal keyword is spelled exactly as documented.
- The operator matches the command.
- Variables are assigned before they are used.
- AnimalScript commands are run inside the interpreter or from a `.animal` file,
  not directly in the terminal shell.
