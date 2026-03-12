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
    query = " ".join(args)
    results = [
        str(note) for note in notebook.data.values()
        if query.lower() in note.title.lower() or query.lower() in note.content.lower()
    ]
    if results:
        return "\n".join(results)
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


@input_error
def all_notes(args, notebook):
    if not notebook.data:
        return "No notes saved."
    return "\n".join(str(note) for note in notebook.data.values())


NOTE_COMMANDS = {
    "add-note": add_note,
    "find-note": find_note,
    "delete-note": delete_note,
    "edit-note": edit_note,
    "all-notes": all_notes,
}
