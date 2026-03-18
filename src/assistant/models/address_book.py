"""Address book container for contact records."""

from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    """Address book storing contacts by name."""

    def add_record(self, record):
        """Add or update a contact record."""
        self.data[record.name.value] = record

    def find(self, name):
        """Find contact by name, return None if not found."""
        return self.data.get(name)

    def delete(self, name):
        """Delete contact by name."""
        if name in self.data:
            del self.data[name]

    def search(self, query):
        """Search contacts by name, phone or email. Returns list of matching records."""
        query_lower = query.lower()
        results = []
        for name, record in self.data.items():
            if query_lower in name.lower():
                results.append(record)
                continue
            for p in record.phones:
                if query in p.value:
                    results.append(record)
                    break
            else:
                email = getattr(record, "email", None)
                if email and query_lower in email.value.lower():
                    results.append(record)
        return results

    def get_upcoming_birthdays(self, days=0):
        """Get contacts with birthdays today (days=0) or in the next N days (1–365)."""
        today = datetime.today().date()
        result = []

        for name, record in self.data.items():
            if record.birthday is None:
                continue

            birthday = record.birthday.value

            try:
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                birthday_this_year = birthday.replace(month=2, day=28).replace(
                    year=today.year
                )

            if birthday_this_year < today:
                try:
                    birthday_this_year = birthday.replace(year=today.year + 1)
                except ValueError:
                    birthday_this_year = birthday.replace(month=2, day=28).replace(
                        year=today.year + 1
                    )

            days_until = (birthday_this_year - today).days

            if days == 0:
                include = days_until == 0
            else:
                include = 0 <= days_until < days

            if include:
                congratulation_date = birthday_this_year
                weekday = congratulation_date.weekday()

                if weekday == 5:
                    congratulation_date += timedelta(days=2)
                elif weekday == 6:
                    congratulation_date += timedelta(days=1)

                result.append(
                    {
                        "name": name,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                        "_sort_key": congratulation_date,
                    }
                )

        result.sort(key=lambda x: x["_sort_key"])
        for item in result:
            del item["_sort_key"]
        return result
