"""
## Description
This script generates an index file for daily notes of a given year.

It creates a Markdown file with the following sections:
- Metadata: Title, author, type, date, updated date, tags.
- Statistics: Total number of notes in the year and number of notes per month.
- Table of Contents: Lists all notes by month.

The script reads the notes from a directory that is organized by year and month
(e.g., \\\\Orion\\home\\obsidian\\Journal\\2024\\202401).

## Notes
- The script expects the notes to be in Markdown format.
- The filenames of the notes can follow the format `YYYYMMDD.md` or a more complex format like 
  `YYYYMMDD_AnyText.md`. In the latter case, the script will extract the date from the first part 
  of the filename before the underscore.

## Changelog
- Version 1.0
  - 2025-01-11: Initial version
- Version 1.1
  - 2025-01-12: Refactored code into multiple functions
- Version 1.2
  - 2025-01-12: Added support for complex filenames with underscores

## Information
Author: Serge Decker
Date: 2025-01-12
Version 1.2
Licence: MIT
Contact: serge.decker@gmail.com
"""

import os
from datetime import datetime
import re
import locale

# Set the locale to Swiss German
locale.setlocale(locale.LC_ALL, 'de_CH')


def extract_metadata(index_file):
    """Extracts metadata from an existing index file."""
    old_date = ""
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r"date:\s*(.*)", content)
            if match:
                old_date = match.group(1).strip()
    return old_date


def write_metadata(index_file, year, old_date):
    """Writes metadata to the index file."""
    with open(index_file, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: Overview {year} Daily Notes\n")
        f.write("author: Serge Decker\n")
        f.write("type: TableOfContents\n")
        f.write(f"date: {old_date}\n" if old_date else "date: \n")
        f.write(f"updated_date: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("tags:\n  - daily\n  - overview\n  - collection\n")


def write_notes_list(f, year, journal_dir):
    """Writes a list of all daily notes to the index file."""
    found_months = []
    total_notes = 0
    for month in range(1, 13):
        month_dir = os.path.join(journal_dir, f"{year}{month:02d}")
        if os.path.exists(month_dir):
            found_months.append(datetime(int(year), month, 1).strftime('%B'))
            entries = [entry for entry in sorted(os.listdir(month_dir)) if entry.endswith(".md")]
            total_notes += len(entries)
            for entry in entries:
                date_part = entry.split("_")[0]
                f.write(f"- [[{year}{month:02d}/{entry}]]\n")
    return found_months, total_notes


def write_month_tags(f, found_months):
    """Writes German month names as tags to the index file."""
    month_names_de = {
        "January": "Januar", "February": "Februar", "March": "März", "April": "April",
        "May": "Mai", "June": "Juni", "July": "Juli", "August": "August",
        "September": "September", "October": "Oktober", "November": "November", "December": "Dezember"
    }
    for month_name in found_months:
        f.write(f"  - {month_names_de[month_name].lower()}\n")
    f.write(f"  - {year}\n---\n\n")


def write_statistics(f, year, total_notes, journal_dir):
    """Writes statistics about the total number of notes to the index file."""
    f.write(f"## Statistics\n\n**Total number of notes in {year}: {total_notes}**\n\n")
    for month in range(1, 13):
        month_dir = os.path.join(journal_dir, f"{year}{month:02d}")
        if os.path.exists(month_dir):
            entries = [entry for entry in sorted(os.listdir(month_dir)) if entry.endswith(".md")]
            f.write(f"{datetime(int(year), month, 1).strftime('%B')}: {len(entries)} notes\n")
    f.write("\n")


def write_table_of_contents(f, year, journal_dir):
    """Writes a table of contents listing all notes by month to the index file."""
    f.write(f"# Journal {year}\n\n")
    for month in range(1, 13):
        month_dir = os.path.join(journal_dir, f"{year}{month:02d}")
        if os.path.exists(month_dir):
            f.write(f"## {datetime(int(year), month, 1).strftime('%B')}\n\n")
            entries = [entry for entry in sorted(os.listdir(month_dir)) if entry.endswith(".md")]
            for entry in entries:
                f.write(f"- [[{year}{month:02d}/{entry}]]\n")
            f.write("\n")


def generate_index(year):
    """Generates an index file for daily notes of a given year."""
    journal_dir = os.path.join("\\\\Orion\\home\\obsidian\\Journal", str(year))
    index_file = os.path.join(journal_dir, f"Overview {year} DailyNotes.md")

    old_date = extract_metadata(index_file)
    if os.path.exists(index_file):
        os.remove(index_file)

    write_metadata(index_file, year, old_date)

    with open(index_file, "a", encoding="utf-8") as f:
        found_months, total_notes = write_notes_list(f, year, journal_dir)
        write_month_tags(f, found_months)
        write_statistics(f, year, total_notes, journal_dir)
        write_table_of_contents(f, year, journal_dir)


if __name__ == "__main__":
    year = input("Enter the year (e.g. 2024): ")
    generate_index(year)
