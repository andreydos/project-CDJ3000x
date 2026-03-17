"""Main entry point for the Personal Assistant CLI."""

from .commands import COMMANDS, NOTE_COMMANDS
from .models import NoteBook
from .storage import load_data, save_data, load_notebook_data, save_notebook_data
from .utils import parse_input
import traceback


RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def colorize_message(message: str) -> str:
    """Return message wrapped in color codes for specific actions."""
    if message in ("Contact deleted.", "Note deleted."):
        return f"{RED}{message}{RESET}"
    if message in ("Contact added.", "Note added."):
        return f"{GREEN}{message}{RESET}"
    return message


def print_response(message: str) -> None:
    """Print a command response wrapped with separators."""
    print(" | " + "-" * 10)
    for line in str(colorize_message(message)).splitlines():
        print(" | " + line)
    print(" | " + "-" * 10)


def main():
    """Run the assistant command loop."""
    book = load_data()
    notebook = load_notebook_data()
    print("Welcome to the assistant bot!")

    try:
        while True:
            try:
                user_input = input("Enter a command: ")
                command, args = parse_input(user_input)

                if command in ["close", "exit"]:
                    print("Good bye!")
                    break

                if command in NOTE_COMMANDS:
                    result = NOTE_COMMANDS[command](args, notebook)
                    print_response(result)
                elif command in COMMANDS:
                    result = COMMANDS[command](args, book)
                    print_response(result)
                elif command:
                    print_response("Invalid command.")
            except Exception as e:
                print("Unexpected error, please contact the developer.")
                traceback.print_exception(type(e), e, e.__traceback__)
    finally:
        save_data(book)
        save_notebook_data(notebook)
        print("Data saved.")
        


if __name__ == "__main__":
    main()



    