"""Utility functions for CLI parsing and error handling."""


def input_error(func):
    """Decorator to catch and display user-friendly error messages."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e) if str(e) else "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
        except Exception as e:
            return f"Something went wrong: {e}"

    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Parse user input into command and arguments."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args
