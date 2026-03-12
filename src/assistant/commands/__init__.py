"""Command handlers for the assistant CLI."""

from .contacts import COMMANDS
from .notes import NOTE_COMMANDS

__all__ = ["COMMANDS", "NOTE_COMMANDS"]