# HTML Bookmark URL Extractor

A Python script to extract all `href` attribute values (URLs and other link targets) from an HTML bookmark file. It uses regular expressions, removes duplicate entries, and can output the results to the console or a text file.

## Features

*   Extracts all values from `href="..."` attributes in an HTML file.
*   Handles variations in attribute formatting (e.g., `href = "..."`, `href="..."`, single or double quotes).
*   Removes duplicate URLs, providing a unique, sorted list.
*   Prompts the user for the input bookmark file path and an optional output file path.
*   Outputs extracted URLs to the console if no output file path is provided.
*   Saves extracted URLs to a specified text file if a path is provided.
*   Includes basic error handling for file operations (file not found, read/write errors).
*   No external libraries required (uses Python's built-in `re` module).

## Prerequisites

*   Python 3.6 or higher (mainly for f-strings, but adaptable for older Python 3).
*   An HTML bookmark file (typically exported from a web browser).

## Installation

No special installation is needed beyond having Python 3 installed.

1.  Clone this repository or download the script.
    ```bash
    git clone [<your-repo-url>](https://github.com/alfinjerome/BookmarkLinksExtractor)
    cd BookmarkLinksExtractor
    ```
    Or simply download the Python file.

## Usage

1.  Ensure your exported HTML bookmark file is accessible.
2.  Run the script from your terminal:
    ```bash
    python BookmarkLinksExtractor.py
    ```
3.  **Follow the prompts:**
    *   **"Enter the bookmark file path: "**: Type the full or relative path to your HTML bookmark file and press Enter.
        *   Example: `my_bookmarks.html` or `/path/to/my_bookmarks.html`
    *   **"Enter the output file path (leave blank to print to console): "**:
        *   To save to a file: Type the desired path for the output text file (e.g., `extracted_links.txt`) and press Enter.
        *   To print to console: Simply press Enter without typing anything.
