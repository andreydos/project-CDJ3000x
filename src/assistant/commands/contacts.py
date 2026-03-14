"""Contact-related command handlers."""

from ..models import AddressBook, Record
from ..utils import input_error
from .registry import command


@command("hello")
def hello_command(args, book: AddressBook):
    """Greeting: hello"""
    return "How can I help you?"


@command("help")
def help_command(args, book: AddressBook):
    """Show available commands."""
    return """Commands:
    Contacts: add, add-phone, add-email, add-address, add-birthday
            change, phone, all, show-birthday, birthdays, search, delete
    Notes:    add-note, find-note, edit-note, delete-note, all-notes
            add-tag, find-by-tag
    Other:    hello, help, exit/close"""


@command("add")
@input_error
def add_contact(args, book: AddressBook):
    """Add contact: add name [phone]"""
    if len(args) < 1:
        raise ValueError("Give me name please.")
    name = args[0]
    phone = args[1] if len(args) > 1 else None
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@command("add-phone")
@input_error
def add_phone(args, book: AddressBook):
    """Add phone to existing contact: add-phone name phone"""
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args[0], args[1]
    record = book.find(name)
    if record is None:
        raise KeyError()
    record.add_phone(phone)
    return "Phone added."


@command("add-email")
@input_error
def add_email(args, book: AddressBook):
    """Add or replace email: add-email name email"""
    if len(args) < 2:
        raise ValueError("Give me name and email please.")
    name, email = args[0], args[1]
    record = book.find(name)
    if record is None:
        raise KeyError()
    record.add_email(email)
    return "Email added."


@command("add-address")
@input_error
def add_address(args, book: AddressBook):
    """Add or replace address: add-address name address..."""
    if len(args) < 1:
        raise ValueError("Give me name please.")
    name = args[0]
    address = " ".join(args[1:]) if len(args) > 1 else ""
    record = book.find(name)
    if record is None:
        raise KeyError()
    record.add_address(address)
    return "Address added."


@command("add-birthday")
@input_error
def add_birthday(args, book: AddressBook):
    """Add birthday: add-birthday name DD.MM.YYYY"""
    if len(args) < 2:
        raise ValueError("Give me name and birthday (DD.MM.YYYY) please.")
    name, birthday_str = args[0], args[1]
    record = book.find(name)
    if record is None:
        raise KeyError()
    record.add_birthday(birthday_str)
    return "Birthday added."


@command("change")
@input_error
def change_contact(args, book: AddressBook):
    """Change phone: change name old_phone new_phone"""
    if len(args) < 3:
        raise ValueError("Give me name, old phone and new phone please.")
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)
    if record is None:
        raise KeyError()
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@command("phone")
@input_error
def show_phone(args, book: AddressBook):
    """Show phones for contact: phone name"""
    if len(args) < 1:
        raise ValueError("Give me name please.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError()
    if not record.phones:
        return "No phones for this contact."
    return "; ".join(p.value for p in record.phones)


@command("all")
@input_error
def show_all(args, book: AddressBook):
    """List all contacts: all"""
    if not book.data:
        return "No contacts saved."
    lines = []
    for name, record in book.data.items():
        parts = [f"{name}:"]
        if record.phones:
            phones_str = "; ".join(p.value for p in record.phones)
            parts.append(phones_str)
        email = getattr(record, "email", None)
        if email:
            parts.append(f"| {email.value}")
        address = getattr(record, "address", None)
        if address and address.value:
            parts.append(f"| {address.value}")
        if record.birthday:
            parts.append(f"| Birthday: {record.birthday}")
        lines.append(" ".join(parts))
    return "\n".join(lines)


@command("show-birthday")
@input_error
def show_birthday(args, book: AddressBook):
    """Show birthday for contact: show-birthday name"""
    if len(args) < 1:
        raise ValueError("Give me name please.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError()
    if record.birthday is None:
        return "No birthday set for this contact."
    return str(record.birthday)


@command("birthdays")
@input_error
def birthdays(args, book: AddressBook):
    """Show upcoming birthdays: birthdays [N] (default 7 days)"""
    days = 7
    if args:
        try:
            days = int(args[0])
            if days < 1:
                days = 7
        except ValueError:
            pass
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return f"No birthdays in the next {days} days."
    lines = []
    for item in upcoming:
        lines.append(f"{item['name']}: {item['congratulation_date']}")
    return "\n".join(lines)


@command("search")
@input_error
def search_contacts(args, book: AddressBook):
    """Search contacts: search query"""
    if len(args) < 1:
        raise ValueError("Give me search query please.")
    query = " ".join(args)
    results = book.search(query)
    if not results:
        return "Nothing found."
    return "\n".join(str(r) for r in results)


@command("delete")
@input_error
def delete_contact(args, book: AddressBook):
    """Delete contact: delete name"""
    if len(args) < 1:
        raise ValueError("Give me name please.")
    name = args[0]
    if book.find(name) is None:
        raise KeyError()
    book.delete(name)
    return "Contact deleted."
