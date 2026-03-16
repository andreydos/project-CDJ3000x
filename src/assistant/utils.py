"""Utility functions for CLI parsing and error handling."""

import shlex


class CommandError(Exception):
    """Base class for command-related errors."""


class InvalidArgumentsError(CommandError):
    """Raised when a command receives invalid or missing arguments."""


class ContactNotFoundError(CommandError):
    """Raised when a contact is not found."""


class NoteNotFoundError(CommandError):
    """Raised when a note is not found."""


def input_error(func):
    """Decorator to catch and display user-friendly error messages."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidArgumentsError as e:
            return str(e)
        except ContactNotFoundError:
            return "Contact not found."
        except NoteNotFoundError as e:
            # If a custom message is provided, use it; otherwise a generic one
            return str(e) if str(e) else "Note not found."
        except ValueError as e:
            # Used for field validation (phone, email, birthday, etc.)
            return str(e) if str(e) else "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."

    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Parse user input into command and arguments."""
    try:
        parts = shlex.split(user_input.strip())
    except ValueError:
        # Unbalanced quotes or similar parsing issue
        raise InvalidArgumentsError("Invalid input syntax.")
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args
