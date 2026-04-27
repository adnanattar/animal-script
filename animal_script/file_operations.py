"""Small file helpers used by tests and future file-based tooling."""


class FileOperations:
    """Read and append plain-text AnimalScript commands."""

    @staticmethod
    def read_commands_from_file(file_path):
        """Return stripped commands from a file or a friendly error message."""
        try:
            with open(file_path, "r") as file:
                commands = file.readlines()
            return [command.strip() for command in commands]
        except FileNotFoundError:
            return "File not found. Please provide a valid file path."
        except Exception as e:
            return f"Error occurred: {e}"

    @staticmethod
    def write_to_file(file_path, content):
        """Append one command line to a file."""
        try:
            with open(file_path, "a") as file:
                file.write(content + "\n")
            return "Content successfully written to file."
        except Exception as e:
            return f"Error occurred: {e}"
