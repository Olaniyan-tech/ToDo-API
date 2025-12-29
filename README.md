# Django Todo API
This project is a Django-based Todo API application with user registration, login/logout, JWT authentication, and task management functionalities using Django REST Framework.


## Project Overview

This project provides a RESTful API for managing user accounts and personal tasks.
Each user can register, log in, and manage their own tasks securely using JWT authentication.


## Features

- User registration and authentication
- JWT-based login and logout
- Token refresh using HTTP-only cookies
- Create, read, update, and delete tasks
- User-specific task ownership
- Task search functionality

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Olaniyan-tech/ToDo-API.git]
   cd ToDo-API

2. Create a virtual environment
   python -m venv env

3. Activate the virtual environment
   env\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Run migrations
   python manage.py migrate

6. Start the server
   python manage.py runserver






