"""Tests for AddressBook, Record, Note, NoteBook."""

import pytest

from assistant.models import AddressBook, Record, Note, NoteBook


class TestRecord:
    def test_add_contact(self):
        record = Record("Alice")
        record.add_phone("1234567890")
        record.add_email("alice@test.com")
        assert record.name.value == "Alice"
        assert len(record.phones) == 1
        assert record.phones[0].value == "1234567890"
        assert record.email.value == "alice@test.com"

    def test_edit_phone(self):
        record = Record("Bob")
        record.add_phone("1234567890")
        record.edit_phone("1234567890", "0987654321")
        assert record.phones[0].value == "0987654321"


class TestAddressBook:
    def test_add_and_find(self):
        book = AddressBook()
        record = Record("Charlie")
        record.add_phone("1234567890")
        book.add_record(record)
        found = book.find("Charlie")
        assert found is not None
        assert found.name.value == "Charlie"

    def test_search_by_name(self):
        book = AddressBook()
        book.add_record(Record("Alice"))
        book.add_record(Record("Bob"))
        results = book.search("Ali")
        assert len(results) == 1
        assert results[0].name.value == "Alice"

    def test_delete(self):
        book = AddressBook()
        book.add_record(Record("Dave"))
        book.delete("Dave")
        assert book.find("Dave") is None


class TestNote:
    def test_note_with_tags(self):
        note = Note("Title", "Content", tags=["tag1"])
        assert note.title == "Title"
        assert note.content == "Content"
        assert "tag1" in note.tags

    def test_add_tag(self):
        note = Note("Title", "Content")
        note.add_tag("work")
        assert "work" in note.tags


class TestNoteBook:
    def test_add_and_find_note(self):
        nb = NoteBook()
        nb.add_note(Note("Meeting", "Discuss project"))
        found = nb.find_note("Meeting")
        assert found is not None
        assert found.content == "Discuss project"

    def test_find_by_tag(self):
        nb = NoteBook()
        note = Note("Task", "Do something", tags=["urgent"])
        nb.add_note(note)
        results = nb.find_by_tag("urgent")
        assert len(results) == 1
        assert results[0].title == "Task"
