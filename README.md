# Test Task - Priyanshu Jha

## Introduction

This application is build using `Django-Rest-Framework`, this is made for the review and inspection by the hiring staff at `Thinkflair`.

The application is efficiently handling the creation of `Author` and `Book` models, the validation have been implemented to limit the number of `Book` objects that can be associated with `Author` objects is no more than 5.

The code is well documented and easy to understand for anyone reviewing the logic.

## Instruction on how to set up and run the application

- Clone this repo

- Create virtual environment -

  ```
  python -m venv venv
  ```

- Activate virtual environment -

  `Windows`

  ```
  venv\Scripts\activate
  ```

  `Linux/Unix`

  ```
  source venv/bin/activate
  ```

- Install all the packages from `requirements.txt`
  ```
  pip install -r requirements.txt
  ```

* Create tables that are defined in the `app`

  ```
  python manage.py makemigrations app
  ```

* Migrate to sync the database with custom tables

  ```
  python manage.py migrate
  ```

- Run the development server

  ```
  python manage.py runserver
  ```

- Redirect to `localhost:8000/api/authors/` to test

## Models

### Author Model

**Fields:**

- `id` (AutoField): The unique identifier for the author.
- `name` (CharField): The name of the author.
- `email` (EmailField): The email address of the author.
- `bio` (TextField): The biography of the author.

**Methods:**

```
__str__(self): Returns the name of the author as a string.
```

### Book Model

**Fields:**

- `id` (AutoField): The unique identifier for the book.
- `title` (CharField): The title of the book.
- `publication_date` (DateField): The publication date of the book.
- `author` (ForeignKey to Author model): The author of the book.

**Methods:**

```
__str__(self): Returns the title of the book as a string.
```

## Views

### AuthorListCreateView

**List or Create Authors**

- URL: `/api/authors/`
- Methods:
  - `GET`: Retrieve all authors
  - Response:
    - Status Code: 200 OK
    - Body: List of `Author` objects
  - `POST`: Create a new author.
    - Request Body:
      - `name` (string): The name of the author.
      - `email` (string): The email of the author.
      - `bio` (string): The biography of the author.
    - Response:
      - Status Code: 201 Created
      - Body: Created author object.
    - Errors:
      - Status Code: 400 Bad Request if the request body is invalid.

### AuthorDetailsView

**Retrieve Author Details**

- URL: `/api/authors/<author_id>/`
- Methods:
  - `GET`: Retrieve details of a specific author by ID.
    - Parameters:
      - author_id (int): The ID of the author.
    - Response:
      - Status Code: 200 OK
      - Body: Details of the specified author.
    - Errors:
      - Status Code: 404 Not Found if the specified author ID does not exist.

### BookListCreateView

**List or Create Books**

- URL: `/api/books/`
- Methods:
  - `GET`: Retrieve a list of all books.
    - Response:
      - Status Code: 200 OK
      - Body: List of book objects.
  - `POST`: Create a new book.
    - Request Body:
      - `title` (string): The title of the book.
      - `publication_date` (date): The publication date of the book.
      - `author` (int): The ID of the author of the book.
    - Response:
      - Status Code: 201 Created
      - Body: Created book object.
    - Errors:
      - Status Code: 400 Bad Request if the request body is invalid.
      - Status Code: 400 Bad Request if the specified author has reached the limit of 5 books.

### BookDetailsView

**Retrieve Book Details**

- URL: `/api/books/<book_id>/`
- Methods:
  - `GET`: Retrieve details of a specific book by ID.
  - Parameters:
    `book_id` (int): The ID of the book.
  - Response:
    - Status Code: 200 OK
    - Body: Details of the specified book.
  - Errors:
    - Status Code: 404 Not Found if the specified book ID does not exist.
