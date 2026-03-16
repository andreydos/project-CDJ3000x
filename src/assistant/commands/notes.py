"""Note-related command handlers."""

from ..models import Note, NoteBook
from ..utils import input_error, InvalidArgumentsError, NoteNotFoundError
from .registry import note_command


@note_command("add-note")
@input_error
def add_note(args, notebook):
    """Add note: add-note title content"""
    if len(args) < 2:
        raise InvalidArgumentsError("Give me title and content please.")
    title, *content = args
    content = " ".join(content)
    notebook.add_note(Note(title, content))
    return "Note added."


@note_command("find-note")
@input_error
def find_note(args, notebook):
    """Search notes: find-note query"""
    if len(args) < 1:
        raise InvalidArgumentsError("Give me search query please.")
    query = " ".join(args)
    results = [
        str(note)
        for note in notebook.data.values()
        if query.lower() in note.title.lower()
        or query.lower() in note.content.lower()
    ]
    if results:
        return "\n".join(results)
    return "Note not found."


@note_command("delete-note")
@input_error
def delete_note(args, notebook):
    """Delete note: delete-note title"""
    if len(args) < 1:
        raise InvalidArgumentsError("Give me title please.")
    title = args[0]
    result = notebook.delete_note(title)
    if result == "Note not found.":
        raise NoteNotFoundError(result)
    return result


@note_command("edit-note")
@input_error
def edit_note(args, notebook):
    """Edit note: edit-note title new_content"""
    if len(args) < 2:
        raise InvalidArgumentsError("Give me title and new content please.")
    title, *content = args
    content = " ".join(content)
    result = notebook.edit_note(title, content)
    if result == "Note not found.":
        raise NoteNotFoundError(result)
    return result


@note_command("all-notes")
@input_error
def all_notes(args, notebook):
    """List all notes: all-notes"""
    if not notebook.data:
        return "No notes saved."
    return "\n".join(str(note) for note in notebook.data.values())


@note_command("add-tag")
@input_error
def add_tag(args, notebook):
    """Add tag to note: add-tag title tag"""
    if len(args) < 2:
        raise InvalidArgumentsError("Give me title and tag please.")
    title, tag = args[0], args[1]
    note = notebook.find_note(title)
    if not note:
        raise NoteNotFoundError("Note not found.")
    note.add_tag(tag)
    return "Tag added."


@note_command("find-by-tag")
@input_error
def find_by_tag(args, notebook):
    """Search notes by tag: find-by-tag tag"""
    if len(args) < 1:
        raise InvalidArgumentsError("Give me tag please.")
    tag = args[0]
    results = notebook.find_by_tag(tag)
    if not results:
        return "No notes with this tag."
    return "\n".join(str(note) for note in results)
