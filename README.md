# Book Manager API

A REST API for managing books, built with Django and Django REST Framework.

## How to run
1. Create and activate a virtual environment:
   `python -m venv venv` then `venv\Scripts\activate`
2. Install packages:
   `pip install django djangorestframework django-cors-headers`
3. Set up the database:
   `python manage.py migrate`
4. Start the server:
   `python manage.py runserver`

## Endpoints
- `GET /api/books/` list books
- `POST /api/books/` create a book
- `GET/PUT/PATCH/DELETE /api/books/<id>/` view, update or delete one book
- `GET /api/books/?search=python` search by title or author
- `GET /api/books/available/` list only available books
