from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3.")

def add(request):
    return render(request, "add.html")

def create(request):
    return render(request, "created.html")

def del1(request):
    return render(request, "del.html")