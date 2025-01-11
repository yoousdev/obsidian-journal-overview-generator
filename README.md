This Python script generates an index file for your daily notes in Obsidian. It creates a yearly overview with metadata, statistics, and a table of contents that lists all your notes by month. Additionally, it generates a monthly index file for each month, which is linked in the yearly overview.

**Features:**

* Generates a yearly index file with:
    * Metadata (title, author, type, date, updated date, tags)
    * Statistics (total number of notes, notes per month)
    * Table of contents with links to monthly index files
* Generates monthly index files with a list of daily notes.
* Extracts metadata from existing index files to preserve the last updated date.
* Supports complex filenames with underscores.

**Requirements:**

* Python 3
* Your daily notes are organized in a directory by year and month (e.g., `\\Orion\home\obsidian\Journal\2024\202401`).
* Your notes are in Markdown format.

**Usage:**

1. Clone the repository: `git clone https://github.com/egemasta/python_script.git`
2. Navigate to the script directory: `cd python_script`
3. Run the script: `python main.py`
4. Enter the year for which you want to generate the overview.

The script will create the yearly and monthly index files in the corresponding directory.

**Customization:**

* You can adjust the path to your journal directory in the `generate_index` function.
* You can modify the metadata in the `write_metadata` function.


**License:**

MIT License

**Contributing:**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
