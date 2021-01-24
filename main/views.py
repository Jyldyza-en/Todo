from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Bookstore

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    book_list = Bookstore.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def third(request):
    return HttpResponse("This is page test3.")

def add(request):
    return render(request, "add.html")

def create(request):
    return render(request, "created.html")

def dell(request):
    return render(request, "del.html")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["books_title"]
    subtitle = form["books_subtitle"]
    description = form["books_description"]
    price = form["books_price"]
    genre = form["books_genre"]
    author = form["books_author"]
    year = form["books_year"]
    book = Bookstore(title=title,subtitle=subtitle,description=description,price=price,genre=genre,author=author,year=year)
    book.save()
    return redirect(second)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)
