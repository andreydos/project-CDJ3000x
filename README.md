# Personal Assistant

CLI application for managing contacts and address book.

## Installation

```bash
# Clone the repository
git clone https://github.com/andreydos/project-CDJ3000x.git
cd project-CDJ3000x

# Install in development mode (can be run from anywhere)
pip install -e .
```

## Running

After installation:

```bash
assistant
```

Or without installation (from project root):

```bash
PYTHONPATH=src python3 -m assistant.main
```

## Commands

| Command | Description |
|---------|-------------|
| `hello` | Greeting |
| `add name [phone]` | Add contact (phone optional) |
| `add-phone name phone` | Add phone to existing contact |
| `add-email name email` | Add or change email |
| `add-address name address...` | Add address |
| `add-birthday name DD.MM.YYYY` | Add birthday |
| `change name old_phone new_phone` | Change phone number |
| `phone name` | Show contact phones |
| `show-birthday name` | Show birthday |
| `birthdays [N]` | Birthdays in next N days (default 7) |
| `search query` | Search by name, phone or email |
| `delete name` | Delete contact |
| `all` | List all contacts |
| `close` / `exit` | Exit |

## Validation

- **Phone**: exactly 10 digits
- **Email**: format `user@domain.tld`
- **Birthday**: format `DD.MM.YYYY`

## Data storage

Data is stored in the user directory:

- Linux/macOS: `~/.local/share/cli-assistant/addressbook.pkl`
- Windows: `%USERPROFILE%\.local\share\cli-assistant\addressbook.pkl`

Data is saved automatically on exit.

## Usage example

```
Enter a command: add John 1234567890
Contact added.
Enter a command: add-email John john@example.com
Email added.
Enter a command: add-birthday John 15.03.1990
Birthday added.
Enter a command: search John
Contact name: John, phones: 1234567890, email: john@example.com, birthday: 15.03.1990
Enter a command: birthdays 14
John: 15.03.2025
Enter a command: exit
Good bye!
```
