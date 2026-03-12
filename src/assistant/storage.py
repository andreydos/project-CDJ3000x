"""Storage for address book data in user directory."""

import pickle
from pathlib import Path

from .models import AddressBook, NoteBook


def get_data_dir() -> Path:
    """Return user data directory, creating it if needed."""
    base = Path.home() / ".local" / "share" / "cli-assistant"
    base.mkdir(parents=True, exist_ok=True)
    return base


def get_data_path() -> Path:
    """Return path to addressbook pickle file."""
    return get_data_dir() / "addressbook.pkl"


def get_notebook_path() -> Path:
    """Return path to notebook pickle file."""
    return get_data_dir() / "notebook.pkl"


def save_data(book: AddressBook) -> None:
    """Save address book to user directory."""
    with open(get_data_path(), "wb") as f:
        pickle.dump(book, f)


def load_data() -> AddressBook:
    """Load address book from user directory."""
    try:
        with open(get_data_path(), "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def save_notebook_data(notebook: NoteBook) -> None:
    """Save notebook to user directory."""
    with open(get_notebook_path(), "wb") as f:
        pickle.dump(notebook, f)


def load_notebook_data() -> NoteBook:
    """Load notebook from user directory."""
    try:
        with open(get_notebook_path(), "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NoteBook()
    