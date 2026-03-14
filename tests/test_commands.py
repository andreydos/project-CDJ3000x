"""Tests for command handlers."""

import pytest

from assistant.models import AddressBook, NoteBook
from assistant.commands import COMMANDS, NOTE_COMMANDS


@pytest.fixture
def book():
    return AddressBook()


@pytest.fixture
def notebook():
    return NoteBook()


class TestContactCommands:
    def test_add_contact(self, book):
        result = COMMANDS["add"](["John", "1234567890"], book)
        assert "added" in result.lower() or "updated" in result.lower()
        assert book.find("John") is not None

    def test_add_contact_invalid_phone(self, book):
        result = COMMANDS["add"](["Jane", "123"], book)
        assert "10 digits" in result

    def test_search_contact(self, book):
        COMMANDS["add"](["Alice", "1234567890"], book)
        result = COMMANDS["search"](["Alice"], book)
        assert "Alice" in result

    def test_hello(self, book):
        result = COMMANDS["hello"]([], book)
        assert "help" in result.lower()

    def test_help(self, book):
        result = COMMANDS["help"]([], book)
        assert "add" in result and "search" in result


class TestNoteCommands:
    def test_add_note(self, notebook):
        result = NOTE_COMMANDS["add-note"](["MyNote", "Some content"], notebook)
        assert "added" in result.lower()
        assert notebook.find_note("MyNote") is not None

    def test_find_note(self, notebook):
        NOTE_COMMANDS["add-note"](["Test", "Hello world"], notebook)
        result = NOTE_COMMANDS["find-note"](["Hello"], notebook)
        assert "Test" in result

    def test_add_tag_and_find_by_tag(self, notebook):
        NOTE_COMMANDS["add-note"](["Note1", "Content"], notebook)
        NOTE_COMMANDS["add-tag"](["Note1", "important"], notebook)
        result = NOTE_COMMANDS["find-by-tag"](["important"], notebook)
        assert "Note1" in result
