"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.urls import path
from library import views


urlpatterns = [
    path('', views.index, name='index'),
    # URL: '/', View: 'index', Name: 'index'
    path('students/', views.students, name='students'),
    # URL: /students/ ,View: students Name: students
    path('books/', views.books, name='books'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_book/', views.add_book, name='add_book'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('search_students/', views.search_students, name='search_students'),
    path('search_books/', views.search_books, name='search_books'),

]
