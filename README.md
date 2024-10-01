# Blogging Platform API

This project is a RESTful API for a blogging platform built using Django, Django Rest Framework (DRF), and PostgreSQL. The API provides endpoints for managing blog posts, including creating, reading, updating, and deleting posts. It also supports user registration, login, token-based authentication, and filtering posts by author or creation date.

## Features

- **User Registration & Login**: 
  - Custom API for user registration and login.
  - Token-based authentication using DRF tokens.

- **CRUD Operations for Posts**: 
  - Create, retrieve, update, and delete blog posts.
  - Only the post owner can edit or delete their own posts. **Public** read access to POSTS are allowed.
  - Filter posts by author and creation date.

- **Permissions**:
  - Custom permission class to ensure only post owners can edit/delete their posts.
  - Read permissions are open to all authenticated users.

- **Pagination**:
  - Paginated responses for listing blog posts to handle large datasets efficiently.

- **Filtering**:
  - Filter posts by author and creation date.

## API Endpoints

### Authentication
- **Register**: `POST /api/v1/auth/register/`
- **Login**: `POST /api/v1/auth/login/`

### Posts
- **List Posts**: `GET /api/v1/posts/`
- **Create Post**: `POST /api/v1/posts/`
- **Retrieve Post**: `GET /api/v1/posts/{id}/`
- **Update Post**: `PATCH /api/v1/posts/{id}/`
- **Delete Post**: `DELETE /api/v1/posts/{id}/`

### Filtering & Pagination
- **Filter by Author**: `GET /api/v1/posts/?author=<author_name>`
- **Filter by Date**: `GET /api/v1/posts/?created_on=<YYYY-MM-DD>`
- **Pagination**: Default limit of 10 posts per page. Use `?page=<page_number>` to navigate.

## Getting Started

### Requirements
- Python 3.x
- Django
- Django Rest Framework
- PostgreSQL/SQLite

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/<repo_name>.git
    cd blog_code
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create `.env.development` and `.env.production` files.
    - Add relevant database and secret key configurations.

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional | for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

### Running Tests
Run the test suite with:
```bash
python manage.py test
