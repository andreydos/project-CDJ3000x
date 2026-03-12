"""Note model."""

from collections import UserDict


class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        tags_str = f", Tags: {', '.join(self.tags)}" if self.tags else ""
        return f"Title: {self.title}, Content: {self.content}{tags_str}"


class NoteBook(UserDict):
    def add_note(self, note):
        self.data[note.title] = note

    def find_note(self, title):
        return self.data.get(title)

    def delete_note(self, title):
        if title in self.data:
            self.data.pop(title)
            return "Note deleted."
        return "Note not found."

    def edit_note(self, title, new_content):
        note = self.find_note(title)
        if note:
            note.content = new_content
            return "Note updated."
        return "Note not found."

    def find_by_tag(self, tag):
        return [note for note in self.data.values() if tag in note.tags]
    