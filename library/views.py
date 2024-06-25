from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Student, Book, Borrow
from django.utils import timezone


def index(request):
    recent_books = Book.objects.all().order_by('-id')[:5]
    total_books = Book.objects.count()
    total_students = Student.objects.count()
    borrowed_books = Book.objects.filter(is_borrowed=True).count()
    available_books = total_books - borrowed_books

    context = {
        'recent_books': recent_books,
        'total_books': total_books,
        'total_students': total_students,
        'borrowed_books': borrowed_books,
        'available_books': available_books
    }

    return render(request, 'index.html', context)



# Explanation:
# recent_books: Queries the Book model to get the 5 most recent books ordered by descending ID.
# total_books: Counts all records in the Book model.
# total_students: Counts all records in the Student model.
# borrowed_books: Counts books where is_borrowed is True.
# available_books: Calculates available books by subtracting borrowed_books from total_books.
# context: Dictionary containing data to pass to the template.
# render: Renders the index.html template with context.




def students(request):
    students_list = Student.objects.all()
    paginator = Paginator(students_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students.html', {'page_obj': page_obj})



# Explanation:
# students_list: Queries all records from the Student model.
# paginator: Creates a paginator object for students_list with 5 items per page.
# page_number: Retrieves the current page number from the request's GET parameters.
# page_obj: Retrieves the current page's objects using the paginator.
# render: Renders the students.html template with the page_obj.



def books(request):
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 5)  # Show 5 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books.html', {'page_obj': page_obj})



# Explanation:
# books_list: Queries all records from the Book model.
# paginator: Creates a paginator object for books_list with 5 items per page.
# page_number: Retrieves the current page number from the request's GET parameters.
# page_obj: Retrieves the current page's objects using the paginator.
# render: Renders the books.html template with the page_obj.



def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Student.objects.create(name=name, email=email)
        return redirect('students')
    return render(request, 'add_student.html')



# Explanation:
# Checks if the request method is POST.
# Retrieves name and email from POST data.
# Creates a new Student object with the provided data.
# Redirects to the 'students' view after successful creation.
# Renders the add_student.html template if the request method is not POST.



def add_book(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        author = request.POST['author']
        general = request.POST['general']
        publisher = request.POST['publisher']
        Book.objects.create(title=title, author=author, general=general, publisher=publisher)
        return redirect('books')
    return render(request, 'add_book.html')



# Explanation:
# Checks if the request method is POST.
# Retrieves title, author, general, and publisher from POST data.
# Creates a new Book object with the provided data.
# Redirects to the 'books' view after successful creation.
# Renders the add_book.html template if the request method is not POST.



def borrow_book(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        book_id = request.POST['book_id']
        student = Student.objects.get(id=student_id)
        book = Book.objects.get(id=book_id)
        Borrow.objects.create(student=student, book=book)
        book.is_borrowed = True
        book.save()
        return redirect('books')
    students_list = Student.objects.all()
    books_list = Book.objects.filter(is_borrowed=False)
    return render(request, 'borrow_book.html', {'students': students_list, 'books': books_list})




# Explanation:
# Checks if the request method is POST.
# Retrieves student_id and book_id from POST data.
# Retrieves Student and Book objects based on IDs.
# Creates a new Borrow record linking the student and book.
# Sets is_borrowed to True for the book and saves it.
# Redirects to the 'books' view after successful borrowing.
# Retrieves all students and books that are not currently borrowed if the request method is not POST.
# Renders the borrow_book.html template with students and books data.




def return_book(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        book_id = request.POST['book_id']
        borrow = Borrow.objects.get(student_id=student_id, book_id=book_id)
        borrow.return_date = timezone.now()
        borrow.save()
        book = Book.objects.get(id=book_id)
        book.is_borrowed = False
        book.save()
        return redirect('books')
    borrows_list = Borrow.objects.filter(return_date__isnull=True)
    return render(request, 'return_book.html', {'borrows': borrows_list})



# Explanation:
# Checks if the request method is POST.
# Retrieves student_id and book_id from POST data.
# Retrieves the corresponding Borrow record based on student_id and book_id.
# Sets return_date to the current date and time.
# Saves the Borrow record.
# Retrieves the Book based on book_id, sets is_borrowed to False, and saves the book.
# Redirects to the 'books' view after successful return.
# Retrieves all current borrows (return_date__isnull=True) if the request method is not POST.
# Renders the return_book.html template with borrows data.




def search_students(request):
    query = request.GET.get('query')
    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query) | students.filter(email__icontains=query)

    paginator = Paginator(students, 5)  # Show 5 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query
    }
    return render(request, 'students.html', context)



# Explanation:
# Retrieves the query parameter from the GET request.
# Retrieves all Student objects.
# Filters students queryset based on name or email containing the query.
# Creates a paginator object for students with 5 items per page.
# Retrieves the current page number from the GET parameters.
# Retrieves the current page's objects using the paginator.
# Constructs a context dictionary with page_obj and query.
# Renders the students.html template with context.



def search_books(request):
    query = request.GET.get('query')
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query) | \
                books.filter(general__icontains=query)

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query
    }
    return render(request, 'books.html', context)


# Explanation:
# Retrieves the query parameter from the GET request.