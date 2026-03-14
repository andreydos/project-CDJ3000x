"""Tests for field validation."""

import pytest

from assistant.models import Name, Phone, Email, Address, Birthday


class TestName:
    def test_valid_name(self):
        name = Name("John")
        assert name.value == "John"

    def test_empty_name_raises(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            Name("")
        with pytest.raises(ValueError, match="cannot be empty"):
            Name("   ")


class TestPhone:
    def test_valid_phone(self):
        phone = Phone("1234567890")
        assert phone.value == "1234567890"

    def test_phone_strips_whitespace(self):
        phone = Phone("  1234567890  ")
        assert phone.value == "1234567890"

    def test_short_phone_raises(self):
        with pytest.raises(ValueError, match="exactly 10 digits"):
            Phone("123")

    def test_long_phone_raises(self):
        with pytest.raises(ValueError, match="exactly 10 digits"):
            Phone("12345678901")

    def test_non_digit_phone_raises(self):
        with pytest.raises(ValueError, match="exactly 10 digits"):
            Phone("123456789a")


class TestEmail:
    def test_valid_email(self):
        email = Email("user@example.com")
        assert email.value == "user@example.com"

    def test_invalid_email_raises(self):
        with pytest.raises(ValueError, match="Invalid email"):
            Email("invalid")
        with pytest.raises(ValueError, match="Invalid email"):
            Email("missing@domain")


class TestBirthday:
    def test_valid_birthday(self):
        bd = Birthday("15.03.1990")
        assert str(bd) == "15.03.1990"

    def test_invalid_format_raises(self):
        with pytest.raises(ValueError, match="DD.MM.YYYY"):
            Birthday("1990-03-15")
        with pytest.raises(ValueError, match="DD.MM.YYYY"):
            Birthday("invalid")
