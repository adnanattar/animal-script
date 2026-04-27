"""Shared error-reporting helper for AnimalScript tooling."""


class ErrorHandling:
    """Print human-readable error messages."""

    @staticmethod
    def handle_error(error_message):
        """Print a standard error message without interrupting the caller."""
        try:
            print(f"Error: {error_message}")
        except Exception as e:
            print("An unexpected error occurred during error handling:", e)
