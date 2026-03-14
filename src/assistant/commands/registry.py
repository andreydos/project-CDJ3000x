"""Command registry with decorator-based registration."""


class CommandRegistry(dict):
    """Registry that collects commands via decorator."""

    def register(self, name: str):
        """Decorator to register a command handler."""

        def decorator(func):
            self[name] = func
            return func

        return decorator


# Registries for contact and note commands
COMMANDS = CommandRegistry()
NOTE_COMMANDS = CommandRegistry()

# Convenience decorators
command = COMMANDS.register
note_command = NOTE_COMMANDS.register
