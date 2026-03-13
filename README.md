# Personal Assistant

CLI application for managing contacts and address book.

## Installation

```bash
git clone https://github.com/andreydos/project-CDJ3000x.git
cd project-CDJ3000x
```

### Global install (run from anywhere)

**Option A — pipx** (recommended):
```bash
pipx install -e .
pipx ensurepath
```
Then restart the terminal or run `source ~/.bashrc` (or `source ~/.zshrc`). This adds `~/.local/bin` to PATH so `assistant` works from any folder.

Requires [pipx](https://github.com/pypa/pipx). If not installed: `sudo apt install pipx` (Linux) or `pip install pipx` (Windows).

**Option B — venv:**
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```
Then run `assistant` only when venv is activated, or use `.venv/bin/assistant` from project root.

### Run without install

From project root:
```bash
PYTHONPATH=src python3 -m assistant.main
```

## Running

```bash
assistant
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
| `add-note title content` | Add note |
| `find-note query` | Search notes by title or content |
| `edit-note title new_content` | Edit note |
| `delete-note title` | Delete note |
| `all-notes` | List all notes |
| `add-tag title tag` | Add tag to note |
| `find-by-tag tag` | Search notes by tag |
| `close` / `exit` | Exit |

## Validation

- **Phone**: exactly 10 digits
- **Email**: format `user@domain.tld`
- **Birthday**: format `DD.MM.YYYY`

## Data storage

Data is stored in the user directory:

- Linux/macOS: `~/.local/share/cli-assistant/`
- Windows: `%USERPROFILE%\.local\share\cli-assistant\`

Files: `addressbook.pkl` (contacts), `notebook.pkl` (notes).

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
