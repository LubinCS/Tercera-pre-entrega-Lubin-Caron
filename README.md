# TerceraEntregaLubin

## Project Description
This Django project is a book management system that allows users to add authors, books, and reviews, as well as search for books.

## Features
- Add new authors
- Add new books
- Add reviews for books
- Search for books by title or author

## Requirements
- Python 3.x (specify the version, e.g., Python 3.8)
- Django 4.x (specify the version, e.g., Django 4.2)

## Setup and Installation
1. Ensure you have Python installed on your system.

2. Navigate to the project directory: 
   ```bash
   cd path/to/TerceraEntregaLubin

3. Create a virtual environment (optional but recommended):
    python -m venv env

4. Install the required packages:
    pip install -r requirements.txt

5. Apply migrations:
    python manage.py migrate

## Running the Project
1. Ensure you're in the project directory and your virtual environment is activated (if you're using one).

2. Start the development server:
    python manage.py runserver

3. Open a web browser and go to http://127.0.0.1:8000/

## URL Patterns
    Home: /
    Add Author: /add_author/
    Add Book: /add_book/
    Add Review: /add_review/
    Search Books: /search_books/

## Testing
1. Ensure the server is running (python manage.py runserver)

2. Visit each URL listed above to test the corresponding functionality.

3. Try adding authors, books, and reviews.

4. Test the search functionality with different queries.

## Known Issues
    (List any known bugs or limitations, if applicable)


## Contributing
    If you wish to contribute to this project, please fork the repository and create a pull request.