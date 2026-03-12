from collections import UserDict



class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"

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

