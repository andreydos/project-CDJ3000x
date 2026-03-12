"""Note-related command handlers."""

from ..models import Note, NoteBook
from ..utils import input_error


@input_error
def add_note(args, notebook):
    if len(args) < 2:
        raise ValueError("Give me title and content please.")
    title, *content = args
    content = " ".join(content)
    notebook.add_note(Note(title, content))
    return "Note added."


@input_error
def find_note(args, notebook):
    if len(args) < 1:
        raise ValueError("Give me search query please.")
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
    if len(args) < 1:
        raise ValueError("Give me title please.")
    title = args[0]
    return notebook.delete_note(title)


@input_error
def edit_note(args, notebook):
    if len(args) < 2:
        raise ValueError("Give me title and new content please.")
    title, *content = args
    content = " ".join(content)
    return notebook.edit_note(title, content)


@input_error
def all_notes(args, notebook):
    if not notebook.data:
        return "No notes saved."
    return "\n".join(str(note) for note in notebook.data.values())


@input_error
def add_tag(args, notebook):
    if len(args) < 2:
        raise ValueError("Give me title and tag please.")
    title, tag = args[0], args[1]
    note = notebook.find_note(title)
    if not note:
        return "Note not found."
    note.add_tag(tag)
    return "Tag added."


@input_error
def find_by_tag(args, notebook):
    if len(args) < 1:
        raise ValueError("Give me tag please.")
    tag = args[0]
    results = notebook.find_by_tag(tag)
    if not results:
        return "No notes with this tag."
    return "\n".join(str(note) for note in results)


NOTE_COMMANDS = {
    "add-note": add_note,
    "find-note": find_note,
    "delete-note": delete_note,
    "edit-note": edit_note,
    "all-notes": all_notes,
    "add-tag": add_tag,
    "find-by-tag": find_by_tag,
}
