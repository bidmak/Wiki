# Wiki Encyclopedia

## Overview

This project is a Wiki Encyclopedia that allows users to create, edit, search, and explore encyclopedia entries. Each entry is stored as a Markdown file, and the application provides features like searching, creating new pages, editing content, and even exploring random entries.

## Features

### Entry Page

- Visiting `/wiki/TITLE` renders a page displaying the contents of the encyclopedia entry with the specified title.
- Utilizes functions from `encyclopedia/util.py` to manage entry content.
- Handles cases where the requested entry does not exist, displaying an error page.

### Index Page

- Updated `index.html` allows users to click on any entry name to be taken directly to that entry's page.

### Search

- Users can type a query into the search box in the sidebar.
- Redirects to the entry page if the query matches an entry name.
- Shows a search results page with entries containing the query as a substring if no direct match is found.
- Clicking on any entry name on the search results page takes the user to that entry's page.

### New Page

- Clicking "Create New Page" in the sidebar takes the user to a page to create a new encyclopedia entry.
- Users can enter a title and Markdown content in a textarea.
- Allows users to save the new page.
- Displays an error message if an entry with the provided title already exists.
- Saves the new entry to disk and redirects the user to the new entry's page upon successful creation.

### Edit Page

- On each entry page, users can click a link to edit the entry's Markdown content in a textarea.
- The textarea is pre-populated with the existing content.
- Users can save changes and are redirected back to the entry's page.

### Random Page

- Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

- Converts Markdown content in the entry file to HTML before displaying it to the user.
- Utilizes the `python-markdown2` package for this conversion (`pip3 install markdown2`).

## Challenge (Optional)

- Implemented Markdown to HTML conversion without using external libraries.
- Supports headings, boldface text, unordered lists, links, and paragraphs using regular expressions in Python.

## How to Run

1. Download the distribution code or create the necessary files.
2. Run migrations with `python manage.py migrate`.
3. Start the Django development server with `python manage.py runserver`.
4. Open the web browser and visit `http://127.0.0.1:8000` to access the Wiki encyclopedia.

Feel free to explore, create new entries, edit content, search for information, and enjoy the Wiki experience!

## Acknowledgments

This project is part of the CS50 Web Programming with Python and JavaScript course. The distribution code and backend logic were provided by the course instructors.
