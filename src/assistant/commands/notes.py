"""Note-related command handlers."""

from ..models import Note, NoteBook
from ..utils import input_error


@input_error
def add_note(args, notebook):
    title, *content = args
    content = " ".join(content)
    notebook.add_note(Note(title, content))
    return "Note added."


@input_error
def find_note(args, notebook):
    title = args[0]
    note = notebook.find_note(title)
    if note:
        return str(note)
    return "Note not found."


@input_error
def delete_note(args, notebook):
    title = args[0]
    return notebook.delete_note(title)


@input_error
def edit_note(args, notebook):
    title, *content = args
    content = " ".join(content)
    return notebook.edit_note(title, content)


NOTE_COMMANDS = {
    "add-note": add_note,
    "find-note": find_note,
    "delete-note": delete_note,
    "edit-note": edit_note,
}