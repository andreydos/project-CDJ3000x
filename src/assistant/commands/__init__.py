"""Command handlers for the assistant CLI."""

from .registry import COMMANDS, NOTE_COMMANDS

# Import modules to trigger @command / @note_command registration
from . import contacts  # noqa: F401
from . import notes  # noqa: F401

__all__ = ["COMMANDS", "NOTE_COMMANDS"]
