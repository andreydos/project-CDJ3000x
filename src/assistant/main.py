"""Main entry point for the Personal Assistant CLI."""

from .commands import COMMANDS, NOTE_COMMANDS
from .models import NoteBook
from .storage import load_data, save_data, load_notebook_data, save_notebook_data
from .utils import parse_input


def main():
    """Run the assistant command loop."""
    book = load_data()
    notebook = load_notebook_data()
    print("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            if command in NOTE_COMMANDS:
                print(NOTE_COMMANDS[command](args, notebook))
            elif command in COMMANDS:
                print(COMMANDS[command](args, book))
            elif command:
                print("Invalid command.")
    finally:
        save_data(book)
        save_notebook_data(notebook)


if __name__ == "__main__":
    main()
    