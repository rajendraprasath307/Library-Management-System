# Library Management System

![Library Management System](/library/static/Screenshot%202024-06-25%20153749.png)

# Library Management System

This Django-based Library Management System allows you to manage library resources, students, and books efficiently.

## Overview

The Library Management System is a web application built with Django, designed to efficiently manage library resources including students, books, borrowing, and returns.

## Installation

### 1. Install Python and Django

Ensure you have Python and Django installed on your system. If not, follow these steps:

- **Python**: Install Python from [python.org](https://www.python.org/downloads/).
- **Django**: Install Django using pip:
  
## Setup Instructions

To run this project locally:

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd library_management

2. **Install dependencies (assuming you have Python and Django installed):**

   ```bash
   pip install -r requirements.txt

3. **Apply migrations to set up the database:**

   ```bash
   python manage.py migrate

4. **Run the development server:**

   ```bash
   python manage.py runserver

5. **Access the application:**

   Open a web browser and go to [http://localhost:8000](http://localhost:8000) to view the Library Management System.



## Project Structure

-library_management/
-├── **library_management/**         **<- Django project root**
-│   ├── settings.py             <- Django settings file
-│   ├── urls.py                 <- Django root URL configuration
-│   ├── wsgi.py                 <- WSGI configuration for deployment
-│
-├── **library/**                    **<- Django app directory**
-│   ├── models.py               <- Django models for database
-│   ├── views.py                <- Django views for handling requests
-│   ├── templates/              <- Directory for HTML templates
-│   │   ├── base.html           <- Base template for HTML pages
-│   │   ├── index.html          <- Template for home page
-│   │   ├── students.html       <- Template for students page
-│   │   ├── books.html          <- Template for books page
-│   │   ├── add_student.html    <- Template for adding a student
-│   │   ├── add_book.html       <- Template for adding a book
-│   │   ├── borrow_book.html    <- Template for borrowing a book
-│   │   ├── return_book.html    <- Template for returning a book
-│   ├── static/                 <- Directory for static files
-│   │   ├── favicon.ico         <- Favicon icon file
-│   │   ├── styles.css          <- CSS stylesheet
-│   │   └── Screenshot 2024-06-25 153749.png  <- Image file
-│
-├── manage.py                   <- Django's command-line utility for management tasks



## Description

This Django project includes:
- **Models**: Defines database models for `Student`, `Book`, and borrowing relationships.
- **Views**: Handles HTTP requests and renders HTML responses.
- **Templates**: HTML templates for different pages like index, students, books, etc.
- **Static Files**: CSS stylesheet, favicon, and images like `Screenshot 2024-06-25 153749.png`.


## Usage

### Admin Panel

Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/).

Use the superuser credentials to log in and manage students, books, and borrowing records.

### Views

- **Overview**: [http://localhost:8000/](http://localhost:8000/) - Overview with library statistics.
- **Students**: [http://localhost:8000/students/](http://localhost:8000/students/) - List and search students.
- **Books**: [http://localhost:8000/books/](http://localhost:8000/books/) - List and search books.
- **Add Student**: [http://localhost:8000/add_student/](http://localhost:8000/add_student/) - Add a new student.
- **Add Book**: [http://localhost:8000/add_book/](http://localhost:8000/add_book/) - Add a new book.
- **Borrow Book**: [http://localhost:8000/borrow_book/](http://localhost:8000/borrow_book/) - Borrow a book.
- **Return Book**: [http://localhost:8000/return_book/](http://localhost:8000/return_book/) - Return a borrowed book.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

Please ensure your code follows the project's coding conventions and includes relevant test cases.

## Credits

- **Developed by**: rajendraprasath and Open AI
- **Email**: [rajendraprasath307@gmail.com](mailto:rajendraprasath307@gmail.com)
