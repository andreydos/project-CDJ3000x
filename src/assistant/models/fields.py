"""Field classes for address book records."""

import re
from datetime import datetime


class Field:
    """Base field class for storing values with validation."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Name field with non-empty validation."""

    def __init__(self, value):
        if not value or not str(value).strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field):
    """Phone field with 10-digit validation."""

    def __init__(self, value):
        super().__init__(value)

    def _validate(self, value):
        value_str = str(value).strip()
        return value_str.isdigit() and len(value_str) == 10

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self._validate(value):
            raise ValueError("Phone must contain exactly 10 digits")
        self._value = str(value).strip()


class Email(Field):
    """Email field with format validation."""

    PATTERN = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __init__(self, value):
        if not self.PATTERN.match(str(value).strip()):
            raise ValueError("Invalid email format")
        super().__init__(str(value).strip())


class Address(Field):
    """Address field - plain text, no strict validation."""

    def __init__(self, value):
        super().__init__(str(value).strip() if value else "")


class Birthday(Field):
    """Birthday field with DD.MM.YYYY format validation."""

    MIN_DATE = datetime(1900, 1, 1).date()

    def __init__(self, value):
        try:
            date_obj = datetime.strptime(str(value).strip(), "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        today = datetime.now().date()
        if date_obj < self.MIN_DATE:
            raise ValueError("Birthday cannot be before 1900.")
        if date_obj > today:
            raise ValueError("Birthday cannot be in the future.")
        super().__init__(date_obj)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
