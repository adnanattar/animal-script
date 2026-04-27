# Contributing to AnimalScript

Contributions are welcome. This project is intentionally small, so changes
should keep the language easy to understand for beginners.

## Local Setup

```bash
git clone https://github.com/adnanattar/animal-script.git
cd animal-script
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

## Running the Interpreter

Interactive mode:

```bash
python -m animal_script.main
```

File mode:

```bash
python -m animal_script.main examples/guide_demo.animal
```

## Test Before Submitting

Run both test commands before opening a pull request:

```bash
python -m unittest discover -v
python -m pytest -q
```

Also check package metadata:

```bash
python setup.py check --metadata --strict
```

## Code Guidelines

- Keep language behavior aligned with the public GitBook guide.
- Add or update tests for every language behavior change.
- Prefer clear names and small functions over clever abstractions.
- Use comments and docstrings to explain intent, not obvious syntax.
- Keep runtime dependencies minimal.

## Pull Request Checklist

- Tests pass locally.
- README or guide-facing documentation is updated when behavior changes.
- New commands have examples and regression tests.
- Error messages remain beginner-friendly.

## Code of Conduct

By participating in this project, you agree to follow the
[Code of Conduct](CODE_OF_CONDUCT.md).
