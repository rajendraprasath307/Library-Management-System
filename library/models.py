from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='Unknown author')
    general = models.CharField(max_length=100, default='General')
    publisher = models.CharField(max_length=100, default='Unknown Publisher')
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} borrows {self.book.title}"

# Methods:
# __str__:
# This method is overridden to provide a string representation of the object.
# It returns the name of the student when an instance of Student is printed or displayed in contexts like admin panels.


# Explanation: Models: Each model (Student, Book, Borrow) represents a core entity in the library management system:
# students, books, and borrowing transactions.

# Fields: Define the characteristics of each entity, such as name and
# email for students, and title, author, etc., for books.

# Relationships: ForeignKey fields establish relationships
# between models (e.g., each Borrow record links to specific Student and Book instances).

