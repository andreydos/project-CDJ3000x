"""Main entry point for the Personal Assistant CLI."""

from .commands import COMMANDS, NOTE_COMMANDS
from .storage import load_data, save_data
from .utils import parse_input
from .models import NoteBook



def main():
    """Run the assistant command loop."""
    book = load_data()
    notebook = NoteBook()
    print("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            if command in COMMANDS:
                print(COMMANDS[command](args, book))
            elif command:
                print("Invalid command.")


           # if command in NOTE_COMMANDS:
            #    print(NOTE_COMMANDS[command](args, notebook))
            #elif command in COMMANDS:
             #   print(COMMANDS[command](args, book))
            #elif command:
             #   print("Invalid command.")
   
    finally:
        save_data(book)


if __name__ == "__main__":
    main()
