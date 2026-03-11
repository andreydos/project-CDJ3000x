"""Record class for address book contacts."""

from .fields import Name, Phone, Email, Address, Birthday


class Record:
    """Contact record with name, phones, email, address and optional birthday."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None

    def add_phone(self, phone):
        """Add a phone number to the contact."""
        self.phones.append(Phone(phone))

    def add_email(self, email):
        """Add or replace email for the contact."""
        self.email = Email(email)

    def add_address(self, address):
        """Add or replace address for the contact."""
        self.address = Address(address) if address else None

    def add_birthday(self, birthday):
        """Add birthday to the contact."""
        self.birthday = Birthday(birthday)

    def remove_phone(self, phone):
        """Remove a phone number from the contact."""
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        """Replace old phone with new phone."""
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            self.phones[self.phones.index(phone_to_edit)] = Phone(new_phone)
        else:
            raise ValueError(f"Phone {old_phone} not found")

    def find_phone(self, phone):
        """Find phone by value, return None if not found."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        parts = [f"Contact name: {self.name.value}"]
        if self.phones:
            phones_str = "; ".join(p.value for p in self.phones)
            parts.append(f"phones: {phones_str}")
        email = getattr(self, "email", None)
        if email:
            parts.append(f"email: {email.value}")
        address = getattr(self, "address", None)
        if address and address.value:
            parts.append(f"address: {address.value}")
        if self.birthday:
            parts.append(f"birthday: {self.birthday}")
        return ", ".join(parts)
