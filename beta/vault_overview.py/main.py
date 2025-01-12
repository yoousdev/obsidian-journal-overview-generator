"""
## Description
This script generates an overview file (overview.md) in the root directory of the vault,
listing all folders, subfolders, and notes in a hierarchical structure. It also includes
the number of characters in each note.

It creates a Markdown file with the following sections:
- Vault Overview: A hierarchical list of all folders, subfolders, and notes with character count.

The script reads the notes from a directory that is organized by folders and subfolders.

## Notes
- The script expects the notes to be in Markdown format (.md).
- The script skips the '.obsidian' and '.trash' folders.

## Changelog
- Version 1.0
  - 2025-01-12: Initial version
- Version 1.1
  - 2025-01-12: Added character count for each note.

## Information
Author: Serge Decker
Date: 2025-01-12
Version 1.1
Licence: MIT
Contact: serge.decker@gmail.com
"""


import os
from datetime import datetime


def generate_vault_overview(vault_path):
    """
     Generates an overview file (overview.md) in the root directory of the vault,
     listing all folders, subfolders, and notes in a hierarchical structure including
     the character count for each note.
     Args:
         vault_path: The path to the Obsidian vault.
    """

    with open(os.path.join(vault_path, "overview.md"), "w", encoding="utf-8") as f:
        f.write(f"# Vault Übersicht\n\n")
        f.write(f"Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for root, dirs, files in os.walk(vault_path):
            if ".obsidian" in root or ".trash" in root:
                continue

            rel_path = os.path.relpath(root, vault_path)
            level = rel_path.count(os.sep)

            if level > 0:
                f.write(f"{'#' * (level + 1)} {os.path.basename(root)}\n\n")

            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as note_file:
                        content = note_file.read()
                        char_count = len(content)
                f.write(f"- [[{file[:-3]}]] ({char_count})\n")

            f.write("\n")


if __name__ == "__main__":
    vault_path = "\\\\Orion\\home\\obsidian"
    generate_vault_overview(vault_path)
