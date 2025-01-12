# Obsidian Vault Overview Generator

This script generates an overview file (`overview.md`) in the root directory of your Obsidian vault, listing all folders, subfolders, and notes in a hierarchical structure.

## Features

- Creates a Markdown file (`overview.md`) with a hierarchical list of all folders, subfolders, and notes in your vault.
- Skips the `.obsidian` folder to avoid including system files and the '.trash' folder.
- Uses Markdown links (`[[ ]]`) for easy navigation within Obsidian.

## Requirements

- Python 3.11 or higher

## Usage

1.  **Save the script:** Save the script as a Python file (e.g., `vault_overview.py`).
2.  **Edit the script:** Open the script in a text editor and replace `/path/to/your/vault` with the actual path to your Obsidian vault.
3.  **Run the script:** Open a terminal or command prompt and navigate to the directory where you saved the script. Then, run the script using the command `python vault_overview.py`.
